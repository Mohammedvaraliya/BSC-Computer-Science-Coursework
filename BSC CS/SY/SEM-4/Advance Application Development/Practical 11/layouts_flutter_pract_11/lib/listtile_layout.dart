import 'package:flutter/material.dart';

class ListTileLayout extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('ListTile Layout Demo'),
      ),
      body: ListView(
        children: [
          ListTile(
            leading: Icon(Icons.person),
            title: Text('John Doe'),
            subtitle: Text('johndoe@example.com'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              // Navigate to user profile page
            },
          ),
          ListTile(
            leading: Icon(Icons.person),
            title: Text('Jane Doe'),
            subtitle: Text('janedoe@example.com'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              // Navigate to user profile page
            },
          ),
          ListTile(
            leading: Icon(Icons.person),
            title: Text('Bob Smith'),
            subtitle: Text('bobsmith@example.com'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              // Navigate to user profile page
            },
          ),
        ],
      ),
    );
  }
}
