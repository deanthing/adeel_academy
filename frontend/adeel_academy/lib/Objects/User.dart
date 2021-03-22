class User {
  // Instance Variables
  String userID;
  String name;
  List<String> courseID = new List();
  bool isOnline;
  bool isTeacher;

  /**
   * Getters and Setters for the Following Variables Above
   */

  String getUserID() {
    return this.userID;
  }

  void setUserID(String newID) {
    this.userID = newID;
  }

  String getName() {
    return name;
  }

  void setName(String newName) {
    this.name = newName;
  }

  List<String> getCourseID() {
    return courseID;
  }

  void setCourseID(List<String> newCourseID) {
    this.courseID = newCourseID;
  }

  void addCourse(String course) {
    courseID.add(course);
  }

  void addAllCourses(List<String> allCourses) {
    courseID.addAll(allCourses);
  }

  void removeCourse(String course) {
    courseID.remove(course);
  }

  void removeAllCourses(List<String> allCourses) {
    courseID.remove(allCourses);
  }

  bool getOnline(bool userStatus) {
    if (userStatus == true) {
      return true;
    }
    return false;
  }

  void setOnline(bool userStatus) {
    this.isOnline = userStatus;
  }

  bool isATeacher(bool user) {
    if (user == true) {
      isTeacher = true;
      return true;
    }
    return false;
  }
}
