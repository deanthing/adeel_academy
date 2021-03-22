from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from marshmallow import fields
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
CORS(app=app)


'''
    Completed: 
        ********* TEACHER *********HAYDEN
            String: userId (firebase)
            String: name
            String: email
            String[]: courseId
            boolean: connected (on/offline)
                    
        ******** ADMIN ********HAYDEN
            String: userId (firebase)
            String: name
            String: email
                    
        ****** MODULE *****HAYDEN
            String: moduleId
            String: name
            String: description
            Document[]: documents
            Course_Assignment[]: assignments
                    
        ****** DOCUMENT ******HAYDEN
            String: documentId
            Enum type: (file, text, URL, media)
                    
        ********* CHAT *********HAYDEN
            Message[]: messages
            String[]: userIds (chat partners)
                    
        ******* MESSAGE *******HAYDEN
            String: userId (sender)
            String: content
            int: timestamp
                    
        ***** ANNOUNCEMENT *****HAYDEN
            String: name
            String: description
            String: courseId
                    
        ** COURSE_ASSIGNMENT **HAYDEN
            String: name
            String: description
            int: dueTime
            String: courseId
                    
        ** STUDENT_ASSIGNMENT **HAYDEN
            String: name
            String: description
            int: dueTime
            boolean: turnedIn
            float: grade
    Complete:
        ********* STUDENT ********* Dean
            String: userId (firebase)
            String: name
            String: email
            String[]: courseId
            boolean: connected (on/offline)
        ******** COURSE ******** Dean
            String: courseId 
            String: name
            String: description
            String[]: userIds (teachers)
            String[]: userIds (students)
            Module[]: modules
            
         ******** StudentCourses ********HAYDEN
            Int: unique takes id
            Int: StudentId (ref student id)
            Int: CourseId (ref teacher id)

        ******** TeacherCourses ********HAYDEN
            Int: teacherCourseId
            Int: courseId
            Int: teacherId
'''

class Student(db.Model):
    studentId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(255))
    connected = db.Column(db.Integer)
    loginId = db.Column(db.Integer, db.ForeignKey('login.loginId'))

    def __repr__(self):
        return "studentId: {}, Name: {}, email: {}, connected: {}, loginId: {}".format(self.courseId, self.name, self.email, self.connected, self.loginId)


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("studentId", "name", "email", "connected", "loginId")


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


class StudentListResource(Resource):
    def get(self):
        students = Student.query.all()
        return students_schema.dump(students)

    def post(self):
        new_student = Student(
            name=request.json['name'],
            email=request.json['email'],
            connected=request.json['connected'],
            loginId=request.json['loginId']
        )
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student)


class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get_or_404(student_id)
        return student_schema.dump(student)

    def patch(self, student_id):
        student = Student.query.get_or_404(student_id)

        if 'studetnId' in request.json:
            student.variable = request.json['variable']
        if 'name' in request.json:
            student.name = request.json['name']
        if 'email' in request.json:
            student.email = request.json['email']
        if 'connected' in request.json:
            student.connected = request.json['connected']
        if 'loginId' in request.json:
            student.loginId = request.json['loginId']

        db.session.commit()
        return student_schema.dump(student)

    def delete(self, student_id):
        student = Student.query.get_or_404(student_id)
        db.session.delete(student)
        db.session.commit()
        return '', 204


api.add_resource(StudentListResource, '/students')
api.add_resource(StudentResource, '/students/<int:student_id>')

'''
curl http://localhost:5000/students \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"cs OOP", "email":"deanallen@gmail.com", "connected": "1", "loginId", "123"}'
'''


# StudentCourses
class StudentCourses(db.Model):
    __tablename__ = 'studentcourse'
    studentCourseId = db.Column(db.Integer, primary_key=True)
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId'))
    studentId= db.Column(db.Integer, db.ForeignKey('student.studentId'))

    def __repr__(self):
        return "studentCourseId: {}, courseId: {}, studentId: {}".format(self.studentCourseId, self.courseId, self.studentId)


class StudentCoursesSchema(ma.Schema):
    class Meta:
        fields = ("studentCourseId", "courseId", "studentId")

