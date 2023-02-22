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
}
