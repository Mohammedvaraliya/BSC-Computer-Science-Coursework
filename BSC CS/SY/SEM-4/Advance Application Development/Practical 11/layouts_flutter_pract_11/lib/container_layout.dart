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