studentCourses_schema = StudentCoursesSchema(many=True)

studentCourse_schema = StudentCoursesSchema()

class StudentCourseListResource(Resource):
    def get(self):
        student_courses = StudentCourses.query.all()
        return studentCourses_schema.dump(student_courses)

    def post(self):
        new_student_course = StudentCourses(
            courseId=request.json['courseId'],
            studentId=request.json['studentId'],
        )
        db.session.add(new_student_course)
        db.session.commit()
        return studentCourse_schema.dump(new_student_course)

class StudentCourseResource(Resource):
    def get(self, studentCourseId):
        student_course = StudentCourses.query.get_or_404(studentCourseId)
        return studentCourse_schema.dump(student_course)

    def patch(self, studentCourseId):
        course = Course.query.get_or_404(studentCourseId)
        if 'studentCourseId' in request.json:
            course.studentCourseId = request.json['studentCourseId']
        if 'studentId' in request.json:
            course.studentId = request.json['studentId']
        if 'courseId' in request.json:
            course.courseId = request.json['courseId']
        db.session.commit()
        return studentCourse_schema.dump(course)

    def delete(self, studentCourseId):
        student_course = Course.query.get_or_404(studentCourseId)
        db.session.delete(student_course)
        db.session.commit()
        return '', 204


api.add_resource(StudentCourseListResource, '/studentcourses')
api.add_resource(StudentCourseResource, '/studentcourses/<int:studentCourseId>')
'''
curl http://localhost:5000/studentcourses \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"studentId":"1", "courseId":"1"}'
'''

# TEACHER
class Teacher(db.Model):
    __tablename__ = 'teacher'
    teacherId = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    courses = db.relationship("TeacherCourses")
    connected = db.Column(db.Boolean)


    def __repr__(self):
        return "Teacher Id : {}, Name: {}, Email: {}, Courses: {}, Connected: {}".format(self.teacherId, self.name, self.email, self.courses, self.connected)


# Marshmellow Schema
class TeacherSchema(ma.Schema):
    class Meta:
        fields = ("teacherId", "name", "email", "courses", "connected")

# Schema for Multiple Teachers
teachers_schema = TeacherSchema(many = True)


# Schema for Individual Teachers
teacher_schema = TeacherSchema()

class TeacherListResource(Resource):
    def get(self):
        posts = Teacher.query.all()
        return teacher_schema.dump(posts)

    def post(self):
        connection = False

        if request.json['connected'] == "True" or request.json['connected'] == 'true':
            connection = True
        
        newTeacher = Teacher(
            name = request.json['name'],
            email = request.json['email'],
            connected = connection
        )

        db.session.add(newTeacher)
        db.session.commit()
        return teacher_schema.dump(newTeacher)


class TeacherResource(Resource):

    def get(self, teacherId):

        teacher = Teacher.query.get_or_404(teacherId)
        return teacher_schema.dump(teacher)

    def patch(self, teacherId):

        teacher = Teacher.query.get_or_404(teacherId)

        if 'teacherId' in request.json:
            teacher.teacherId = request.json['teacherId']

        if 'name' in request.json:
            teacher.name = request.json['name']

        if 'email' in request.json:
            teacher.email = request.json['email']

        if 'connected' in request.json and (request.json['connected'] == 'True' or request.json['connected'] == 'true'):
            teacher.connected = True

        db.session.commit()
        return teacher_schema.dump(teacher)

    
    def delete(self, teacherId):

        teacher = teacherId.query.get_or_404(teacherId)
        db.session.delete(teacher)
        db.session.commit()
        return '', 204
    
# Registering the Endpoints 
api.add_resource(TeacherListResource, '/teachers')
api.add_resource(TeacherResource, '/teachers/<int:teacherId>')




# TeacherCourses
class TeacherCourses(db.Model):
    __tablename__ = 'teachercourse'
    teacherCourseId = db.Column(db.Integer, primary_key=True)
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId'))
    teacherId= db.Column(db.Integer, db.ForeignKey('teacher.teacherId'))

    def __repr__(self):
        return "teacherCourseId: {}, courseId: {}, teacherId: {}".format(self.teacherCourseId, self.courseId, self.teacherId)


