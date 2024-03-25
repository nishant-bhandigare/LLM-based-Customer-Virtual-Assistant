const { PrismaClient } =require('@prisma/client')
const prisma = new PrismaClient()

const getConversationBySenderId=async(req,res)=>{
    const senderId=req.params.senderId;
    const result=await prisma.chat.findMany({
        where:{
            senderId:senderId
        }
    })
    if(result){
        return res.status(200).json({success:true,result:result})
    }
    else{
        return res.status(404).json({success:false})

    }
    
}



module.exports=getConversationBySenderId