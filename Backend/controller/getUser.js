const { PrismaClient } =require('@prisma/client')
const prisma = new PrismaClient()

const getUser=async(req,res)=>{
    try {
        const result=await prisma.user.findMany()
        return res.status(200).json({success:true,result})
    } catch (error) {
        return res.status(400).json({success:false,message:"Internal Server Error"})
    }
}

module.exports=getUser