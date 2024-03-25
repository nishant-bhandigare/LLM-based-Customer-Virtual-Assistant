import 'package:chatbot/screens/talk.dart';
import 'package:chatbot/widgets/history_item.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return (Scaffold(
      appBar: AppBar(title: const Text("Hi, Michael"), ),
      body: Padding(
        padding: const EdgeInsets.all(6.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              child: const Text("How may I help\nyou today?", style: TextStyle(fontSize: 25),),
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                border: Border.all(color: Colors.black),
              ),
            ),
            const SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                InkWell(
                  child: Container(
                    width: MediaQuery.of(context).size.width * 0.5,
                    height: 208,
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      // border: Border.all(color: Colors.black),
                      borderRadius: BorderRadius.circular(15),
                      color: Colors.lightGreenAccent,
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            CircleAvatar(
                              child: Image.asset(
                                "assets/icons/mic.png",
                                width: 25,
                              ),
                            ),
                            const Spacer(),
                            IconButton(
                              onPressed: () {},
                              icon: const Icon(Icons.arrow_forward),
                            ),
                          ],
                        ),
                        const Spacer(),
                        const Text("Talk\nwith Assistant", style: TextStyle(fontSize: 22, color: Colors.black, fontWeight: FontWeight.bold)),
                      ],
                    ),
                  ),
                  onTap: (){
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => const TalkPage()),
                    );
                  },
                ),
                Column(
                  children: [
                    Container(
                      width: MediaQuery.of(context).size.width * 0.45,
                      height: 100,
                      padding: const EdgeInsets.all(12),
                      decoration: BoxDecoration(
                        // border: Border.all(color: Colors.black),
                        borderRadius: BorderRadius.circular(15),
                        color: const Color.fromRGBO(208, 162, 247, 1),
                      ),
                      child: Column(
                        children: [
                          Row(
                            children: [
                              CircleAvatar(
                                child: Image.asset(
                                  "assets/icons/keyboard.png",
                                  width: 25,
                                ),
                              ),
                              IconButton(
                                onPressed: () {},
                                icon: const Icon(Icons.arrow_forward),
                              ),
                            ],
                          ),
                          const Text("Chat with Assistant", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),),
                        ],
                      ),
                    ),
                    const SizedBox(height: 8,),
                    Container(
                      width: MediaQuery.of(context).size.width * 0.45,
                      height: 100,
                      decoration: BoxDecoration(
                        // border: Border.all(color: Colors.black),
                        borderRadius: BorderRadius.circular(15),
                        color: const Color.fromRGBO(255, 230, 230, 1),
                      ),
                    ),
                  ],
                ),
              ],
            ),
            const SizedBox(height: 20),
            const Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text("History", style: TextStyle(fontSize: 20,)),
                Text("See all"),
              ],
            ),
            const SizedBox(height: 15),
            const HistoryItem(),
            const HistoryItem(),
            const HistoryItem(),
          ],
        ),
      ),
    ));
  }
}
