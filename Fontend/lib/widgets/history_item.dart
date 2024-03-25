import 'package:flutter/material.dart';

class HistoryItem extends StatelessWidget{
  const HistoryItem({super.key});

  @override
  Widget build(BuildContext context) {
    return(Container(
      padding: EdgeInsets.all(8.0),
      margin: EdgeInsets.symmetric(vertical: 8.0),
      decoration: BoxDecoration(
        border: Border.all(color: Colors.black),
        borderRadius: BorderRadius.circular(15),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          CircleAvatar(
            child: Image.asset(
              "assets/icons/speak.png",
              width: 30,
            ),
          ),
          Text("data"),
          Icon(Icons.more_vert),
        ],
      ),
    ));
  }

}