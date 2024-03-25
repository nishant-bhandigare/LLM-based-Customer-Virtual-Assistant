const express=require('express')
const app=express()
var cors = require('cors')
const router = require('./routes/chat.routes')
const { PrismaClient } =require('@prisma/client')
const prisma = new PrismaClient()
const nodemailer = require('nodemailer');

app.use(express.json())
app.use(cors())

app.use('/',router)

app.get('/',(req,res)=>{
    res.send("Welcome to CRA")
})

app.get('/user/problem',async(req,res)=>{
    try {
        const result=await prisma.user.findMany()
        return res.status(200).json({success:true,result})
    } catch (error) {
        return res.status(400).json({success:false,message:"Internal Server Error"})
    }
})

app.get('/user/problem/:ph',async(req,res)=>{
    try {
        const phoneno=req.params.ph
        const result=await prisma.user.findMany({
            where:{
                phoneno
            }
        })
        return res.status(200).json({success:true,result})
    } catch (error) {
        return res.status(400).json({success:false,message:"Internal Server Error"})
    }
})

app.get('/test/mail',async(req,res)=>{
    const {email}=req.body
    let mailTransporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'shakthtest@gmail.com',
            pass: process.env.sender_pass
        }
    });
    
    let mailDetails = {
        from: 'organizationk14@gmail.com',
        to: email,
        subject: 'Regarding appointment',
        html:`<h1>Hi,</h1>
        <h1>Your Appointment is fixed </h1>
        `
    };
    mailTransporter.sendMail(mailDetails, function(err, data) {
        if(err) {
           return res.status(501).json({sucess:'false'})
        } else {

           return res.status(200).json({sucess:'true',message:'Email sent successfully'})
            
        }
    });
})

app.listen(3000,()=>{
    console.log('App listening at port 3000')
})