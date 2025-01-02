document.getElementById('add-task-btn').addEventListener('click', addTask);
document.getElementById('task-input').addEventListener('keypress', function(e) {
  if (e.key === 'Enter') {
    addTask();
  }
});

function addTask() {
  const taskInput = document.getElementById('task-input');
  const taskText = taskInput.value.trim();

  if (taskText === '') {
    alert('Por favor, adicione uma tarefa.');
    return;
  }

  const li = document.createElement('li');
  li.innerHTML = `
    <span class="task-text">${taskText}</span>
    <button class="delete-btn">Excluir</button>
  `;

  li.querySelector('.task-text').addEventListener('click', function() {
    li.classList.toggle('completed');
  });

  li.querySelector('.delete-btn').addEventListener('click', function() {
    li.remove();
  });

  document.getElementById('task-list').appendChild(li);
  taskInput.value = '';
}