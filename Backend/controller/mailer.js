const nodemailer = require('nodemailer');

const sendMail=(req,res)=>{
    const {email}=req.body
    let mailTransporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'shakthtest@gmail.com',
            pass: 'rgid quhp oaob ywgf '
        }
    });
    
    let mailDetails = {
        from: 'organizationk14@gmail.com',
        to: email,
        subject: 'Your ERP need to be verified',
        html:`<h1>Hi,</h1>
        <h1>Your ERP Email Verification OTP :- ${otp}</h1>
        `
    };
    mailTransporter.sendMail(mailDetails, function(err, data) {
        if(err) {
           return res.status(501).json({sucess:'false'})
        } else {

           return res.status(200).json({sucess:'true',message:'Email sent successfully'})
            
        }
    });
}

module.exports=sendMail