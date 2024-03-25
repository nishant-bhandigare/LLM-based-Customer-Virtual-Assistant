const { PrismaClient } =require('@prisma/client')

const prisma = new PrismaClient()

const saveConversation=async (req,res)=>{
    const {senderId,sender_msg,bot_msg}=req.body
    const result=await prisma.chat.create({
        data:{
            senderId,sender_msg,bot_message:bot_msg
        }
    })
    if(result){
        return res.status(200).json({success:true})
    }
    else{
        return res.status(404).json({success:false})
    }
}

module.exports=saveConversation;