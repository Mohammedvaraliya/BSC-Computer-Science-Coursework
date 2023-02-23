import 'package:flutter/material.dart';
import 'package:user_auth_flutter_pract_09/user_db.dart';
import './login_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.orange,
        ),
        home: LoginPage(
          userDb: UserDb(),
        ));
  }
}
