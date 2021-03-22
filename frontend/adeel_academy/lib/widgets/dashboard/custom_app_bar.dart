import 'package:flutter/material.dart';
import 'package:adeel_academy/widgets/dashboard/widgets.dart';

class CustomAppBar extends StatelessWidget {
  final double scrollOffset;

  const CustomAppBar({
    Key key,
    this.scrollOffset = 0.0,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(
        vertical: 10.0,
        horizontal: 24.0,
      ),
      color:
          Colors.black.withOpacity((scrollOffset / 350).clamp(0, 1).toDouble()),
      child: Responsive(
        mobile: _CustomAppBarMobile(),
        desktop: _CustomAppBarDesktop(),
      ),
    );
  }
}

class _CustomAppBarMobile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Row(
        children: [
          // Image.asset(Assets.nostra_logo),
          // const SizedBox(width: 12.0),
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                // _AppBarButton(
                //   title: 'Key Metrics',
                //   onTap: () => print('Key Metrics'),
                // ),
                // _AppBarButton(
                //   title: 'Recommended',
                //   onTap: () => print('Recommended'),
                // ),
                // _AppBarButton(
                //   title: 'Highlights',
                //   onTap: () => print('Highlights'),
                // ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _CustomAppBarDesktop extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Row(
        children: [
          Image.asset(null),
          const SizedBox(width: 12.0),
          Expanded(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _AppBarButton(
                  title: 'Home',
                  onTap: () => print('Home'),
                ),
                _AppBarButton(
                  title: 'Search Page',
                  onTap: () => print('Search Page'),
                ),
                _AppBarButton(
                  title: 'Highlights',
                  onTap: () => print('Highlights'),
                ),
                _AppBarButton(
                  title: 'Recommended',
                  onTap: () => print('Recommended'),
                ),
                _AppBarButton(
                  title: 'Lowlights',
                  onTap: () => print('Lowlights'),
                ),
              ],
            ),
          ),
          // const Spacer(),
          // Expanded(
          //   child: Row(
          //     mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          //     children: [
          //       IconButton(
          //         padding: EdgeInsets.zero,
          //         icon: Icon(Icons.search),
          //         iconSize: 28.0,
          //         color: Colors.white,
          //         onPressed: () => print('Search'),
          //       ),
          //       _AppBarButton(
          //         title: 'Converted Home',
          //         onTap: () => print('Home Page'),
          //       ),
          //       _AppBarButton(
          //         title: 'Recommended',
          //         onTap: () => print('Recommended'),
          //       ),
          //       IconButton(
          //         padding: EdgeInsets.zero,
          //         icon: Icon(Icons.card_giftcard),
          //         iconSize: 28.0,
          //         color: Colors.white,
          //         onPressed: () => print('Ideal Path'),
          //       ),
          //       IconButton(
          //         padding: EdgeInsets.zero,
          //         icon: Icon(Icons.notifications),
          //         iconSize: 28.0,
          //         color: Colors.white,
          //         onPressed: () => print(''),
          //       ),
          //     ],
          //   ),
          // ),
        ],
      ),
    );
  }
}

class _AppBarButton extends StatelessWidget {
  final String title;
  final Function onTap;

  const _AppBarButton({
    Key key,
    @required this.title,
    @required this.onTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Text(
        title,
        style: const TextStyle(
          color: Colors.white,
          fontSize: 16.0,
          fontWeight: FontWeight.w600,
        ),
      ),
    );
  }
}
