import 'package:flutter/material.dart';
import 'package:adeel_academy/views/login/login_view.dart';
import 'package:adeel_academy/views/login/signup_view.dart';

class LogIn extends StatelessWidget {
  final String text1;
  final String text2;
  LogIn(this.text1, this.text2);

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        //Log In
        GestureDetector(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => LoginView()),
            );
          },
          child: Container(
            padding: const EdgeInsets.symmetric(
              horizontal: 60,
              vertical: 15,
            ),
            child: TextButton(
                child: Text(
                  text1,
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w800,
                    color: Colors.white,
                  ),
                ),
                onPressed: () {
                  // take user to LogIn view when this button is pressed
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => LoginView()),
                  );
                }),
            decoration: BoxDecoration(
              color: Colors.red[900],
              borderRadius: BorderRadius.circular(5),
            ),
          ),
        ),
        // Spacing:
        SizedBox(height: 10),
        // Sign up:
        Container(
          padding: const EdgeInsets.symmetric(
            horizontal: 60,
            vertical: 15,
          ),
          child: TextButton(
              child: Text(
                text2,
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.w800,
                  color: Colors.red,
                ),
              ),
              onPressed: () {
                // take user to LogIn view when this button is pressed
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => SignupView()),
                );
              }),
        ),
      ],
    );
  }
}
