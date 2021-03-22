import 'package:flutter/material.dart';

/* 
This class is the navigation header that 
an be placed at the top of any screen.
*/
class NavigationBar extends StatelessWidget {
  const NavigationBar({Key key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(color: Colors.red[700]),
      height: 100,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: <Widget>[
          SizedBox(
            height: 80,
            width: 150,
            child: Image.asset('assets/logo.png'),
          ),
          Row(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              // Here we can place navigation items using _NavBarItem()s
              // _NavBarItem('Info'),
              // SizedBox(width: 60),
              // _NavBarItem('Help')
            ],
          ),
        ],
      ),
    );
  }
}

class _NavBarItem extends StatelessWidget {
  final String title;
  const _NavBarItem(this.title);

  @override
  Widget build(BuildContext context) {
    return Text(title,
        style: TextStyle(
          fontSize: 18,
          color: Colors.white,
        ));
  }
}
