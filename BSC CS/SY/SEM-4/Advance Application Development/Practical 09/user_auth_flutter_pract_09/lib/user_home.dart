// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';

class UserHome extends StatelessWidget {
  final String username;

  const UserHome({super.key, required this.username});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("User Home"),
      ),
      body: Container(
        alignment: Alignment.center,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Welcome, $username!",
              style: TextStyle(fontSize: 24),
            ),
            SizedBox(height: 16),
            Text(
              "You have successfully logged in.",
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}
