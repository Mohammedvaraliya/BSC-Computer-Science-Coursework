# navigation_flutter_pract_12

**Aim : Create an app using Flutter to demonstrate navigation in an App**

## Initializing a Flutter project.

1. Initialize a `Flutter` project using `flutter`.
    
    ```bash
    flutter create navigation_flutter_pract_12
    ```
    
2. Add Following Code in `main.dart` file
    
    ```dart
    import 'package:flutter/material.dart';
    import 'package:navigation_flutter_pract_12/home_screen.dart';
    import 'package:navigation_flutter_pract_12/detail_screen.dart';
    
    void main() {
      runApp(const MyApp());
    }
    
    class MyApp extends StatelessWidget {
      const MyApp({super.key});
    
      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          title: 'Navigation Demo',
          initialRoute: '/',
          routes: {
            '/': (context) => HomeScreen(),
            '/detail': (context) => DetailScreen(),
          },
        );
      }
    }
    ```
    
3. Create new dart file in `lib` directory named `home_screen.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class HomeScreen extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Home Screen'),
          ),
          body: Center(
            child: ElevatedButton(
              child: Text('Go to Detail Screen'),
              onPressed: () {
                Navigator.pushNamed(context, '/detail');
              },
            ),
          ),
        );
      }
    }
    ```
    
4. Create new dart file in `lib` directory named `detail_screen.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class DetailScreen extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Detail Screen'),
          ),
          body: Center(
            child: ElevatedButton(
              child: Text('Go back to Home Screen'),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
          ),
        );
      }
    }
    ```
    

**Running a project**

**Connect Phone**

make sure USB debugging is enabled in Developer option

**Run The app**

```bash
flutter run main.dart
```

**Output:**

![Frame 12](https://user-images.githubusercontent.com/95087498/223932776-c7089dae-14e8-4094-9c2b-0dd7aedc845e.png)

