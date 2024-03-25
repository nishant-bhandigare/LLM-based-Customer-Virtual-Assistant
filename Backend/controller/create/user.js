const { PrismaClient } =require('@prisma/client')
const {hashPassword, comparePassword} = require('../../utils/hashPassword')
const prisma = new PrismaClient()

const createUser=async(req,res)=>{
    const{name,email,password}=req.body
    const secPass=await hashPassword(password)
    const existingUser=await prisma.account.findFirst({
        where:{
            email
        }
    })
    if(existingUser){
        return res.status(400).json({success:false,message:"User already created"})
    }
    else{
        const create=await prisma.account.create({
            data:{
                name,email,password:secPass
            }
        })
        return res.status(200).json({success:true,message:"User created successfully"})
    }
}

const getUser=async(req,res)=>{
    const{email,password}=req.body
    const existingUser=await prisma.account.findFirst({
        where:{
            email
        }
    })
    if(existingUser){
        const conf=await comparePassword(password,existingUser.password)
        if(conf){
            return res.status(200).json({success:"true",message:"User authenticated"})
        }
        else{
            return res.status(404).json({success:false,message:"Password incorrect"})
        }
    }
    else{
        
        return res.status(400).json({success:false,message:"User was not created"})
    }
}

module.exports={createUser,getUser}