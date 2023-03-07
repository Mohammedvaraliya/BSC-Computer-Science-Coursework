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
