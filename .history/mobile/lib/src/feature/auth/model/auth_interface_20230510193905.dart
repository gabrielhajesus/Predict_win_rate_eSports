import 'domain/user.dart';

abstract class ILogin {
  Future<User> login(User user);
  Future<User> signup(User user);
  Future<User> forgotpass(User user);
}
