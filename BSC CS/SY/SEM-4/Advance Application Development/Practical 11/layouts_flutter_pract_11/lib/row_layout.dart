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
