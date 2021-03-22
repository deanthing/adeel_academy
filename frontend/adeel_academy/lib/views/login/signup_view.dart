import 'package:flutter/material.dart';
import 'package:adeel_academy/views/dashboard/starting_dash_view.dart';
import 'package:adeel_academy/widgets/centered_view/centered_view.dart';
import 'package:adeel_academy/util/authentication.dart';

class SignupView extends StatefulWidget {
  @override
  _SignupViewState createState() => _SignupViewState();
}

// This will be the page that opens whenever user presses the LogIn button
class _SignupViewState extends State<SignupView> {
  // controller for email textfield
  final emailController = TextEditingController();
  // controller for password textfield
  final passwordController = TextEditingController();

  String signupErrorMessage = "";

  // email validator
  String _validateEmail(String value) {
    value = value.trim();

    if (emailController.text != null) {
      if (value.isEmpty) {
        return 'Email can\'t be empty';
      } else if (!value.contains(RegExp(
          r"^[a-zA-Z0-9.a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9]+\.[a-zA-Z]+"))) {
        return 'Enter a correct email address';
      }
    }
    return null;
  }

  // password validator
  String _validatePassword(String value) {
    value = value.trim();

    if (passwordController.text != null) {
      if (value.isEmpty) {
        return 'Password cannot be empty';
      }
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Sign Up"),
        backgroundColor: Colors.red[700],
      ),
      body: CenteredView(
        child: new Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(padding: EdgeInsets.fromLTRB(0.0, 60.0, 0.0, 0.0)),
            Image.asset('assets/images/logo.png'),
            new Container(
              //padding: const EdgeInsets.fromLTRB(0.0, 20.0, 0.0, 0.0),
              child: new Form(
                autovalidate: true,
                child: new Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: <Widget>[
                    TextFormField(
                      decoration: new InputDecoration(
                          labelText: "Email:", fillColor: Colors.white),
                      keyboardType: TextInputType.emailAddress,
                      controller:
                          emailController, // add controller to textfield
                    ),
                    TextFormField(
                      decoration: new InputDecoration(
                        labelText: "Password:",
                      ),
                      obscureText: true,
                      keyboardType: TextInputType.text,
                      controller:
                          passwordController, // add controller to textfield
                    ),
                    Padding(
                      padding: const EdgeInsets.only(top: 30.0),
                    ),
                    if (signupErrorMessage != "") ...[
                      Text(
                        signupErrorMessage,
                        style: TextStyle(color: Colors.red),
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 30.0),
                      ),
                    ],
                    Text(
                        "Must be a valid email and password must be at least 6 characters."),
                    Padding(
                      padding: const EdgeInsets.only(top: 30.0),
                    ),
                    MaterialButton(
                        height: 40.0,
                        minWidth: 100.0,
                        color: Colors.orange,
                        splashColor: Colors.teal,
                        textColor: Colors.white,
                        child: Text("Sign up"),
                        onPressed: () async {
                          print("sign up pressed");
                          // validate email and password and then register
                          if (_validateEmail(emailController.text) == null &&
                              _validatePassword(passwordController.text) ==
                                  null) {
                            await registerWithEmailPassword(
                                    emailController.text,
                                    passwordController.text)
                                .then((result) {
                              print(result);
                              Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (context) => StartingDashView()),
                              );
                            }).catchError((error) {
                              setState(() {
                                signupErrorMessage =
                                    "Error creating your account.";
                              });
                              print('Registration Error: $error');
                            });
                          } else {
                            setState(() {
                              signupErrorMessage =
                                  "Error validating your information.";
                            });
                          }
                        })
                  ],
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
