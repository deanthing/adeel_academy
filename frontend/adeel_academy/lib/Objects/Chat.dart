import 'Message.dart';

class Chat {
  // Instance Variables
  List<Message> messages = new List<Message>();
  List<String> userIDs = new List<String>();


  /**
   * Getters and Setters for the Following Variables Above
   */

  List<Message> getMessages() {
    return messages;
  }

  void setMessages(List<Message> newMessages) {
    this.messages = newMessages;
  }

  void addMessage(Message newMessage) {
    messages.add(newMessage);
  }

  void addMessages(List<Message> newMessages) {
    messages.addAll(newMessages);
  }

  void removeMessage(Message removeMessage) {
    messages.remove(removeMessage);
  }

  void removeMessages(Message removeMessages) {
    messages.remove(removeMessages);
  }

  // This is a Helper Method to Get a Single Message
  void processMessage(Message message) {
    if (messages.contains(message)) {
      print(message);
    }
  }

  void getMessage(Message message) {
    messages.forEach((element) => processMessage(message));
  }

  List<String> getUserIDs() {
    return userIDs;
  }

  void setUserID(List<String> uIDs) {
    this.userIDs = uIDs;
  }

  // This is a Helper Method to Get a Single User ID
  void processID(String uID) {
    if (userIDs.contains(uID)) {
      print(uID);
    }
  }

  void getUserID(String uID) {
    messages.forEach((element) => processID(uID));
  }
}
