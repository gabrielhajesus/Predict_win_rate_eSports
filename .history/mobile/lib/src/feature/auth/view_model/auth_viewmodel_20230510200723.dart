import 'package:mobx/mobx.dart';

part 'auth_viewmodel.g.dart';

class AuthViewmodel = AuthViewmodelBase with _$AuthViewmodel;

abstract class AuthViewmodelBase with Store {
  @observable
  String email = "";

  @action
  void setEmail(String value) => email = value;

  @observable
  String password = "";

  @action
  void setPassword(String value) => password = value;

  @observable
  bool passwordVisible = false;

  @action
  void togglePasswordVisibility() => passwordVisible = !passwordVisible;

  @observable
  bool loading = false;

  @observable
  bool loggedIn = false;

  @computed
  bool get isEmailValid => RegExp(
          r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?)*$")
      .hasMatch(email);

  @computed
  bool get isPasswordValid => password.length >= 6;

  @computed
  Function get loginPressed =>
      (isEmailValid && isPasswordValid && !loading) ? login : login;

  @action
  Future<void> login() async {
    loading = true;
    try {
      await login(email, password);
    } on UnimplementedError {
    } finally {
      loading = false;
    }
  }

  @action
  void logout() {
    loggedIn = false;
  }
}
