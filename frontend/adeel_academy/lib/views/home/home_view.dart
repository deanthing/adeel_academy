import 'package:adeel_academy/util/data.dart';
import 'package:flutter/material.dart';
import 'package:adeel_academy/widgets/centered_view/centered_view.dart';
import 'package:adeel_academy/widgets/details/details.dart';
import 'package:adeel_academy/widgets/log_in/log_in.dart';
import 'package:adeel_academy/widgets/navigation/nav_drawer.dart';

// This is the home view for our web page.
class HomeView extends StatelessWidget {
  testGetListData() {
    getList("courses");
  }

  testGetIndividualData() {
    getIndividual("courses", 1);
  }

  testPutData() {
    final Map<String, String> data = {
      "name": "csci900",
      "description": "coding classs",
    };

    // send data to /logins with data
    putData("courses", data);
  }

  const HomeView({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Image.asset('assets/images/logo.png'),
        toolbarHeight: 80,
        backgroundColor: Colors.red[700],
      ),
      drawer: NavDrawer(),
      body: CenteredView(
        child: Column(
          children: <Widget>[
            //NavigationBar(),
            Expanded(
              child: Row(
                children: <Widget>[
                  Details(),
                  Expanded(
                    child: Center(
                      child: LogIn('Log In', 'Sign Up'),
                    ),
                  ),
                ],
              ),
            ),
            TextButton(
                onPressed: () => testGetListData(),
                child:
                    Text("test get list of Data: read flutter print output")),
            TextButton(
                onPressed: () => testPutData(),
                child: Text("test push Data: read flutter print output")),
            TextButton(
                onPressed: () => testGetIndividualData(),
                child: Text(
                    "test get piece of Data with id of 1: read flutter print output")),
          ],
        ),
      ),
    );
  }
}
