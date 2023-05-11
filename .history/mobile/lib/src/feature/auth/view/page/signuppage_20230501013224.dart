import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:localization/localization.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';
import 'package:predict/src/commom/form_text_field.dart';

import '../../view_model/login_viewmodel.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({Key? key}) : super(key: key);

  @override
  State<SignUpPage> createState() => _SignUpPageState();
}

class _SignUpPageState extends ModularState<SignUpPage, LoginViewModel> {
  late ColorScheme _colors;
  late ThemeData _theme;

  Widget get _loadingIndicator => Visibility(
        child: const LinearProgressIndicator(
          backgroundColor: Colors.blueGrey,
        ),
        visible: store.isLoading,
      );

  Widget get _username => widget.createFormField(
        title: 'username'.i18n(),
        theme: _theme,
        keyboardType: TextInputType.text,
        textInputAction: TextInputAction.next,
        hint: 'username_hint'.i18n(),
        //enabled: !store.isLoading,
        //errorText: store.error.username,
        //onChange: (value) => store.username = value,
      );

  Widget get _password => widget.createFormField(
        title: 'password'.i18n(),
        theme: _theme,
        keyboardType: TextInputType.text,
        obscureText: true,
        hint: 'password_hint'.i18n(),
        //enabled: !store.isLoading,
        //errorText: store.error.username,
        //onChange: (value) => store.username = value,
      );

  Widget get _repassword => widget.createFormField(
        title: 'repassword'.i18n(),
        theme: _theme,
        keyboardType: TextInputType.text,
        obscureText: true,
        hint: 'repassword_hint'.i18n(),
        //enabled: !store.isLoading,
        //errorText: store.error.username,
        //onChange: (value) => store.username = value,
      );

  Widget get _email => widget.createFormField(
        title: 'email'.i18n(),
        theme: _theme,
        keyboardType: TextInputType.emailAddress,
        textInputAction: TextInputAction.next,
        hint: 'email_hint'.i18n(),
        //enabled: !store.isLoading,
        //errorText: store.error.username,
        //onChange: (value) => store.username = value,
      );

  Widget get _phone => widget.createFormField(
        title: 'phone'.i18n(),
        theme: _theme,
        mask: "(##) #####-####",
        keyboardType: TextInputType.phone,
        textInputAction: TextInputAction.next,
        hint: 'phone_hint'.i18n(),
        //enabled: !store.isLoading,
        //errorText: store.error.username,
        //onChange: (value) => store.username = value,
      );

  Widget get _birthdate => widget.createFormField(
        title: 'birthdate'.i18n(),
        theme: _theme,
        mask: "##/##/####",
        keyboardType: TextInputType.datetime,
        validator: (value) {
          if (value == null || value.isEmpty) {
            return null;
          }
          final components = value.split("/");
          if (components.length == 3) {
            final day = int.tryParse(components[0]);
            final month = int.tryParse(components[1]);
            final year = int.tryParse(components[2]);
            if (day != null && month != null && year != null) {
              final date = DateTime(year, month, day);
              if (date.year == year && date.month == month && date.day == day) {
                return null;
              }
            }
          }
          return "wrong date";
        },
        textInputAction: TextInputAction.next,
        hint: 'birthdate_hint'.i18n(),
        //enabled: !store.isLoading,
        //errorText: store.error.username,
        //onChange: (value) => store.username = value,
      );

  Widget get _loginButton => Container(
        margin: const EdgeInsets.fromLTRB(30, 15, 30, 5),
        width: double.infinity,
        height: 56,
        child: ElevatedButton(
          style: ButtonStyle(
            shape: MaterialStateProperty.all<RoundedRectangleBorder>(
              RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(6),
              ),
            ),
          ),
          onPressed: store.isLoading ? null : store.login,
          child: Text('signup'.i18n()),
        ),
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
                  _loadingIndicator,
                  const SizedBox(height: 5),
                  _username,
                  _password,
                  _repassword,
                  _email,
                  _phone,
                  _birthdate,
                  _loginButton,
                ],
              ),
            );
          }),
        ),
      ),
    );
  }
}
