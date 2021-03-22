import 'package:flutter/material.dart';
import 'package:adeel_academy/Objects/Course.dart';
import 'package:adeel_academy/views/home/home_view.dart';

void main() {
  print("started");

  // Course testing:
  Course course1 =
      Course("1", "course 1", "this is test course 1", ["st1"], ["te1"], null);
  Course course2 =
      Course("2", "course 2", "this is test course 2", ["st2"], ["te2"], null);

  List<Course> courses = [course1, course2];

  //server.start();
  runApp(new MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Adeel Academy',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.red,
        visualDensity: VisualDensity.adaptivePlatformDensity,
        scaffoldBackgroundColor: Colors.white,
      ),
      home: HomeView(),
      //home: StartingDashView(),
    );
  }
}
