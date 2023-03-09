# layouts_flutter_pract_11

**Aim : Create an app using Flutter to demonstrate navigation in an App**

## Initializing a Flutter project.

1. Initialize a `Flutter` project using `flutter`.
    
    ```bash
    flutter create navigation_flutter_pract_12
    ```
    
2. Add Following Code in `main.dart` file
    
    ```dart
    import 'package:flutter/material.dart';
    import 'package:layouts_flutter_pract_11/container_layout.dart';
    import 'package:layouts_flutter_pract_11/column_layout.dart';
    import 'package:layouts_flutter_pract_11/gridview_layout.dart';
    import 'package:layouts_flutter_pract_11/listtile_layout.dart';
    import 'package:layouts_flutter_pract_11/row_layout.dart';
    import 'package:layouts_flutter_pract_11/stack_layout.dart';
    
    void main() {
      runApp(MyApp());
    }
    
    class MyApp extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          title: 'Layout Demo',
          home: HomePage(),
          theme: ThemeData(
            elevatedButtonTheme: ElevatedButtonThemeData(
              style: ElevatedButton.styleFrom(
                primary: Colors.blueGrey[700],
                onPrimary: Colors.white,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16.0),
                ),
                elevation: 4.0,
                textStyle: TextStyle(
                  fontSize: 24.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        );
      }
    }
    
    class HomePage extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Layout Demo'),
          ),
          body: SafeArea(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ContainerLayout(),
                      ),
                    );
                  },
                  child: Text('Container Layout'),
                ),
                SizedBox(height: 16.0),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => RowLayout(),
                      ),
                    );
                  },
                  child: Text('Row Layout'),
                ),
                SizedBox(height: 16.0),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => StackLayout(),
                      ),
                    );
                  },
                  child: Text('Stack Layout'),
                ),
                SizedBox(height: 16.0),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ColumnLayout(),
                      ),
                    );
                  },
                  child: Text('Column Layout'),
                ),
                SizedBox(height: 16.0),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => GridViewLayout(),
                      ),
                    );
                  },
                  child: Text('GridView Layout'),
                ),
                SizedBox(height: 16.0),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ListTileLayout(),
                      ),
                    );
                  },
                  child: Text('ListTile Layout'),
                ),
              ],
            ),
          ),
        );
      }
    }
    ```
    
3. Create new dart file in `lib` directory named `container_layout.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class ContainerLayout extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Small Container'),
          ),
          body: Center(
            child: Container(
              height: 400.0,
              width: 400.0,
              color: Colors.blue,
              child: Center(
                child: Text(
                  'This is a small container',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 24.0,
                  ),
                ),
              ),
            ),
          ),
        );
      }
    }
    ```
    
4. Create new dart file in `lib` directory named `row_layout.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class RowLayout extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Row Layout'),
          ),
          body: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              Container(
                color: Colors.red,
                width: 100.0,
                height: 100.0,
              ),
              Container(
                color: Colors.green,
                width: 100.0,
                height: 100.0,
              ),
              Container(
                color: Colors.yellow,
                width: 100.0,
                height: 100.0,
              ),
            ],
          ),
        );
      }
    }
    ```
    
5. Create new dart file in `lib` directory named `stack_layout.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class StackLayout extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Stack Layout Demo'),
          ),
          body: Stack(
            children: [
              Positioned(
                top: 20.0,
                left: 20.0,
                child: Container(
                  width: 100.0,
                  height: 100.0,
                  color: Colors.red,
                ),
              ),
              Positioned(
                top: 50.0,
                left: 50.0,
                child: Container(
                  width: 100.0,
                  height: 100.0,
                  color: Colors.green,
                ),
              ),
              Positioned(
                top: 80.0,
                left: 80.0,
                child: Container(
                  width: 100.0,
                  height: 100.0,
                  color: Colors.blue,
                ),
              ),
            ],
          ),
        );
      }
    }
    ```
    
6. Create new dart file in `lib` directory named `column_layout.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class ColumnLayout extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Column Layout Demo'),
          ),
          body: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Expanded(
                flex: 1,
                child: Container(
                  color: Colors.red,
                  child: Center(
                    child: Text(
                      'Column 1',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 24.0,
                      ),
                    ),
                  ),
                ),
              ),
              SizedBox(height: 16.0),
              Expanded(
                flex: 2,
                child: Container(
                  color: Colors.green,
                  child: Center(
                    child: Text(
                      'Column 2',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 24.0,
                      ),
                    ),
                  ),
                ),
              ),
              SizedBox(height: 16.0),
              Expanded(
                flex: 3,
                child: Container(
                  color: Colors.blue,
                  child: Center(
                    child: Text(
                      'Column 3',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 24.0,
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        );
      }
    }
    ```
    
7. Create new dart file in `lib` directory named `gridview_layout.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class GridViewLayout extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('GridView Layout Demo'),
          ),
          body: GridView.count(
            crossAxisCount: 2,
            children: [
              Container(
                color: Colors.red,
              ),
              Container(
                color: Colors.green,
              ),
              Container(
                color: Colors.blue,
              ),
              Container(
                color: Colors.yellow,
              ),
              Container(
                color: Colors.orange,
              ),
              Container(
                color: Colors.purple,
              ),
            ],
          ),
        );
      }
    }
    ```
    
8. Create new dart file in `lib` directory named `listtile_layout.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    
    class ListTileLayout extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('ListTile Layout Demo'),
          ),
          body: ListView(
            children: [
              ListTile(
                leading: Icon(Icons.person),
                title: Text('John Doe'),
                subtitle: Text('johndoe@example.com'),
                trailing: Icon(Icons.arrow_forward),
                onTap: () {
                  // Navigate to user profile page
                },
              ),
              ListTile(
                leading: Icon(Icons.person),
                title: Text('Jane Doe'),
                subtitle: Text('janedoe@example.com'),
                trailing: Icon(Icons.arrow_forward),
                onTap: () {
                  // Navigate to user profile page
                },
              ),
              ListTile(
                leading: Icon(Icons.person),
                title: Text('Bob Smith'),
                subtitle: Text('bobsmith@example.com'),
                trailing: Icon(Icons.arrow_forward),
                onTap: () {
                  // Navigate to user profile page
                },
              ),
            ],
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

![Frame 13](https://user-images.githubusercontent.com/95087498/223936031-2510eb63-e53c-4de3-80a0-92d0be100376.png)

![Frame 14](https://user-images.githubusercontent.com/95087498/223936051-ed7f7ccd-b973-4ab5-a7fc-2c70cfce0afe.png)

![Frame 15](https://user-images.githubusercontent.com/95087498/223936071-9aca7864-1328-4646-b999-3e5085b075d2.png)

![Frame 16](https://user-images.githubusercontent.com/95087498/223936090-3c0bb422-62fd-4a25-b8ea-0c88e9f48a87.png)
