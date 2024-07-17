import 'package:chatbot/screens/talk.dart';
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(height: 40),
            HomeHeader(userName: "Michael"),
            SizedBox(height: 20),
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 20),
              child: Row(
                children: [
                  Activity(text: 'Chat', iconData: Icons.chat_outlined,),
                  SizedBox(width: 20),
                  Activity(text: 'Talk', iconData: Icons.mic_none,),
                ],
              ),
            ),
            SizedBox(height: 20),
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 20),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  Text("History",
                      style:
                          TextStyle(fontSize: 18, fontWeight: FontWeight.w500)),
                  Spacer(),
                  Text("See All",
                      style:
                          TextStyle(fontSize: 15, fontWeight: FontWeight.w500)),
                  SizedBox(width: 10),
                  Icon(Icons.arrow_forward_ios_rounded, size: 15),
                ],
              ),
            ),
            SizedBox(height: 20),
            HistoryItem(),
          ],
        ),
      ),
    );
  }
}

class HomeHeader extends StatelessWidget {
  const HomeHeader({super.key, required this.userName});

  final String userName;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.of(context).size.width,
      padding: const EdgeInsets.symmetric(horizontal: 20),
      height: 60,
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          const CircleAvatar(
            radius: 25,
          ),
          const SizedBox(width: 20),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text("Hey there!", style: TextStyle(fontSize: 15)),
              Text(
                userName,
                style: const TextStyle(fontSize: 20),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class HistoryItem extends StatelessWidget {
  const HistoryItem({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.maxFinite,
      margin: const EdgeInsets.symmetric(horizontal: 20),
      padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 15),
      decoration: BoxDecoration(
        border: Border.all(),
        borderRadius: BorderRadius.circular(30),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Container(
            width: 50,
            height: 50,
            decoration: BoxDecoration(
              border: Border.all(),
              borderRadius: BorderRadius.circular(15),
            ),
          ),
          const SizedBox(width: 15),
          const Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Title"),
              Text("Title"),
            ],
          ),
        ],
      ),
    );
  }
}

class Activity extends StatelessWidget {
  const Activity({super.key, required this.text, required this.iconData});

  final String text;
  final IconData iconData;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        height: MediaQuery.of(context).size.height * 0.3,
        padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 15),
        decoration: BoxDecoration(
          border: Border.all(),
          borderRadius: BorderRadius.circular(30),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            InkWell(
              onTap: (){
                Navigator.of(context).push(MaterialPageRoute(builder: (context) => const Talk()));
              },
              child: Container(
                width: double.maxFinite,
                height: MediaQuery.of(context).size.height*0.15,
                decoration: BoxDecoration(
                  border: Border.all(),
                  borderRadius: BorderRadius.circular(40),
                ),
                child: Center(
                  child: Icon(iconData, size: MediaQuery.of(context).size.width*0.1,),
                ),
              ),
            ),
            Text("$text with Morgan", style: const TextStyle(fontSize: 18), textAlign: TextAlign.center),
          ],
        ),
      ),
    );
  }
}
