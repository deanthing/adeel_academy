import 'package:flutter/material.dart';

class CourseModules extends StatelessWidget {
  const CourseModules({Key key}) : super(key: key);

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
              'Course Modules:',
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
            'This will be the course modules view.',
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
