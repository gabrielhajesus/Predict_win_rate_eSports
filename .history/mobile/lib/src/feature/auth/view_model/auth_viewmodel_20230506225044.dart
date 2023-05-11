import 'package:flutter_triple/flutter_triple.dart';
import 'package:mobx/mobx.dart';
part 'auth_viewmodel.g.dart';

class AuthViewModel extends NotifierStore<Exception, int> {
  AuthViewModel() : super(0);
}

class AuthViewmodel = AuthViewmodelBase with _$AuthViewmodel;

abstract class AuthViewmodelBase with Store {}
