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
