class Message {
  // Instance Variables
  String userID;
  String content;
  int timestamp;

  /**
   * Getters and Setters for the Following Variables Above
   */

  String getUserID() {
    return userID;
  }

  void setUserID(String uID) {
    this.userID = uID;
  }

  String getContent() {
    return content;
  }

  void setContent(String content) {
    this.content = content;
  }

  int getTimestamp() {
    return timestamp;
  }

  void setTimestamp(int time) {
    this.timestamp = time;
  }
}
