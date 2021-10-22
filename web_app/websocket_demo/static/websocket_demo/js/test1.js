/* eslint-disable no-unused-vars */


// // // Without async/await, promises or callbacks
// function getPost() {
//     // console.log('Am inside the async main function!');
//     // let consume = await createPost();
//     console.log('Done!');
// }

// function createPost(){
//     setTimeout(()=> 
//     {
//         console.log('Waiting...');
//     }, 3000);
// }

// createPost();
// getPost();




// // Without async/await using callbacks
function getPost() {
    // console.log('Am inside the getPost function!');
    console.log('Done!');
}

function createPost(callback){
    setTimeout(()=> 
    {
        console.log('Waiting...');
        callback();
    }, 3000);
}

createPost(getPost);




// // // Without async/await using promises
// function getPost() {
//     console.log('Done!');
// }

// function createPost(callback){
//     return new Promise((resolve, reject)=> {
//         setTimeout(()=> 
//         {
//             console.log('Waiting...');
//             const error = false;
//             resolve();
//             // if(!error) {
//             //     resolve();
//             // }
//             // else {
//             //     reject('Error! Something went wrong!')
//             // }
//         }, 3000);
//     })
// }

// createPost().then(getPost);






// // // With async/await using promises
// function getPost() {
//     console.log('Done!');
// }

// function createPost(callback){
//     return new Promise((resolve, reject)=> {
//         setTimeout(()=> 
//         {
//             console.log('Waiting...');
//             resolve();
//             // const error = false;
//             // if(!error) {
//             //     resolve();
//             // }
//             // else {
//             //     reject('Error! Something went wrong!')
//             // }
//         }, 3000);
//     })
// }

// async function TestAsyncAwait() {
//     await createPost();
//     getPost();
// }

// TestAsyncAwait();




// // // With async/await using promises1
// var myTestVar = '';

// function getPost() {
//     console.log('Done!');
// }

// function createPost(callback){
//     return new Promise((resolve, reject)=> {
//         setTimeout(()=> 
//         {
//             console.log('Waiting...');
//             myTestVar = 'Updated'
//             resolve();
//             // const error = false;
//             // if(!error) {
//             //     resolve();
//             // }
//             // else {
//             //     reject('Error! Something went wrong!')
//             // }
//         }, 3000);
//     })
// }

// async function TestAsyncAwait() {
//     await createPost();
//     getPost();
//     console.log(myTestVar);
// }

// TestAsyncAwait();



// // // With async/await using promises 
// // var bookInit = [];
// var bookInit = '';
// function ConnectToWebSocket() {
//     return new Promise((resolve, reject)=> {
//         console.log('Connecting to websockets server..')
//         // // Note that the path doesn't matter for routing; any WebSocket
//         // // connection gets bumped over to WebSocket consumers
//         // var socket = new WebSocket("ws://" + window.location.host + "/chat/");
//         // socket.onmessage = function(event) {
//         // var json_data = JSON.parse(event.data);
//         // // NOTE: We escape JavaScript to prevent XSS attacks.
//         // // bookInit = json_data['codename'];
//         bookInit = 'Updated';
//         // console.log(bookInit);
//         // }
//         // socket.onopen = function() {
//         //     socket.send("echo");
//         // }
//         // // Call onopen directly if socket is already open
//         // if (socket.readyState == WebSocket.OPEN) socket.onopen();
//         resolve();
//     })

// }

// function getValueOfList() {
//     console.log(bookInit);
// }

// // async function AsyncAwait() {
// //    await ConnectToWebSocket();
// //    getValueOfList();
// // }
// // AsyncAwait();

// ConnectToWebSocket().then(getValueOfList);






// // Bringing sleep to native javascript
// // Using Promises
// function sleep(ms) {
//     return new Promise((resolve => setTimeout(resolve, ms)));
// }

// console.log('Sleeping..');
// sleep(3000).then(()=> console.log('Done sleeping..'));



// // Using Date.now() inbuilt function
// function sleep(ms) {
//     const date = Date.now();
//     let currentDate = null;
//     do {
//         currentDate = Date.now();
//     }
//     while (currentDate - date < ms);
// }
// console.log('Sleeping..');
// sleep(10000);
// console.log('Done sleeping..');




// // Checking out Date class
// console.log(new Date())