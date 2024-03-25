const { PrismaClient } =require('@prisma/client')

const prisma = new PrismaClient()

const saveUser=async(req,res)=>{
    const {name,phoneno,address,problem_detail,nature_of_issue,date}=req.body
    
   
    const result=await prisma.user.create({
        data:{
            name,phoneno,address,problem_detail,nature_of_issue,date
        }
    })
    if(result){
        return res.status(200).json({success:true,id:result.id})
    }else{
        return res.status(400).json({success:false})
    }
}

module.exports=saveUser