import 'package:dio/dio.dart';

import '../../model/login_interface.dart';
import '../../model/domain/user.dart';
import '../dto/user_dto.dart';

class LoginRepository implements ILogin {
  @override
  Future<User> login(User user) async {
    final dto = UserDto.fromDomain(user);
    final response = await Dio().post(
      'http://flutter-api.mocklab.io/auth/login',
      data: dto.toJson(),
    );
    if (response.statusCode == 200) {
      final token = response.headers.value('Authorization');
      final domain = User(user.username, null, token: token);
      return Future.value(domain);
    } else {
      throw Exception("Usuário ou Senha Inválidos!");
    }
  }
}
