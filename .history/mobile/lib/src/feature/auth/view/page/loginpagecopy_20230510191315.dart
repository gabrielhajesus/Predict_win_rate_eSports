import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:localization/localization.dart';
import 'package:predict/src/commom/form_text_field.dart';

import '../../view_model/auth_viewmodel.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginpageState();
}

class _LoginpageState extends State<LoginPage> {
  bool obscureText = true;
  late ColorScheme _colors;
  late ThemeData _theme;
  final store = AuthViewmodel();

  @override
  Widget build(BuildContext context) {
    final _logo = Hero(
      tag: 'hero',
      child: CircleAvatar(
        backgroundColor: Colors.transparent,
        radius: 150.0,
        child: Image.asset(
          'lib/assets/images/title.png',
        ),
      ),
    );

    Widget get _loadingIndicator => Visibility(
      visible: store.loading,
      child: const LinearProgressIndicator(
        backgroundColor: Colors.blueGrey,
      ),
    );

    Widget get _email => widget.createFormField(
      title: 'email'.i18n(),
      keyboardType: TextInputType.emailAddress,
      textInputAction: TextInputAction.next,
      theme: _theme,
      enabled: !store.loading,
      hint: 'email_hint'.i18n(),
      onChange: (value) => store.email = value,
      );

      Widget get _password => widget.createFormField(
      title: 'password'.i18n(),
      theme: _theme,
      keyboardType: TextInputType.text,
      obscureText: true,
      hint: 'password_hint'.i18n(),
      enabled: !store.loading,
      onChange: (value) => store.password = value,
    );

    final _loginButton = Padding(
      padding: const EdgeInsets.symmetric(vertical: 16.0),
      child: ElevatedButton(
        onPressed: () async => {
          Modular.to.pushNamed('/home'),
        },
        child:
            Text('login'.i18n(), style: const TextStyle(color: Colors.white)),
      ),
    );

    final _forgotLabel = TextButton(
      child: Text(
        'forgot_password'.i18n(),
        style: const TextStyle(color: Colors.black54),
      ),
      onPressed: () async => {
        Modular.to.pushNamed('/auth/forgotpass'),
      },
    );

    final _signupLabel = TextButton(
      child: Text(
        'signup'.i18n(),
        style: TextStyle(color: Colors.black54),
      ),
      onPressed: () async => {
        Modular.to.pushNamed('/auth/signup'),
      },
    );

    return Scaffold(
      appBar: AppBar(title: Text('signup'.i18n())),
      body: Center(
        child: SingleChildScrollView(
          child: Observer(builder: (_) {
            return Form(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.center,
                mainAxisSize: MainAxisSize.max,
                children: [
                  _loadingIndicator,
                  const SizedBox(height: 5),
                  _email,
                  _password,
                ],
              ),
            );
          }),
        ),
      ),
    );
  }
}
