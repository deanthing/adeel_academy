import 'package:flutter/material.dart';
import 'package:adeel_academy/Objects/Course.dart';
import 'package:adeel_academy/widgets/centered_view/centered_view.dart';
import 'package:adeel_academy/widgets/dashboard/dash_course.dart';
import 'package:adeel_academy/widgets/details/details.dart';
import 'package:adeel_academy/widgets/log_in/log_in.dart';
import 'package:adeel_academy/widgets/navigation/nav_drawer.dart';

// This is the home view for our web page.
class StartingDashView extends StatelessWidget {
  //final List<Course> courses;
  const StartingDashView({Key key}) : super(key: key);

  //final List<Widget> courseWidgets = [];

  @override
  Widget build(BuildContext context) {
    // Course testing:
    Course course1 = Course(
        "1",
        "Biology 1",
        "Welcome to Biology 1, this is our course description....",
        ["st1"],
        ["te1"],
        null);
    Course course2 = Course(
        "2",
        "Physics 2",
        "Welcome to Physics 2, where we learn about physics 2",
        ["st2"],
        ["te2"],
        null);
    Course course3 = Course(
        "3",
        "Physics 3",
        "Welcome to Physics 3, where we learn about physics 3",
        ["st3"],
        ["te3"],
        null);

    List<Course> courses = [course1, course2, course3];
    List<Widget> courseWidgets = [];
    for (Course course in courses) {
      DashCourse dashWidget = DashCourse(course);
      courseWidgets.add(dashWidget);
    }
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Image.asset('assets/images/logo.png'),
        toolbarHeight: 80,
        backgroundColor: Colors.red[700],
      ),
      drawer: NavDrawer(),
      body: CenteredView(
        child: Column(children: courseWidgets),
      ),
    );
  }
}