class TeacherCoursesSchema(ma.Schema):
    class Meta:
        fields = ("teacherCourseId", "courseId", "teacherId")

teacherCourses_schema = TeacherCoursesSchema(many=True)

teacherCourse_schema = TeacherCoursesSchema()

class TeacherCourseListResource(Resource):
    def get(self):
        teacher_courses = TeacherCourses.query.all()
        return teacherCourses_schema.dump(teacher_courses)

    def post(self):
        new_teacher_course = TeacherCourses(
            courseId=request.json['courseId'],
            teacherId=request.json['teacherId'],
        )
        db.session.add(new_teacher_course)
        db.session.commit()
        return teacherCourse_schema.dump(new_teacher_course)

class TeacherCourseResource(Resource):
    def get(self, teacherCourseId):
        teacher_course = TeacherCourses.query.get_or_404(teacherCourseId)
        return teacherCourse_schema.dump(teacher_course)

    def patch(self, teacherCourseId):
        course = Course.query.get_or_404(teacherCourseId)
        if 'teacherCourseId' in request.json:
            course.teacherCourseId = request.json['teacherCourseId']
        if 'teacherId' in request.json:
            course.teacherId = request.json['teacherId']
        if 'courseId' in request.json:
            course.courseId = request.json['courseId']
        db.session.commit()
        return teacherCourse_schema.dump(course)

    def delete(self, teacherCourseId):
        teacher_course = Course.query.get_or_404(teacherCourseId)
        db.session.delete(teacher_course)
        db.session.commit()
        return '', 204


api.add_resource(TeacherCourseListResource, '/teachercourses')
api.add_resource(TeacherCourseResource, '/teachercourses/<int:teacherCourseId>')




# ADMIN
class Admin(db.Model):
    __tablename__ = 'admin'

    adminId = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __repr__(self):

        return "AdminId: {}, Name: {}, Email: {}".format(self.adminId, self.name, self.email)


# Marshmellow Schema
class AdminSchema(ma.Schema):

    class Meta:
        fields = ("adminId", "name", "email")


# Schema for Multiple Admin
admins_schema = AdminSchema(many = True)

# Schema for Single Admin
admin_schema = AdminSchema()


# The Endpoints for the List of Admins
class AdminListResource(Resource):

    def get(self):

        posts = Admin.query.all()
        return admins_schema.dump(posts)

    
    def post(self):
        newAdmin = Admin(
            name = request.json['name'],
            email = request.json['email']
        )

        db.session.add(newAdmin)
        db.session.commit()
        return admin_schema.dump(newAdmin)


# Endpoint for Each Admin, given their Admin Id
class AdminResource(Resource):

    def get(self, adminId):
        admin = Admin.query.get_or_404(adminId)
        return admin_schema.dump(admin)

    def patch(self, adminId):

        admin = Admin.query.get_or_404(adminId)

        if "adminId" in request.json['adminId']:
            admin.adminId = request.json['adminId']

        if 'name' in request.json['name']:
            admin.name = request.json['name']

        if 'email' in request.json['email']:
            admin.email = request.json['email']

        db.session.commit()
        return admin_schema.dump(admin)

    def delete(self, adminId):
        admin = Admin.query.get_or_404(adminId)
        db.session.delete(admin)
        db.session.commit()
        return '', 204


# Register the Endpoints 
api.add_resource(AdminListResource, '/admin')
api.add_resource(AdminResource, '/admin/<int:adminId>')


# MODULE
class Module(db.Model):

    __tablename__ = 'module'
    
    moduleId = db.Column(db.Integer, primary_key = 50)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId'))
    documents = db.relationship("Document")
    assignments = db.relationship("CourseAssignment")

    def __repr__(self):
        return "<Module Id: {}, Name: {}, Description: {}, CourseId: {}, docuemnts: {}, assignments: {}>".format(self.moduleId, self.name, self.description, self.courseId, self.documents, self.assignments)


