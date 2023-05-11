import 'package:flutter_triple/flutter_triple.dart';

class AuthViewModel extends NotifierStore<Exception, int> {
  AuthViewModel() : super(0);
}

import 'package:mobx/mobx.dart';
part 'auth_viewmodel.g.dart';

class AuthViewmodel = AuthViewmodelBase with _$AuthViewmodel;

abstract class AuthViewmodelBase with Store {

}