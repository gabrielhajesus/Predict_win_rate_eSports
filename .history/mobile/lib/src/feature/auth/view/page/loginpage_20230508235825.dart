import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:localization/localization.dart';
import 'package:predict/src/commom/custom_textformfield.dart';

import '../../../../commom/constants.dart';
import '../../../../commom/custom_icon_button.dart';
import '../../view_model/auth_viewmodel.dart';
import '../../view_model/login_viewmodel.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginpageState();
}

class _LoginpageState extends State<LoginPage> {
  bool obscureText = true;
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

    final _email = CustomTextFormField(
      textInputType: TextInputType.emailAddress,
      textInputAction: TextInputAction.next,
      onChanged: store.setEmail,
      enabled: !store.loading,
      hint: 'email_hint'.i18n(),
      icon: Icon(Icons.person),
      suffix: widget,
    );

    final _password = CustomTextFormField(
      obscure: !store.passwordVisible,
      textInputType: TextInputType.text,
      textInputAction: TextInputAction.done,
      onChanged: store.setPassword,
      enabled: !store.loading,
      hint: 'password_hint'.i18n(),
      icon: Icon(Icons.lock),
      suffix: CustomIconButton(
        radius: 32,
        iconData:
            store.passwordVisible ? Icons.visibility_off : Icons.visibility,
        onTap: store.togglePasswordVisibility,
      ),
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

    return SafeArea(
      child: Scaffold(
        backgroundColor: Color.fromARGB(73, 0, 34, 254),
        body: Container(
          alignment: Alignment.center,
          margin: const EdgeInsets.all(32),
          child: Card(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16),
            ),
            elevation: 16,
            child: Center(
              child: SingleChildScrollView(
                child:  Form(
                      child: Column(
                        children: <Widget>[
                          _logo,
                          SizedBox(height: 48.0),
                          _email,
                          SizedBox(height: 8.0),
                          _password,
                          SizedBox(height: 24.0),
                          _loginButton,
                          _signupLabel,
                          _forgotLabel
                        ],
                      ),
                    );
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