# Marshmallow Schema
class ModuleSchema(ma.Schema):
    class Meta:
        fields = ("moduleId", "name", "description", "courseId")

# Schema for Multiple Modules
modules_schema = ModuleSchema(many = True)

# Schema for Single Module
module_schema = ModuleSchema()

# Endpoint for a List of Modules
class ModuleListResource(Resource):
    def get(self):

        posts = Module.query.all()
        return modules_schema.dump(posts)

    def post(self):
        newModule = Module(
            name = request.json['name'],
            description = request.json['description'],
            courseId = request.json['courseId'],
        )

        db.session.add(newModule)
        db.session.commit()
        return module_schema.dump(newModule)


# Endpoint for the Single Module, given the Module Id
class ModuleResource(Resource):
    def get(self, moduleId):
        module = Module.query.get_or_404(moduleId)
        return module_schema.dump(module)


    def patch(self, moduleId):
        module = Module.query.get_or_404(moduleId)

        if 'moduleId' in request.json['moduleId']:
            module.moduleId = request.json['moduleId']

        if 'name' in request.json['name']:
            module.name = request.json['name']

        if 'description' in request.json['description']:
            module.description = request.json['description']

        db.session.commit()
        return module_schema.dump(module)


    def delete(self, moduleId):
        module = Module.query.get_or_404(moduleId)
        db.session.delete(module)
        db.session.commit()
        return '', 204



# Register the Endpoints
api.add_resource(ModuleListResource, '/module')
api.add_resource(ModuleResource, '/module/<int:moduleId>')


# DOCUMENT
class Document(db.Model):

    __tablename__ = 'document'

    documentId = db.Column(db.Integer, primary_key = True)
    moduleId = db.Column(db.Integer, db.ForeignKey('module.moduleId'))
    studentAssignmentId = db.Column(db.Integer, db.ForeignKey('studentAssignment.assignmentId'))

    # Enum Type --> Not Sure How to Proceed on this Yet


    def __repr__(self):
        return "Document Id: {}".format(self.documentId)

# Marshmallow Schema
class DocumentSchema(ma.Schema):
    class Meta:
        fields = ("documentId", "document")

# Schema for Multiple Documents
documents_schema = DocumentSchema(many = True)

# Schema for Single Documents
document_schema = DocumentSchema()

# Endpoint for a List of Documents
class DocumentListResource(Resource):

    def get(self):
        posts = Document.query.all()
        return documents_schema.dump(posts)

    
    def post(self):
        newDocument = Document(
            moduleId = request.json['moduleId'],
            studentAssignmentId = request.json['studentAssignmentId'],
        )

        db.session.add(newDocument)
        db.session.commit()
        return document_schema.dump(newDocument)



# Endpoint for a Single Document

class DocumentResource(Resource):
    def get(self, documentId):
        document = Document.query.get_or_404(documentId)
        return document_schema.dump(document)

    
    def patch(self, documentId):
        document = Document.query.get_or_404(documentId)

        if 'documentId' in request.json['documentId']:
            document.documentId = request.json['documentId']

        db.session.commit()
        return document_schema.dump(document)


    def delete(self, documentId):
        document = Document.query.get_or_404(documentId)
        db.session.delete(document)
        db.session.commit()
        return '', 204


# Register the Endpoints
api.add_resource(DocumentListResource, '/documents')
api.add_resource(DocumentResource, '/documents/<int:documentId>')


# CHAT
class Chat(db.Model):
    __tablename__ = 'chat'
    chatId = db.Column(db.Integer, primary_key = True)
    chatName = db.Column(db.String(50))
    createrId = db.Column(db.Integer)
    inChat = db.relationship("InChat")

# Marshmallow Schema
class ChatSchema(ma.Schema):
    class Meta:
        fields = ("chatId", "chatName", "createrId", "inChat")

# Schema for Multiple Chats
chats_schema = ChatSchema(many = True)

# Schema for Single chat
chat_schema = ChatSchema()

