import 'package:mongo_dart/mongo_dart.dart';

class MongoDataBase {
  Future<List<Map<String, dynamic>>> fetchData() async {
    Db db = await Db.create(
        'mongodb+srv://gabrielhjalberto:gabriel123@cluster0.t8961c5.mongodb.net/Predict_win_rate?retryWrites=true&w=majority');
    await db.open();

    final collection = db.collection('teams_details');
    final data = await collection.find().toList();

    await db.close();

    return data;
  }
}
