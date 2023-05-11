import 'package:flutter_modular/flutter_modular.dart';
import 'data/repository/auth_repository.dart';
import 'model/auth_interface.dart';
import 'model/auth_usecase.dart';
import '../../feature/auth/view_model/auth_viewmodel.dart';
import 'view/page/forgotpasspage.dart';
import 'view/page/loginpage.dart';
import 'view/page/signuppage.dart';

class authModule extends Module {
  @override
  List<Bind<Object>> get binds => [
        Bind.factory((i) => AuthViewmodel()),
        Bind.factory((i) => AuthUseCase()),
        Bind.factory<IAuth>((i) => AuthRepository()),
      ];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (_, __) => const LoginPage()),
        ChildRoute('/login', child: (_, __) => const LoginPage()),
        ChildRoute('/signup', child: (_, __) => const SignUpPage()),
        ChildRoute('/forgotpass', child: (_, __) => const ForgotPassPage()),
      ];
}

class AuthModule extends Module {
  static const AUTH_ROUTE = "/auth";

  @override
  List<Bind> get binds => [];

  @override
  List<ModularRoute> get routes =>
      [ModuleRoute(AUTH_ROUTE, module: AuthSingletonModule())];
}

class AuthSingletonModule extends Module {
  static const BASE_PAGE = "/";
  static const ONE_PAGE = "/login";
  static const TWO_PAGE = "/signup";
  static const THREE_PAGE = "/forgotpass";

  @override
  List<Bind> get binds => [Bind.singleton((i) => AuthViewmodel())];

  @override
  List<ModularRoute> get routes => [
        ChildRoute(ONE_PAGE, child: (context, args) => const LoginPage()),
        ChildRoute(TWO_PAGE, child: (context, args) => const SignUpPage()),
        ChildRoute(THREE_PAGE, child: (context, args) => const ForgotPassPage())
      ];
}
