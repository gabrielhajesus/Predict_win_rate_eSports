import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:localization/localization.dart';
import 'package:predict/src/commom/form_text_field.dart';
import '../../view_model/auth_viewmodel.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginPagePageState();
}

class _LoginPagePageState extends State<LoginPage> {
  late ColorScheme _colors;
  late ThemeData _theme;
  final store = AuthViewmodel();

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

  Widget get _password => widget.createFormField(
        title: 'password'.i18n(),
        theme: _theme,
        keyboardType: TextInputType.text,
        obscureText: true,
        hint: 'password_hint'.i18n(),
        enabled: !store.loading,
        onChange: (value) => store.password = value,
      );

  Widget get _email => widget.createFormField(
        title: 'email'.i18n(),
        theme: _theme,
        keyboardType: TextInputType.emailAddress,
        textInputAction: TextInputAction.next,
        hint: 'email_hint'.i18n(),
        enabled: !store.loading,
        onChange: (value) => store.email = value,
      );

  @override
  Widget build(BuildContext context) {
    _theme = Theme.of(context);
    _colors = _theme.colorScheme;

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
                  _logo,
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
