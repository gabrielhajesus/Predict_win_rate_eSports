import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';
import '../model/login_usecase.dart';

part 'auth_viewmodel.g.dart';

class AuthViewmodel = AuthViewmodelBase with _$AuthViewmodel;

abstract class AuthViewmodelBase with Store {
  @observable
  String _email = "";

  @action
  void setEmail(String value) {
    _email = value;
  }

  @observable
  String _password = "";

  @action
  void setPassword(String value) {
    _password = value;
  }
}
