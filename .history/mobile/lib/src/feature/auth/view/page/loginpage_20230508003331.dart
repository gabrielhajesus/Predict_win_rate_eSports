import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:localization/localization.dart';
import 'package:predict/src/commom/custom_textformfield.dart';

import '../../../../commom/constants.dart';
import '../../view_model/login_viewmodel.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginpageState();
}

class _LoginpageState extends State<LoginPage> {
  bool obscureText = true;
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  hiddenButton() {
    return IconButton(
        onPressed: () {
          setState(() {
            obscureText = !obscureText;
          });
        },
        icon:
            Icon(obscureText ? Icons.visibility_off : Icons.visibility_sharp));
  }

  @override
  Widget build(BuildContext context) {
    final logo = Hero(
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
      onChanged: (email) {},
      hint: 'email_hint'.i18n(),
      icon: Icon(Icons.person),
    );

    final _password = CustomTextFormField(
      obscure: true,
      textInputType: TextInputType.none,
      textInputAction: TextInputAction.done,
      onChanged: (password) {},
      hint: 'password_hint'.i18n(),
      icon: Icon(Icons.lock),
    );

    final loginButton = Padding(
      padding: const EdgeInsets.symmetric(vertical: 16.0),
      child: ElevatedButton(
        onPressed: () async => {
          Modular.to.pushNamed('/home'),
        },
        child:
            Text('login'.i18n(), style: const TextStyle(color: Colors.white)),
      ),
    );

    final forgotLabel = TextButton(
      child: Text(
        'forgot_password'.i18n(),
        style: const TextStyle(color: Colors.black54),
      ),
      onPressed: () async => {
        Modular.to.pushNamed('/auth/forgotpass'),
      },
    );

    final signupLabel = TextButton(
      child: Text(
        'signup'.i18n(),
        style: TextStyle(color: Colors.black54),
      ),
      onPressed: () async => {
        Modular.to.pushNamed('/auth/signup'),
      },
    );

    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: ListView(
          shrinkWrap: true,
          padding: EdgeInsets.only(left: 24.0, right: 24.0),
          children: <Widget>[
            logo,
            SizedBox(height: 48.0),
            email,
            SizedBox(height: 8.0),
            password,
            SizedBox(height: 24.0),
            loginButton,
            signupLabel,
            forgotLabel
          ],
        ),
      ),
    );
  }
}
