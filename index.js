const express = require('express');
const mongoose = require('mongoose');


const app = express();
app.use(express.json());

mongoose.connect("mongodb://127.0.0.1:27017/Recipe").then(()=>console.log("success connected")).catch((err)=>console.log("error"))

const recipeSchema = new mongoose.Schema({ 
    title: String,
    description: String
  });

  const Recipee = mongoose.model('recipeCollection', recipeSchema);


  app.get("/recipes", async (req, resp)=>{
    let data = await Recipee.find();
    resp.send(data);
  })

  app.post('/create', async (req, resp)=>{

      let data = new  Recipee(req.body);
      let result = await data.save();
      console.log(result);
      resp.send(result);
      
  });

  app.delete("/delete/:_id", async (req, resp)=>{

    console.log(req.params);
    let data = await Recipee.deleteOne(req.params);
    resp.send("Done");
  })

  

  app.listen(5000);