import 'package:flutter_modular/flutter_modular.dart';
import 'package:localization/localization.dart';

import 'domain/user.dart';
import 'login_interface.dart';

class LoginUseCase {
  final repository = Modular.get<ILogin>();

  String? validateUsername(String username) {
    if (username.isEmpty) {
      return 'username_required'.i18n();
    }

    return null;
  }

  String? validatePassword(String password) {
    if (password.isEmpty) {
      return 'login_password_required'.i18n();
    }
    if (password.length < 4) {
      return 'login_password_minimun'.i18n();
    }
    return null;
  }

  Future<User> login(String username, String password) {
    return repository.login(User(username, password));
  }

  Future<User> signup(String username, String password) {
    return repository.signup(User(username, password));
  }

  Future<User> forgotpass(String username, String password) {
    return repository.forgotpass(User(username, password));
  }
}
