class CourseAssignment {
  // Instance Variables
  String name;
  String description;
  int timeStamp;
  String courseID;

  /**
   * Getters and Setters for the Following Variables Above
   */

  String getName() {
    return name;
  }

  void setName(String newName) {
    this.name = newName;
  }

  String getDescription() {
    return description;
  }

  void setDescription(String newDescription) {
    this.description = newDescription;
  }

  int getTimeStamp() {
    return timeStamp;
  }

  void setTimeStamp(int time) {
    this.timeStamp = time;
  }

  String getCourseID() {
    return courseID;
  }

  void setCourseID(String course) {
    this.courseID = course;
  }
}
