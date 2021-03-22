import 'CourseAssignment.dart';
import 'Document.dart';

class Module {
  // Instance Variables
  String moduleID;
  String name;
  String description;
  List<Document> documents = new List<Document>();
  List<CourseAssignment> assignment = new List<CourseAssignment>();

  /**
   * Getters and Setters for the Following Variables Above
   */

  String getModuleID() {
    return moduleID;
  }

  void setModuleID(String newModID) {
    this.moduleID = newModID;
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

  List<Document> getDocuments() {
    return documents;
  }

  void setDocuments(List<Document> newDocuments) {
    this.documents = newDocuments;
  }

  void addDocument(Document addDocument) {
    documents.add(addDocument);
  }

  void addDocuments(List<Document> addDocuments) {
    documents.addAll(addDocuments);
  }

  void removeDocument(Document removeDoc) {
    documents.remove(removeDoc);
  }

  void removeDocuments(List<Document> removeDocs) {
    documents.remove(removeDocs);
  }
}
