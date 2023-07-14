// async function postData(url = "", data = {}) {
//    // Default options are marked with *
//    const response = await fetch(url, {
//      method: "POST", // *GET, POST, PUT, DELETE, etc.
//      headers: {
//        "Content-Type": "application/json",
//      },
   
//      body: JSON.stringify(data), // body data type must match "Content-Type" header
//    });
//    return response.json(); // parses JSON response into native JavaScript objects
//  }
 
//  postData("https://example.com/answer", { answer: 42 }).then((data) => {
//    console.log(data); // JSON data parsed by `data.json()` call
//  });






// document.querySelector('#send').addEventListener('click',
// async function (){
//    document.querySelector('.right').style.display='none'
//    document.querySelector('.right2').style.display='block'
//    questioninput= document.getElementById('questioninput').value
//    document.getElementById('questioninput').value=''
//    document.getElementById('question1').innerHTML=questioninput
   
//    result= await postData('/api',{"question":questioninput})
//    answer.innerHTML=result.answer
//    console.log(result.answer)
// })
async function postData(url = "", data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}
//  postData("https://example.com/answer", { answer: 42 }).then((data) => {
//    console.log(data); // JSON data parsed by `data.json()` call
//  });

 


 



document.querySelector("#send").addEventListener("click",async()=>{
  document.querySelector(".right").style.display="none";
  document.querySelector(".right2").style.display="block";
  questioninput=document.querySelector("#questioninput").value;
  document.querySelector("#questioninput").style.display="";
  document.getElementById("question1").innerHTML=questioninput;
  console.log("sab badhiya hai")


//  result= await postData("/api", { 'question': questioninput }).then((data) => {
//   document.getElementById("answer").innerHTML=result.answer;
//   console.log(result.answer)
// })

   result= await postData('/api',{"question":questioninput})
   answer.innerHTML=result.answer
   console.log(result.answer)

  
})
;