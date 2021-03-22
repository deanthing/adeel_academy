import 'Module.dart';

class Course {
  // Instance Variables
  String courseID;
  String name;
  String description;
  List<String> studentIDs = new List<String>();
  List<String> teacherIDs = new List<String>();
  List<Module> modules = new List<Module>();

  Course(this.courseID, this.name, this.description, this.studentIDs, this.teacherIDs, this.modules);



  /**
   * Getters and Setters for the Following Variables Above
   */

  String getCourseID() {
    return courseID;
  }

  void setCourseID(String newCourse) {
    this.courseID = newCourse;
  }

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

  List<String> getStudentIDs() {
    return studentIDs;
  }

  void setStudentIDs(List<String> newStudentIDs) {
    this.studentIDs = newStudentIDs;
  }

  void addStudentID(String studentID) {
    studentIDs.add(studentID);
  }

  void addStudentIDs(List<String> studentIDs) {
    studentIDs.addAll(studentIDs);
  }

  void removeStudentID(String studentID) {
    studentIDs.remove(studentID);
  }

  void removeStudentIDs(List<String> studentIDs) {
    studentIDs.remove(studentIDs);
  }

  List<String> getTeacherIDs() {
    return teacherIDs;
  }

  void setTeacherIDs(List<String> newteacherIDs) {
    this.teacherIDs = newteacherIDs;
  }

  void addTeacherID(String teacherID) {
    teacherIDs.add(teacherID);
  }

  void addTeacherIDs(List<String> teacherIDs) {
    teacherIDs.addAll(teacherIDs);
  }

  void removeTeacherID(String teacherID) {
    teacherIDs.remove(teacherID);
  }

  void removeTeacherIDs(List<String> teacherIDs) {
    teacherIDs.remove(teacherIDs);
  }

  List<Module> getModules() {
    return modules;
  }

  void setModules(List<Module> newModules) {
    this.modules = newModules;
  }

  void addModule(Module newModule) {
    modules.add(newModule);
  }

  void removeModule(Module newModule) {
    modules.remove(newModule);
  }

  void addModules(List<Module> newModules) {
    modules.addAll(newModules);
  }

  void removeModules(List<Module> newModules) {
    modules.remove(newModules);
  }
}
