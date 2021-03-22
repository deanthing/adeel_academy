import 'package:flutter/material.dart';

class Details extends StatelessWidget {
  const Details({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 600,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Center(
            child: Text(
              'Adeel Academy:\nA learning platform for all subjects',
              style: TextStyle(
                fontWeight: FontWeight.w800,
                height: 0.9,
                fontSize: 60,
              ),
            ),
          ),
          SizedBox(
            height: 30,
          ),
          Text(
            'Adeel Academy is a learning management platform where you can access public lectures and quizzes, as well as track your education progress. Teachers can also create private groups to host their online lectures and assignments.',
            style: TextStyle(
              fontSize: 21,
              height: 1.7,
            ),
          ),
        ],
      ),
    );
  }
}
