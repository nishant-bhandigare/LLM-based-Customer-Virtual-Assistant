import 'package:chatbot/screens/home.dart';
import 'package:chatbot/screens/login.dart';
import 'package:chatbot/widgets/my_button.dart';
import 'package:chatbot/widgets/my_textfield.dart';
import 'package:dio/dio.dart';
import 'package:flutter/material.dart';


class RegisterPage extends StatelessWidget {
  RegisterPage({super.key});

  // text editing controllers
  final emailController = TextEditingController();
  final nameController=TextEditingController();
  final passwordController = TextEditingController();

  // sign user in method
  Future<bool> signUserIn() async{
    final dio = Dio();
    var result=await dio.post('https://test-js-szch.onrender.com/register',data:{
      "name":nameController.text,
      "email":emailController.text,
      "password":passwordController.text
    });
    if(result.statusCode==200){
      return true;
    }
    return false;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[300],
      resizeToAvoidBottomInset: false,
      body: SafeArea(
        
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const SizedBox(height: 50),

              // logo
              const Icon(
                Icons.lock,
                size: 100,
              ),

              const SizedBox(height: 50),

              // welcome back, you've been missed!
              Text(
                'Welcome back you\'ve been missed!',
                style: TextStyle(
                  color: Colors.grey[700],
                  fontSize: 16,
                ),
              ),

              const SizedBox(height: 25),

              // username textfield
              MyTextField(
                controller: emailController,
                hintText: 'Email',
                obscureText: false,
              ),

              const SizedBox(height: 10),

              // password textfield
              MyTextField(
                controller: nameController,
                hintText: 'Name',
                obscureText: false,
              ),

              const SizedBox(height: 10),

              MyTextField(
                controller: passwordController,
                hintText: 'Password',
                obscureText: true,
              ),

              // forgot password?
              

              const SizedBox(height: 20),

              // sign in button
              MyButton(
                name: "Register",
                onTap: ()async{
                  var res=await signUserIn();
                  res==true?Navigator.push(context, MaterialPageRoute(builder: (context)=>const HomeScreen())):Navigator.push(context, MaterialPageRoute(builder: (context)=> RegisterPage()));
                },
              ),

              const SizedBox(height: 20),

              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 25.0),
                child: Row(
                  children: [
                    Expanded(
                      child: Divider(
                        thickness: 0.5,
                        color: Colors.grey[400],
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 10.0),
                      child: Text(
                        'Or continue with',
                        style: TextStyle(color: Colors.grey[700]),
                      ),
                    ),
                    Expanded(
                      child: Divider(
                        thickness: 0.5,
                        color: Colors.grey[400],
                      ),
                    ),
                  ],
                ),
              ),

               const SizedBox(height: 15),

              MyButton(
                name: "SignIn",
                onTap: ()=>{
                  Navigator.push(context, MaterialPageRoute(builder: (context)=> LoginPage()))
                },
              ),


              // or continue with
              // Padding(
              //   padding: const EdgeInsets.symmetric(horizontal: 25.0),
              //   child: Row(
              //     children: [
              //       Expanded(
              //         child: Divider(
              //           thickness: 0.5,
              //           color: Colors.grey[400],
              //         ),
              //       ),
              //       Padding(
              //         padding: const EdgeInsets.symmetric(horizontal: 10.0),
              //         child: Text(
              //           'Or continue with',
              //           style: TextStyle(color: Colors.grey[700]),
              //         ),
              //       ),
              //       Expanded(
              //         child: Divider(
              //           thickness: 0.5,
              //           color: Colors.grey[400],
              //         ),
              //       ),
              //     ],
              //   ),
              // ),


              // google + apple sign in buttons
              // Row(
              //   mainAxisAlignment: MainAxisAlignment.center,
              //   children: const [
              //     // google button
              //     SquareTile(imagePath: 'lib/images/google.png'),

              //     SizedBox(width: 25),

              //     // apple button
              //     SquareTile(imagePath: 'lib/images/apple.png')
              //   ],
              // ),

              const SizedBox(height: 50),

              // not a member? register now
             
            ],
          ),
        ),
      ),
    );
  }
}