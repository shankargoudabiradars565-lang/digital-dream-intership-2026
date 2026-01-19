function addTask() {
    let taskInput = document.getElementById("task");
    let taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task");
        return;
    }

    let li = document.createElement("li");

    let span = document.createElement("span");
    span.innerText = taskText;

    let actions = document.createElement("div");
    actions.className = "actions";

    let doneBtn = document.createElement("button");
    doneBtn.innerText = "✔";
    doneBtn.className = "done";
    doneBtn.onclick = () => {
        span.classList.toggle("completed");
    };

    let deleteBtn = document.createElement("button");
    deleteBtn.innerText = "✖";
    deleteBtn.className = "delete";
    deleteBtn.onclick = () => {
        li.remove();
    };

    actions.appendChild(doneBtn);
    actions.appendChild(deleteBtn);

    li.appendChild(span);
    li.appendChild(actions);

    document.getElementById("todoList").appendChild(li);
    taskInput.value = "";
}