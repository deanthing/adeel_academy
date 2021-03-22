class StudentAssignment {
  // Instance Variables
  String name;
  String description;
  int timeStamp;
  bool turnedIn;
  dynamic grade;

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

  bool getTurnedIn() {
    return turnedIn;
  }

  void setTurnedIn(bool turnedIn) {
    this.turnedIn = turnedIn;
  }

  dynamic getGrade() {
    return grade;
  }

  void setGrade(dynamic grade) {
    this.grade = grade;
  }
}
