import 'package:flutter/material.dart';
import 'package:adeel_academy/Objects/Course.dart';

class CourseHome extends StatelessWidget {
  //const CourseHome({Key key}) : super(key: key);
  final Course course;
  const CourseHome(this.course);

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
              course.getName(),
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
            course.getDescription(),
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
