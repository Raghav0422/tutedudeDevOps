
var express =require('express');
var app = express();

app.set('view engine', 'ejs');

const URL = process.env.BACKEND_URL || 'http://localhost:5000/submit'

// const fetch =(...args)=>
//     import ('node-fetch').then(({default: fetch})=>fetch(...args));
// above line is replaced with below line
const fetch=global.fetch

// app.use(express.static(path.join(__dirname,'public')));

app.get('/submit', async function(req,res){
    // res.sendFile(path.join(__dirname+'/public/index.html'));
    const options={
        method: 'GET'
    };
    fetch(URL,options)
        .then(res=>res.json())
        .then(json=>console.log(json))
        .catch(err=>console.error('error: '+err));
    try{
        let response = await fetch(URL,options);
        response = await response.json()
        res.render('index',response)
    }catch(err){
        console.log(err);
        res.status(500).json({msg:`Internal Server Error.`});
    }
});

app.listen(3000,function(){
    console.log('Ares listinig on port 3000!')
})