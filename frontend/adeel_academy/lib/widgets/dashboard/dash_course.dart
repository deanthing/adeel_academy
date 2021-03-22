import 'package:flutter/material.dart';
import 'package:adeel_academy/Objects/Course.dart';
import 'package:adeel_academy/views/course/course_view.dart';

/*
This widget centers its child by creating space between its 
child and its parent.
*/
class DashCourse extends StatelessWidget {
  // final Widget child;
  final Course course;
  //const DashCourse({Key key, this.course}) : super(key: key);
  DashCourse(this.course);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Card(
        child: InkWell(
          splashColor: Colors.blue.withAlpha(30),
          onTap: () {
            Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => CoursePage(course),
                ));
          },
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              ListTile(
                  leading: Icon(Icons.class_),
                  title: Text(course.getName()),
                  subtitle: Text(course.getDescription())),
              // Row(
              //   mainAxisAlignment: MainAxisAlignment.end,
              //   children: <Widget>[
              //     TextButton(
              //       child: const Text('BUY TICKETS'),
              //       onPressed: () {/* ... */},
              //     ),
              //     const SizedBox(width: 8),
              //     TextButton(
              //       child: const Text('LISTEN'),
              //       onPressed: () {/* ... */},
              //     ),
              //     const SizedBox(width: 8),
              //   ],
              // ),
            ],
          ),
        ),
      ),
    );
  }
//   Widget build(BuildContext context) {
//     return Container(
//       padding: const EdgeInsets.symmetric(horizontal: 70, vertical: 60),
//       alignment: Alignment.topCenter,
//       child: ConstrainedBox(
//         constraints: BoxConstraints(maxWidth: 1200),
//         child: child,
//       ),
//     );
//   }
// }
}
