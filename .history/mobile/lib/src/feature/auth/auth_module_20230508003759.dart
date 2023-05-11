import 'package:flutter_modular/flutter_modular.dart';
import 'data/repository/auth_repository.dart';
import 'model/login_interface.dart';
import 'model/login_usecase.dart';
import '../../feature/auth/view_model/auth_viewmodel.dart';
import 'view/page/forgotpasspage.dart';
import 'view/page/loginpage.dart';
import 'view/page/signuppage.dart';
import 'view_model/login_viewmodel.dart';

class AuthModule extends Module {
  @override
  List<Bind<Object>> get binds => [
        Bind.factory((i) => LoginViewModel()),
        Bind.factory((i) => LoginUseCase()),
        Bind.factory<ILogin>((i) => LoginRepository()),
      ];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (_, __) => const LoginPage()),
        ChildRoute('/login', child: (_, __) => const LoginPage()),
        ChildRoute('/signup', child: (_, __) => const SignUpPage()),
        ChildRoute('/forgotpass', child: (_, __) => const ForgotPassPage()),
      ];
}
