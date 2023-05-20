const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
let todos = [];

todoForm.addEventListener("submit", submitAddTodo);

function deleteTodo(event) {
  const li = event.target.parentElement;
  li.remove();
  todos = todos.filter((todo) => todo.id !== parseInt(li.id));
  saveTodos();
}

function paintTodo(newTodo) {
  const li = document.createElement('li');
  li.id = newTodo.id;
  li.innerHTML = `<span>${newTodo.text}</span><button>X</button>`;
  li.querySelector('button').addEventListener("click", deleteTodo);
  todoList.appendChild(li);
}

function submitAddTodo(event) {
  event.preventDefault();
  const content = document.getElementById("content");
  const newTodo = { text: content.value, id: Date.now() };
  todos.push(newTodo);
  saveTodos();
  content.value = "";
  paintTodo(newTodo);
}

function saveTodos() {
  window.localStorage.setItem('todo', JSON.stringify(todos));
}

todos = JSON.parse(localStorage.getItem('todo')) || [];
todos.forEach(paintTodo);