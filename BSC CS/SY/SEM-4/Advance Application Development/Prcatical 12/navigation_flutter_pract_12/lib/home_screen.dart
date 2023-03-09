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
