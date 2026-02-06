const form = document.getElementById("todo-form");
const input = document.getElementById("todo-input");
const list = document.getElementById("todo-list");

const STORAGE_KEY = "todos";

document.addEventListener("DOMContentLoaded", loadTodos);

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const title = input.value.trim();
    if (!title) return;

    const todos = getTodos();
    todos.push({ title });

    saveTodos(todos);
    renderTodos(todos);

    input.value = "";
});

function getTodos() {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
}

function saveTodos(todos) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
}

function loadTodos() {
    renderTodos(getTodos());
}

function renderTodos(todos) {
    list.innerHTML = "";

    todos.forEach((todo, index) => {
        const li = document.createElement("li");
        li.textContent = todo.title;

        const btn = document.createElement("button");
        btn.textContent = "❌";
        btn.onclick = () => deleteTodo(index);

        li.appendChild(btn);
        list.appendChild(li);
    });
}

function deleteTodo(index) {
    const todos = getTodos();
    todos.splice(index, 1);
    saveTodos(todos);
    renderTodos(todos);
}