# Endpoint for a List of chats
class ChatListResource(Resource):
    def get(self):
        chats = Chat.query.all()
        return chats_schema.dump(chats)

    
    def post(self):
        new_chat = Chat(
            chatName = request.json['chatName'],
            createrId = request.json['createrId'],
        )

        db.session.add(new_chat)
        db.session.commit()
        return chat_schema.dump(new_chat)

# Endpoint for a Single Document
class ChatResource(Resource):

    def get(self, chatId):
        chat = Chat.query.get_or_404(chatId)
        return chat_schema.dump(chat)

    
    def patch(self, chatId):
        chat = Chat.query.get_or_404(chatId)

        if 'chatId' in request.json['chatId']:
            chat.chatId = request.json['chatId']

        db.session.commit()
        return chat_schema.dump(chat)

    def delete(self, chatId):
        document = Chat.query.get_or_404(chatId)
        db.session.delete(document)
        db.session.commit()
        return '', 204

# Register the Endpoints
api.add_resource(ChatListResource, '/chats')
api.add_resource(ChatResource, '/chats/<int:chatId>')


# InChat
class InChat(db.Model):
    __tablename__ = 'inchat'
    inChatId = db.Column(db.Integer, primary_key = True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    teacherId = db.Column(db.Integer, db.ForeignKey('teacher.teacherId'))
    chatId = db.Column(db.Integer, db.ForeignKey('chat.chatId'))

# Marshmallow Schema
class InChatSchema(ma.Schema):
    class Meta:
        fields = ("inChatId", "studentId", "teacherId", "chatId")

# Schema for Multiple InChats
in_chats_schema = InChatSchema(many = True)

# Schema for Single chat
in_chat_schema = InChatSchema()

# Endpoint for a List of chats
class InChatListResource(Resource):
    def get(self):
        chats = InChat.query.all()
        return in_chats_schema.dump(chats)

    
    def post(self):
        new_in_chat = InChat(
            studentId = request.json['studentId'],
            teacherId = request.json['teacherId'],
            chatId = request.json['chatId']
        )

        db.session.add(new_in_chat)
        db.session.commit()
        return in_chat_schema.dump(new_in_chat)

# Endpoint for a Single Document
class InChatResource(Resource):
    def get(self, chatId):
        in_chat = InChat.query.get_or_404(chatId)
        return in_chat_schema.dump(in_chat)

    def patch(self, chatId):
        in_chat = InChat.query.get_or_404(chatId)

        if 'userId' in request.json['userId']:
            in_chat.userId = request.json['userId']

        if 'chatId' in request.json['chatId']:
            in_chat.chatId = request.json['chatId']

        db.session.commit()
        return chat_schema.dump(in_chat)

    def delete(self, chatId):
        inchat = InChat.query.get_or_404(chatId)
        db.session.delete(inchat)
        db.session.commit()
        return '', 204

# Register the Endpoints
api.add_resource(InChatListResource, '/inChats')
api.add_resource(InChatResource, '/inChats/<int:chatId>')

# MESSAGE
class Message(db.Model):
    __tablename__ = 'message'
    messageId = db.Column(db.Integer, primary_key = True)
    chatId = db.Column(db.Integer, db.ForeignKey('chat.chatId'))
    userId = db.Column(db.Integer)
    message = db.Column(db.String(400))
    timeStamp = db.Column(db.Integer)

    def __repr__(self):
        return "messageId: {}, chatId: {}, userId: {}, message: {}, timestamp: {}".format(self.messageId, self.chatId, self.chatId, self.message, self.timeStamp)

# Marshmallow Schema
class MessageSchema(ma.Schema):
    class Meta:
        fields = ("messageId", "chatId", "userId", "message", "timeStamp")

# Schema for Multiple Messages
messages_schema = MessageSchema(many = True)

# Schema for Single Messages
message_schema = MessageSchema()


# Endpoint for Returning a List of Messages
class MessagesListResource(Resource):
    def get(self):
        posts = Message.query.all()
        return messages_schema.dump(posts)

    def post(self):
        new_message = Message(
            chatId = request.json['chatId'],
            userId = request.json['userId'],
            message = request.json['message'],
            timestamp = request.json['timeStamp'],
        )
        db.session.add(new_message)
        db.session.commit()
        return message_schema.dump(new_message)


# Endpoint for a Single Message
class MessageResource(Resource):

    def get(self, messageId):
        message = Message.query.get_or_404(messageId)
        return message_schema.dump(message)
        

    def patch(self, messageId):
        message = Message.query.get_or_404(messageId)

        if "messageId" in request.json['messageId']:
            message.messageId = request.json['messageId']

        if 'message' in request.json['message']:
            message.message = request.json['message']

        if 'timestamp' in request.json['timestamp']:
            message.timestamp = request.json['timestamp']

        db.session.commit()
        return message_schema.dump(message)

    def delete(self, messageId):
        message = Message.query.get_or_404(messageId)
        db.session.delete(message)
        db.session.commit()
        return message_schema.dump(message)
        
# Register Endpoints
api.add_resource(MessagesListResource, '/messages')
api.add_resource(MessageResource, '/messages/<int:messageId>')


# ANNOUNCEMENT

class Announcement(db.Model):
    __tablename__ = 'announcement'

    announcementId = db.Column(db.Integer, primary_key = True)
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId'))
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    timeStamp = db.Column(db.Integer)

    def __repr__(self):
        return "<Course Id: {}, Name: {}, Description: {}, timeStamp: {}>".format(self.courseId, self.name, self.description, self.timeStamp)


# Marshmallow Schema
class AnnouncementSchema(ma.Schema):
    class Meta:
        fields = ("announcementId", "courseId", "name", "description", "timeStamp")

# Schema for Multiple Announcements
announcements_schema = AnnouncementSchema(many = True)

# Schema for Single Announcement
announcement_schema = AnnouncementSchema()

# Endpoint for a List of Announcements
class AnnouncementListResource(Resource):
    def get(self):
        announcement = Announcement.query.all()
        return announcement_schema.dump(announcement)

    def post(self):
        new_announcement = Announcement(
            courseId = request.json['courseId'],
            name = request.json['name'],
            description = request.json['description'],
            timeStamp = request.json['timeStamp'],
        )

        db.session.add(new_announcement)
        db.session.commit()
        return announcement_schema.dump(new_announcement)


# Endpoint for a Single Announcement
class AnnouncementResource(Resource):
    def get(self, announcementId):
        announcement = Announcement.query.get_or_404(announcementId)
        return announcement_schema.dump(announcement)

    def patch(self, announcementId):
        announcement = Announcement.query.get_or_404(announcementId)

        if 'courseId' in request.json['courseId']:
            announcement.courseId = request.json['courseId']

        if 'name' in request.json['name']:
            announcement.name = request.json['name']

        if 'description' in request.json['description']:
            announcement.description = request.json['description']

        if 'timeStamp' in request.json['timeStamp']:
            announcement.timeStamp = request.json['timeStamp']

        db.session.commit()
        return announcement_schema.dump(announcement)

    def delete(self, announcementId):
        announcement = Announcement.query.get_or_404(announcementId)
        db.session.delete(announcement)
        db.session.commit()
        return '', 204

# Register Endpoints
api.add_resource(AnnouncementListResource, '/announcements')
api.add_resource(AnnouncementResource, '/announcements/<int:announcementId>')



# Course Assignment
class CourseAssignment(db.Model):
    __tablename__ = 'courseAssignment'
    
    courseAssignmentId = db.Column(db.Integer, primary_key = True)
    courseId = db.Column(db.Integer, db.ForeignKey('course.courseId'))
    moduleId = db.Column(db.Integer, db.ForeignKey('module.moduleId'))
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    dueDate = db.Column(db.Integer)

    def __repr__(self):

        return "<courseAssignmentId: {}, courseId: {}, moduleId: {},  Name: {}, Description: {}, dueDate: {}>".format(self.courseAssignmentId, self.courseId, self.moduleId, self.name, self.description, self.dueDate)

# Marshmallow Schema
class CourseAssignmentSchema(ma.Schema):
    class Meta:
        fields = ("courseAssignmentId", "courseId", "name", "description", "dueDate")

# Schema for Multiple Course Assignments
courseAssignmentsSchema = CourseAssignmentSchema(many = True)

# Schema for Single Course Assignment
course_Assignment_Schema = CourseAssignmentSchema()

# Endpoint for a List of Course Assignments
class CourseAssignmentsListResource(Resource):

    def get(self):
        posts = CourseAssignment.query.all()
        return course_Assignment_Schema.dump(posts)


    def post(self):
        newCourseAssignment = CourseAssignment(
            courseId = request.json['courseId'],
            name = request.json['name'],
            description = request.json['description'],
            dueDate = request.json['dueDate']
        )
        db.session.add(newCourseAssignment)
        db.session.commit()
        return course_Assignment_Schema.dump(newCourseAssignment)


# Endpoint for a Single Course Assignment
class CourseAssignmentResource(Resource):
    def get(self, courseId):
        courseAssignment = CourseAssignment.get_or_404(courseId)
        return course_Assignment_Schema.dump(courseAssignment)


    def patch(self, courseId):
        courseAssignment = CourseAssignment.get_or_404(courseId)

        if 'courseId' in request.json['courseId']:
            courseAssignment.courseId = request.json['courseId']

        if 'name' in request.json['name']:
            courseAssignment.name = request.json['name']
        if 'description' in request.json['description']:

            courseAssignment.description = request.json['description']
        if 'dueDate' in request.json['dueDate']:
            courseAssignment.dueDate = request.json['dueDate']

        db.session.commit()
        return course_Assignment_Schema.dump(courseAssignment)

# Register Endpoints
api.add_resource(CourseAssignmentsListResource, '/courseAssignments')
api.add_resource(CourseAssignmentResource, '/courseAssignments/<int:courseId>')
    


# STUDENT ASSIGNMENT
class StudentAssignment(db.Model):
    __tablename__ = 'studentAssignment'

    assignmentId = db.Column(db.Integer, primary_key = 50)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    dueDate = db.Column(db.Integer)
    grade = db.Column(db.Float)
    turnedIn = db.Column(db.Boolean)

    def __repr__(self):
        return "Assignment Id: {}, Name: {}, Description: {}, Due Date: {}, Grade: {}, Turned in: {}".format(self.assignmentId, self.name, self.description, self.dueDate, self.grade, self.turnedIn)

# Marshmallow Schema
class StudentAssignmentSchema(ma.Schema):
    class Meta:
        fields = ("assignmentId", "name", "description", "dueDate", "grade", "turnedIn")

# Schema for Multiple Student Assignments
students_assignment_schema = StudentAssignmentSchema(many = True)

# Schema for Single Student Assignments
student_assignment_schema = StudentAssignmentSchema()

# Endpoint for the List of Student Assignments
class StudentAssignmentListResource(Resource):
    def get(self):
        student_assignment = StudentAssignment.query.all()
        return students_assignment_schema.dump(student_assignment)

    def post(self):
        newStudentAssignment = StudentAssignment(
            name = request.json['name'],
            description = request.json['description'],
            dueDate = request.json['dueDate'],
            grade = request.json['grade'],
            turnedIn = request.json['turnedIn']
        )

        db.session.add(newStudentAssignment)
        db.session.commit()
        return students_assignment_schema.dump(newStudentAssignment)

# Endpoint for a Single Student Assignment
class StudentAssignmentResource(Resource):

    def get(self, assignmentId):
        student_ass = StudentAssignment.query.get_or_404(assignmentId)
        return student_assignment_schema.dump(student_ass)

    def patch(self, assignmentId):
        student_ass = StudentAssignment.query.get_or_404(assignmentId)

        if 'assignmentId' in request.json['assignmentId']:
            student_ass.assignmentId = request.json['assignmentId']

        if 'name' in request.json['name']:
            student_ass.name = request.json['name']

        if 'description' in request.json['description']:
            student_ass.description = request.json['description']

        if 'dueDate' in request.json['dueDate']:
            student_ass.dueDate = request.json['dueDate']

        if 'grade' in request.json['grade']:
            student_ass.grade = request.json['grade']

        if 'turnedIn' in request.json['turnedIn']:
            student_ass.turnedIn = request.json['turnedIn']

        db.session.commit()
        return student_assignment_schema.dump(student_ass)

    def delete(self, assignmentId):
        student_ass = StudentAssignment.query_or_404(assignmentId)
        db.session.delete(student_ass)
        db.session.commit()
        return '', 204


# Register Endpoints
api.add_resource(StudentAssignmentListResource, '/studentAssignments')
api.add_resource(StudentAssignmentResource, '/studentAssignments/<int:assignmentId>')

# Course
class Course(db.Model):
    __tablename__ = 'course'
    courseId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500)) 
    students = db.relationship("StudentCourses")
    teachers = db.relationship("TeacherCourses")
    modules = db.relationship("Module")

    def __repr__(self):
        return "courseId: {}, Name: {}, description: {}, students: {}, teachers: {}, modules: {}".format(self.courseId, self.name, self.description, self.students, self.teachers, self.modules)

