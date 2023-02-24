## Activity Life Cycle
<br>

### My Android Application

This is an Android application that demonstrates the activity lifecycle in Android. The application was built using Android Studio and programmed in Kotlin.

### Features

The application has a single activity that overrides all of the activity lifecycle methods, including:

* `onCreate()`: called when the activity is first created.
* `onStart()`: called when the activity is becoming visible to the user.
* `onResume()`: called when the activity will start interacting with the user.
* `onPause()`: called when the activity is going into the background, but has not been destroyed.
* `onStop()`: called when the activity is no longer visible to the user.
* `onDestroy()`: called when the activity is being destroyed.
* `onRestart()`: called when the activity is restarting after being stopped.

Each of these methods returns a Toast message that indicates which method is currently being executed.

### Installation

1. Clone this repository: 

        git clone https://github.com/Mohammedvaraliya/BSC-CS-Practical-Performed.git
2. Open the project in Android Studio
3. Build and run the project on an emulator or physical device

### Usage

Once the application is installed on your device, open the application to see the activity lifecycle methods in action. The application will display a Toast message each time a lifecycle method is called, indicating which method is being executed.

### Overview



### Contributing

Contributions are always welcome! If you have any ideas or suggestions for improving the app, feel free to create a pull request or open an issue.