<template>
  <div>
    <h2>Lista de Tarefas</h2>
    <form @submit.prevent="addTask">
      <input type="text" v-model="newTask" placeholder="Digite uma nova tarefa" required />
      <button type="submit">Adicionar</button>
    </form>
    <ul>
  <li v-for="task in tasks" :key="task._id">
    <div class="task-description">
      {{ task.description }}
    </div>
    <div class="task-actions">
      <button @click="deleteTask(task._id)">Excluir</button>
      <button @click="showUpdateTaskForm(task)">Atualizar</button>
    </div>
    <div v-if="taskBeingEdited && taskBeingEdited._id === task._id">
      <h3>Editar Tarefa</h3>
      <form @submit.prevent="updateTaskAndHideForm">
        <input type="text" v-model="taskBeingEdited.description" required />
        <button type="submit">Salvar</button>
        <button type="button" @click="taskBeingEdited = null">Cancelar</button>
      </form>
    </div>
  </li>
</ul>

  </div>
</template>

<script>
import { getTasks, createTask, updateTask, deleteTask } from "../api";

export default {
  data() {
    return {
      tasks: [],
      newTask: "",
      taskBeingEdited: null,
      userId: null,
    };
  },
  methods: {
    async loadTasks(userId) {
      this.userId = userId;
      this.tasks = await getTasks(userId);
    },
    async addTask() {
      const task = {
        description: this.newTask,
        done: false,
      };
      const createdTask = await createTask(task, this.userId);
      this.tasks.push(createdTask);
      this.newTask = "";
    },
    async deleteTask(taskId) {
      await deleteTask(taskId);
      this.tasks = this.tasks.filter((task) => task._id !== taskId);
    },
    showUpdateTaskForm(task) {
      this.taskBeingEdited = task;
  },
    async updateTaskAndHideForm() {
      await updateTask(this.taskBeingEdited._id, this.taskBeingEdited);
      this.taskBeingEdited = null;
  },
  },
};
</script>

<!-- Add your scoped styles here -->

  
<style scoped>
* {
  box-sizing: border-box;
}

div {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;   /* aumentado de 1rem para 2rem */
  font-family: Arial, sans-serif;
  width: 100%;
}

h2, h3 {
  color: #333;
  margin-bottom: 1rem;  /* adicionado para dar espaço entre o título e o formulário abaixo */
}

form {
  display: flex;
  flex-direction: column; /* Adiciona isso para tornar o formulário de edição vertical */
  width: 75%;
  margin-bottom: 1rem;
}

input {
  flex-grow: 1;
  padding: 0.5rem;
  margin-bottom: 0.5rem; /* Adiciona isso para dar espaço entre os elementos do formulário */
  border: none;
  border-radius: 5px;
}

input {
  flex-grow: 1;
  padding: 0.6rem 0.5rem; /* Adicione um pouco mais de padding vertical */
  margin-bottom: 0.5rem; /* Adiciona isso para dar espaço entre os elementos do formulário */
  border: none;
  border-radius: 5px;
}

button {
  padding: 0.5rem 1rem;
  background-color: #0070f3;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 0.5rem;
}

button:hover {
  background-color: #0051bb;
}

ul {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding: 0;
  justify-content: start;
  align-items: flex-start; /* adicione esta linha */
  width: 100%;
  gap: 1rem;
}

li {
  display: flex;
  flex-direction: column;
  background-color: #f0f0f0;
  padding: 1rem;
  border-radius: 5px;
  margin-bottom: 1.5rem;
  flex-basis: calc(25% - 1rem); /* faz com que a task ocupe um terço da largura total, descontando a margem */
}

.task-description {
  margin-bottom: 0.25rem;
}

.task-actions {
  display: flex;   
  flex-direction: row;  
  justify-content: center; /* Centraliza os botões */
  gap: 0.5rem;  
}

li:nth-child(3n) {
  margin-right: 0; /* Remove a margem direita da terceira task de cada linha para evitar espaçamento extra no final da linha */
}

li:nth-child(odd) {
  background-color: #e6e6e6;
}

</style>