class CourseSchema(ma.Schema):
    courseId = fields.Int()
    name = fields.Str()
    description = fields.Str()
    students = ma.Nested(students_schema)
    teachers = ma.Nested(teachers_schema)
    modules = ma.Nested(modules_schema)

    class Meta:
        fields = ("courseId", "name", "description", "students", "teachers", "modules")

courses_schema = CourseSchema(many=True)

course_schema = CourseSchema()

class CourseListResource(Resource):
    def get(self):
        courses = Course.query.all()
        return courses_schema.dump(courses)

    def post(self):
        new_course = Course(
            name=request.json['name'],
            description=request.json['description'],
        )
        db.session.add(new_course)
        db.session.commit()
        return course_schema.dump(new_course)

class CourseResource(Resource):
    def get(self, course_id):
        course = Course.query.get_or_404(course_id)
        return course_schema.dump(course)

    def patch(self, course_id):
        course = Course.query.get_or_404(course_id)
        if 'courseId' in request.json:
            course.courseId = request.json['courseId']
        if 'name' in request.json:
            course.name = request.json['name']
        if 'description' in request.json:
            course.description = request.json['description']
        db.session.commit()
        return course_schema.dump(course)

    def delete(self, course_id):
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        return '', 204



api.add_resource(CourseListResource, '/courses') 
api.add_resource(CourseResource, '/courses/<int:course_id>') 
'''
curl http://localhost:5000/courses \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"cs OOP", "description":"i am describing this course"}'
'''


