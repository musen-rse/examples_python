# Weather Station Story

## The application
Our company creates a popular weather station software. It controls a temperature sensor that measures the temperature every second. Whenever the temperature is measured we want to update a temperature display.

## Starting point
The `Application` class contains an instance of the `TemperatureSensor` and a `ConsoleTableChart`. The sensor knows the chart and will call the chart’s `draw()` method whenever it measures a new value.

## Stage 1: A second chart
Our glorious overlords (managers) have graced us with a new feature request to keep up with the competition: adding a bar chart to the application.

### The problem
In the current state of the application the sensor can only deal with one specific type of chart (`ConsoleTableChart`).

### The solution
After implementing the `ConsoleBarChart` we extract a common `Chart` interface with an abstract `draw()` method that both chart types must implement.
Now the sensor does not depend on a concrete chart type, but only the `Chart` interface, therefore adhering to the **Dependency Inversion Principle (DIP)**.

## Stage 2: Mass producing charts
During the next code review session we show our implementation to our colleagues. They point out that in the `Application` class we still depend on the concrete chart types `ConsoleTableChart` and `ConsoleBarChart` that change frequently. Also there will be new chart variants in the future so they ask us to improve our solution.

### The problem
Our `Application` class needs to create instances of the concrete chart types to pass them on to our sensor.

### The solution
We’ve heard about the **Abstract Factory Pattern** that encapsulates the creation of objects and exposes them only through their common interface afterwards. 
Therefore, we decide to implement an abstract `ChartFactory` that defines abstract `create_table_chart()` and `create_bar_chart()` methods that both return objects of the abstract type `Chart`. 
The `ConsoleChartFactory` implements this interface and creates and returns  `ConsoleTableChart` and `ConsoleBarChart`  instances.

We inject this factory into the constructor of the `Application` class leading to an application core that does not depend on any concrete chart types anymore.

## Stage 3: Reduce coupling
Our boss informs us that there is still a weakness in our design. Since we will add more charts in the future, we would have to change the interface of the factory each time. Since interfaces should be stable we need to come up with a better solution.
While we are at it we can also implement a feature request from our clients for a menu that allows the users to select a chart type when the application starts.


### The problem
We notice that with our current implementation of the `ChartFactory` the `Application` class still has a dependency to the specific method name of the specific chart we want to create. This means we have add a method call for every new chart type in our `Application` class. Even worse, this also implies that whenever we need new chart types we need to add a new method to the `ChartFactory` interface, which is part of our application core. Both are violations of the Open Closed Principle (OCP).


### The solution
We change our `ChartFactory` interface to contain a single `create_chart(chart_type: str)`  method that accepts the chart type as a string. By doing this we loose some safety because the methods accepts any string valid or not. But we also add another method `get_chart_choices()` that returns a list of strings with all of possible chart types. 
In our `Application` class we can now display the possible choices in our selection menu and select a chart type without changing anything in that class.

## Stage 4: A second sensor
To stay ahead of the competition we decide to add a humidity sensor as a second sensor type to our application. Our boss reassures us that the sensors are known up front and will not be created dynamically at runtime, so no need for an additional factory. However, both sensors need to be able to send updates to a chart.
 

### The problem
We implement the `HumiditySensor` class and notice that there are some striking similarities to the `TemperatureSensor`. They both have a `measure()` method and both also implement the exact same logic to add /remove and draw their attached `Chart`s which violates the **Don’t Repeat Yourself Principle (DRY)**. 

### The solution
We decide to extract a common abstract `Sensor` base class that both the `TemperatureSensor` and `HumiditySensor` inherit from. The `Sensor` class defines an abstract `measure()` method and contains the logic to add/remove charts and a `draw_all()` method that calls the `draw()` method of every chart attached to the sensor. The `TemperatureSensor` and  `HumiditySensor` can now call this method whenever they measure a new value without needing to implement the logic themselves.


## Stage 5: Logging

Our charts have been showing some weird data. To find out what's happening under the hood we want to log the values produced by the sensors to a file.
One colleague suggests that we implement a file logger that implements the `Chart` interface, so it could be updated with the latest values along with the regular `Chart`s as well. While we think that this is a good idea in general, we argue that a logger is conceptually something different than a chart, so we'd like to come up with a better solution.

### The problem
We need to implement a file logger that is updated along with the charts without using the `Chart` interface.

### The solution
We decide to introduce a new interface called `Observer` that contains an `update()` method that both the charts and the new file logger will implement.
Instead of using `Chart`s our sensors will now talk to `Observer` instances. At this point we notice that managing `Observers` and measuring data are different responsibilities as well. To separate these responsibilities we extract an abstract `Subject` class that only contains the code to manage `Observers` while keeping the `measure()` method in the `Sensor` class.
Finally we make `Sensor` class inherit from the `Subject` class.
We now have a generic mechanism to notify interested components of our application about updates. This is called the **Observer Pattern**.

## Stage 6: Another strategy

Our clients are complaining again. This time it's the resource consumption of our application. Some of them are using it on very low power machines. Measuring the sensors and updating the charts every second is too much for those tiny CPUs. Some want to have the application only display the data once and then exit, others would like to trigger an update manually and the rest want to keep the continuous updating we already have.

### The problem
We need to implement a mechanism that allows us to measure the data at different times. Since some of our clients want to trigger updates manually we can't just set a different timer value. 

### The solution
We could have an `if` statement in the `Application`'s `run()` method to determine when to measure and update our charts. However, that would violate the **Open Closed Principle** since we'd have to extend that `if` statement whenever the requirements for updating change. Instead we decide to apply the **Dependency Inversion Principle** and encapsulate the algorithm that determines when we want to call the `measure()` method into different classes that all implement a common interface that we'll call `MeasureStrategy`.
When starting our program we inject either a `OneTimeMeasureStrategy`, a `ManualMeasureStrategy` or a `ContinuousMeasureStrategy` into the `Application` class. Instead of calling the sensor's measure method itself, the `Application` class will delegate that responsibility to the respective `Strategy`. We call this the **Strategy Pattern**.
