import 'package:flutter/material.dart';

class CustomTextFormField extends StatelessWidget {
  const CustomTextFormField(
      {Key? key,
      required this.hint,
      this.obscure = false,
      required this.textInputAction,
      required this.textInputType,
      required this.icon,
      required this.onChanged})
      : super(key: key);

  final String hint;
  final bool obscure;
  final TextInputAction textInputAction;
  final TextInputType textInputType;
  final Icon icon;
  final Function(String) onChanged;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        shape: BoxShape.rectangle,
        color: Colors.grey[200],
        borderRadius: BorderRadius.circular(32),
      ),
      padding: const EdgeInsets.only(left: 16),
      child: TextFormField(
        obscureText: obscure,
        keyboardType: textInputType,
        onChanged: onChanged,
        textInputAction: textInputAction,
        decoration: InputDecoration(
          hintText: hint,
          border: InputBorder.none,
          icon: icon,
        ),
        textAlignVertical: TextAlignVertical.center,
      ),
    );
  }
}
