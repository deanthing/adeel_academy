import 'package:flutter/material.dart';
import 'package:adeel_academy/views/dashboard/starting_dash_view.dart';
import 'package:adeel_academy/widgets/centered_view/centered_view.dart';
import 'package:adeel_academy/util/authentication.dart';

class LoginView extends StatefulWidget {
  @override
  _LoginViewState createState() => _LoginViewState();
}

// This will be the page that opens whenever user presses the LogIn button
class _LoginViewState extends State<LoginView> {
  // controller for email textfield
  final emailController = TextEditingController();
  // controller for password textfield
  final passwordController = TextEditingController();

  bool validLogin = false;
  String loginMessage = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Log In"),
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
                    if (loginMessage != "") ...[
                      Text(
                        loginMessage,
                        style: TextStyle(color: Colors.red),
                      ),
                      Padding(
                        padding: const EdgeInsets.only(top: 30.0),
                      ),
                    ],
                    MaterialButton(
                      height: 40.0,
                      minWidth: 100.0,
                      color: Colors.orange,
                      splashColor: Colors.teal,
                      textColor: Colors.white,
                      child: Text("Login"),
                      onPressed: () async {
                        await signInWithEmailPassword(
                                emailController.text, passwordController.text)
                            .then((result) {
                          setState(() {
                            validLogin = true;
                          });
                          print(result);
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => StartingDashView()),
                          );
                        }).catchError((error) {
                          setState(() {
                            loginMessage = "Error logging in";
                          });
                          print('Registration Error: $error');
                        });
                      },
                    )
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
