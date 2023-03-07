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
