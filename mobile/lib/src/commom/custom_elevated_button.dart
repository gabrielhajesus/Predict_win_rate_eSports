import 'package:flutter/material.dart';
import 'package:localization/localization.dart';

class CustomElevatedButton extends ElevatedButton {
  CustomElevatedButton({
    Key? key,
    required String text,
    required VoidCallback onPressed,
  }) : super(
            key: key,
            onPressed: onPressed,
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all<Color>(
                  const Color.fromARGB(201, 14, 2, 238)),
            ),
            child: Text(
              text.i18n(),
              style: const TextStyle(
                color: Color.fromARGB(255, 255, 255, 255),
              ),
            ));
}
