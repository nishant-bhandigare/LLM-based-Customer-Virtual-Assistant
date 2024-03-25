const bcrypt=require('bcryptjs');

const hashPassword=async(password)=>{
    const salt=await bcrypt.genSalt(10);
    const secPass=await bcrypt.hash(password,salt);
    return secPass;
}

const comparePassword=async(password,userPassword)=>{
    const result=await bcrypt.compare(password,userPassword)
    return result
}

module.exports={hashPassword,comparePassword}