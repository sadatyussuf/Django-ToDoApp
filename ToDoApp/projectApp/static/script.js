// let done = document.querySelectorAll('.done')
// let undo = document.querySelectorAll('.undo-icon')
// let texts = document.querySelectorAll('.todo-text')

let boxes = document.querySelectorAll('.todoBox')

boxes.forEach( box => {
// console.log(box)
const done = box.querySelector('.done')
const text = box.querySelector('.todo-text')
const undo = box.querySelector('.undo-icon')
// console.log(done)
done.addEventListener('click',() => {
    text.style.textDecoration = 'line-through'
})

undo.addEventListener('click',() => {
    text.style.textDecoration = 'none'
})

})













// console.log(texts)
// done.forEach(btn => {
//     btn.addEventListener('click',(e) => {
//         current = e.target
//         console.log(current)
//     texts.forEach(text => {
//         console.log(text)
//     })
//     // text.innerText.style.textDecoration = 'line-through'
//         console.log("I am here")
//     })
// })
