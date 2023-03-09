# User Authentication App

**Aim : Create an app using Flutter for User Authentication**

## Initializing a Flutter project.

1. Initialize a `Flutter` project using `flutter`.
    
    ```bash
    flutter create userauth_flutter_pract_09
    ```
    
2. Add Following Code in `main.dart` file
    
    ```dart
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
    ```
    
3. Create new dart file in `lib` directory named `user_db.dart`.
    
    And add the following code in that file.
    
    ```dart
    class UserDb {
      final Map<String, String> _users = {
        'student': '1234',
        'mvlu': 'password',
        'system': 'admin',
        'root': 'admin',
        'varaliya': 'varaliya123'
      };
    
      bool authenticate(String username, String password) {
        if (_users.containsKey(username) && _users[username] == password) {
          return true;
        }
        return false;
      }
    
      bool userExist(String username) {
        return _users.containsKey(username);
      }
    
      void addUser(String username, String password) {
        if (!_users.containsKey(username)) {
          _users[username] = password;
        } else {
          throw Exception('Username already exists!');
        }
      }
    }
    ```
    
4. Create new dart file in `lib` directory named `create_user.dart`.
    
    And add the following code in that file.
    
    ```dart
    import 'package:flutter/material.dart';
    import 'package:user_auth_flutter_pract_09/user_db.dart';
    import 'login_page.dart';
    
    class CreateUser extends StatefulWidget {
      final UserDb userDb;
    
      const CreateUser({Key? key, required this.userDb}) : super(key: key);
    
      @override
      _CreateUserState createState() => _CreateUserState();
    }
    
    class _CreateUserState extends State<CreateUser> {
      final _formKey = GlobalKey<FormState>();
      final _usernameController = TextEditingController();
      final _passwordController = TextEditingController();
    
      void _addUser(String username, String password) {
        UserDb userDb = UserDb();
        if (userDb.userExist(username)) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content:
                  Text("Username already exists. Please try another username."),
            ),
          );
        } else {
          userDb.addUser(username, password);
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text("User created successfully."),
            ),
          );
          _usernameController.clear();
          _passwordController.clear();
          Navigator.pushReplacement(
            context,
            MaterialPageRoute(
              builder: (context) => LoginPage(userDb: userDb),
              settings: RouteSettings(arguments: userDb),
            ),
          );
        }
      }
    
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text("Create User"),
          ),
          body: Container(
            margin: EdgeInsets.all(20),
            child: Form(
              autovalidateMode: AutovalidateMode.onUserInteraction,
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  TextFormField(
                    decoration: InputDecoration(
                      labelText: 'USERNAME',
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                    controller: _usernameController,
                    validator: (value) {
                      if (value!.isEmpty) {
                        return "Username cannot be empty";
                      }
                      return null;
                    },
                  ),
                  SizedBox(
                    height: 30,
                  ),
                  TextFormField(
                    obscureText: true,
                    decoration: InputDecoration(
                      labelText: 'PASSWORD',
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(30),
                      ),
                    ),
                    controller: _passwordController,
                    validator: (value) {
                      if (value!.isEmpty) {
                        return "Password cannot be empty";
                      }
                      return null;
                    },
                  ),
                  SizedBox(
                    height: 40,
                  ),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(30),
                        ),
                      ),
                      onPressed: () {
                        if (_formKey.currentState!.validate()) {
                          _addUser(
                            _usernameController.text,
                            _passwordController.text,
                          );
                        }
                      },
                      child: Text("CREATE"),
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      }
    }
    ```
    
5. Create new dart file in `lib` directory named `login_page.dat`.
    
    And add the following code in that file.
    
    ```dart
    // ignore_for_file: prefer_const_constructors
    
    import 'package:flutter/material.dart';
    import 'package:user_auth_flutter_pract_09/user_db.dart';
    import 'user_home.dart';
    import 'create_user.dart';
    
    class LoginPage extends StatelessWidget {
      final _formKey = GlobalKey<FormState>();
      final username = TextEditingController();
      final password = TextEditingController();
    
      final UserDb userDb;
    
      LoginPage({Key? key, required this.userDb}) : super(key: key);
    
      bool authenticate() {
        return userDb.authenticate(username.text, password.text);
      }
    
      void handleSubmit(BuildContext context) {
        if (_formKey.currentState!.validate()) {
          if (authenticate()) {
            Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => UserHome(
                        username: username.text,
                      )),
            );
          } else {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text("Invalid credentials"),
              ),
            );
          }
        }
      }
    
      void handleCreateUser(BuildContext context) async {
        final result = await Navigator.push(
          context,
          MaterialPageRoute(
              builder: (context) => CreateUser(
                    userDb: UserDb(),
                  )),
        );
    
        if (result == true) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text("User created successfully"),
            ),
          );
        }
      }
    
      // LoginPage({super.key});
    
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text("User Authentication Pract 09"),
          ),
          body: Container(
            margin: EdgeInsets.all(20),
            child: Form(
              autovalidateMode: AutovalidateMode.onUserInteraction,
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  TextFormField(
                    decoration: InputDecoration(
                      labelText: 'USERNAME',
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(30)),
                    ),
                    controller: username,
                    validator: (value) {
                      if (value!.isEmpty) {
                        return "Username cannot be empty";
                      }
                      return null;
                    },
                  ),
                  SizedBox(
                    height: 30,
                  ),
                  TextFormField(
                    onEditingComplete: () {
                      handleSubmit(context);
                    },
                    obscureText: true,
                    decoration: InputDecoration(
                      labelText: 'PASSWORD',
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(30)),
                    ),
                    controller: password,
                    validator: (value) {
                      if (value!.isEmpty) {
                        return "Password cannot be empty";
                      }
                      return null;
                    },
                  ),
                  SizedBox(
                    height: 40,
                  ),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(30))),
                      onPressed: () {
                        handleSubmit(context);
                      },
                      child: Text("LOGIN"),
                    ),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                  SizedBox(
                    width: double.infinity,
                    child: OutlinedButton(
                      style: OutlinedButton.styleFrom(
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(30),
                        ),
                      ),
                      onPressed: () {
                        handleCreateUser(context);
                      },
                      child: Text("CREATE USER"),
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      }
    }
    ```
    
6. Create new dart file in `lib` directory named `user_home.dat`.
    
    And add the following code in that file.
    
    ```dart
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
    ```
    

**Running a project**

**Connect Phone**

make sure USB debugging is enabled in Developer option

**Run The app**

```bash
flutter run main.dart
```

## Screenshots

![Frame 1](https://user-images.githubusercontent.com/95087498/220708069-b0187150-0065-468c-b4f4-5446b0fc35c7.png)

