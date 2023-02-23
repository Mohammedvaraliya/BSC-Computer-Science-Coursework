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
