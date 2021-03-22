import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:adeel_academy/Objects/Course.dart';
import 'package:adeel_academy/views/dashboard/starting_dash_view.dart';
import 'package:adeel_academy/views/home/home_view.dart';
import 'package:adeel_academy/widgets/centered_view/centered_view.dart';
import 'package:adeel_academy/widgets/course/course_announcements.dart';
import 'package:adeel_academy/widgets/course/course_home.dart';
import 'package:adeel_academy/widgets/course/course_modules.dart';
import 'package:adeel_academy/widgets/details/details.dart';
import 'package:adeel_academy/widgets/log_in/log_in.dart';
import 'package:adeel_academy/widgets/navigation/nav_drawer.dart';

class CoursePage extends StatefulWidget {
  final Course course;
  const CoursePage(this.course);
  @override
  _CoursePageState createState() => _CoursePageState();
}

class _CoursePageState extends State<CoursePage> {
  // Generating a long list to fill the ListView
  // final List<Map> data = List.generate(100,
  //     (index) => {'id': index, 'name': 'Item $index', 'isSelected': false});

  Widget currPage;
  bool started = false;

  @override
  Widget build(BuildContext context) {
    if (!started) {
      currPage = CourseHome(widget.course);
      started = true;
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
            child: Row(children: [
          Column(
            children: [
              TextButton(
                  onPressed: () {
                    setState(() {
                      currPage = CourseHome(widget.course);
                    });
                  },
                  child: Text("Home")),
              TextButton(
                  onPressed: () {
                    setState(() {
                      currPage = CourseAnnouncements();
                    });
                  },
                  child: Text("Announcements")),
              TextButton(
                  onPressed: () {
                    //currPage = HomeView();
                    setState(() {
                      currPage = CourseModules();
                    });
                  },
                  child: Text("Modules")),
            ],
            // body: CenteredView(
            //   child: Column(
            //     children: courseWidgets
            //   ),

            // ),
          ),
          // Column(
          //   children: [Text('1')],
          // )
          currPage,
        ])));
    // Column(
    //   children: [
    //     TextButton(
    //       onPressed: () {
    //         print("pressed");
    //       },
    //     child: Text("ok")
    //     )
    //   ],
    //   children: [InkWell(
    //     child: TextButt("Home"),
    //     onTap: () {
    //     print("tapped on container");
    //     },
    //  ),]
    //  InkWell(
    //     child: Text("Assignments"),
    //     onTap: () {
    //     print("tapped on container");
    //     },
    //  ),
    //]
    //);
    // return Scaffold(
    //     appBar: AppBar(
    //       title: Text('Kindacode.com'),
    //     ),
    //     body: SafeArea(
    //         child: ListView.builder(
    //       itemCount: data.length,
    //       itemBuilder: (BuildContext ctx, index) {
    //         return Card(
    //             margin: EdgeInsets.all(10),
    //             shape:
    //                 RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),

    //             // The color depends on this is selected or not
    //             color: data[index]['isSelected'] == true ? Colors.amber : Colors.white,
    //             child: ListTile(
    //               onTap: (){
    //                 // if this item isn't selected yet, "isSelected": false -> true
    //                 // If this item already is selected: "isSelected": true -> false
    //                 setState(() {
    //                   data[index]['isSelected'] = !data[index]['isSelected'];
    //                 });
    //               },
    //               leading: CircleAvatar(
    //                   backgroundColor: Colors.blue,
    //                   child: Text(data[index]['id'].toString())),
    //               title: Text(data[index]['name']),
    //             ));
    //       },
    //     )));
  }
}
