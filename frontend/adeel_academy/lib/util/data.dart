import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map<String, dynamic>> getIndividual(String endpoint, int id) async {
  Uri url = Uri.http("127.0.0.1:5000", "/" + endpoint + "/" + id.toString());
  http.Response dat = await http.get(url, headers: {
    "Accept": "application/json",
    "Access-Control-Allow-Origin": "*",
  });
  // print(jsonDecode(dat.body));

  final Map<String, dynamic> out = json.decode(dat.body);

  print(out);

  return out;
}

Future<List<dynamic>> getList(String endpoint) async {
  Uri url = Uri.http("127.0.0.1:5000", "/" + endpoint);
  http.Response dat = await http.get(url, headers: {
    "Accept": "application/json",
    "Access-Control-Allow-Origin": "*",
  });

  List<dynamic> out = [];

  for (var item in json.decode(dat.body)) {
    out.add(item);
  }

  print(out);

  return out;
}

Future<Map<String, dynamic>> putData(String endpoint, Map data) async {
  Uri url = Uri.http("127.0.0.1:5000", "/" + endpoint);

  http.Response dat = await http.post(
    url,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
    body: jsonEncode(data),
  );

  final Map<String, dynamic> out = json.decode(dat.body);

  print(out);

  return null;
}
