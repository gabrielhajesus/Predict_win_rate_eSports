import 'package:flutter/material.dart';

class CustomTextFormField extends StatelessWidget {
  const CustomTextFormField(
      {Key? key,
      required this.hint,
      this.obscure = false,
      required this.textInputType,
      required this.onChanged})
      : super(key: key);

  final String hint;
  final bool obscure;
  final TextInputType textInputType;
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
        decoration: InputDecoration(
          hintText: hint,
          border: InputBorder.none,
        ),
        textAlignVertical: TextAlignVertical.center,
      ),
    );
  }
}
