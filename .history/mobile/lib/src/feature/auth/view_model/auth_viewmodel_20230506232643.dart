import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';
import '../model/login_usecase.dart';

part 'auth_viewmodel.g.dart';

class AuthViewmodel = AuthViewmodelBase with _$AuthViewmodel;

abstract class AuthViewmodelBase with Store {
  String _email = "";

  void setEmail(String value) {
    _email = value;
  }

  String _password = "";

  void setPassword(String value) {
    _password = value;
  }
}