class Login(db.Model):
    __tablename__ = 'login'
    loginId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))

    def __repr__(self):
        return "loginId: {}, email: {}, password: {}".format(self.courseId, self.email, self.password)


class LoginSchema(ma.Schema):
    class Meta:
        fields = ("loginId", "email", "password")


login_schema = LoginSchema()
logins_schema = LoginSchema(many=True)


class LoginListResource(Resource):
    def get(self):
        logins = Login.query.all()
        return logins_schema.dump(logins)

    def post(self):
        new_login = Login(
            email=request.json['email'],
            password=request.json['password'],
        )
        db.session.add(new_login)
        db.session.commit()
        return login_schema.dump(new_login)


class LoginResource(Resource):
    def get(self, login_id):
        login = Login.query.get_or_404(login_id)
        return login_schema.dump(login)

    def patch(self, login_id):
        login = Login.query.get_or_404(login_id)

        if 'studentId' in request.json:
            login.studentId = request.json['studentId']
        if 'email' in request.json:
            login.email = request.json['email']
        if 'password' in request.json:
            login.password = request.json['password']

        db.session.commit()
        return login_schema.dump(login)

    def delete(self, login_id):
        login = Login.query.get_or_404(login_id)
        db.session.delete(login)
        db.session.commit()
        return '', 204


api.add_resource(LoginListResource, '/logins')
api.add_resource(LoginResource, '/logins/<int:login_id>')

'''
curl http://localhost:5000/logins \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"email":"deanallen@gmail.com", "password":"passTest.98", "userId": "999"}'
'''



# main function that gets flask runnning
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)