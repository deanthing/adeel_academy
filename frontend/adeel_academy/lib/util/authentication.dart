import 'package:shared_preferences/shared_preferences.dart';
import 'package:adeel_academy/util/data.dart';

// registers a new users given email and pass
Future<String> registerWithEmailPassword(String email, String password) async {
  return null;
}

// signs in a user after an account has already been created
Future<String> signInWithEmailPassword(String email, String password) async {
  // query db for email password

  // set as logged in
  SharedPreferences prefs = await SharedPreferences.getInstance();
  prefs?.setBool("isLoggedIn", true);

  int userId = 0;
  prefs?.setInt("userId", userId);

  return null;
}

//  signs a user out
Future<String> signOut() async {}
