<template>
  <div>
    <h2>Lista de Tarefas</h2>
    <form @submit.prevent="addTask">
      <input type="text" v-model="newTask" placeholder="Digite uma nova tarefa" required />
      <button type="submit">Adicionar</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task._id">
        {{ task.description }}
        <button @click="deleteTask(task._id)">Excluir</button>
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
    };
  },
  async created() {
    this.tasks = await getTasks();
  },
  methods: {
    async addTask() {
      const task = {
        description: this.newTask,
        done: false,
      };
      const createdTask = await createTask(task);
      this.tasks.push(createdTask);
      this.newTask = "";
    },
    async deleteTask(taskId) {
      await deleteTask(taskId);
      this.tasks = this.tasks.filter((task) => task._id !== taskId);
    },
  },
};
</script>

<!-- Add your scoped styles here -->

  
  <style scoped>
  form {
    display: flex;
    margin-bottom: 1rem;
  }
  
  input {
    flex-grow: 1;
    padding: 0.5rem;
    margin-right: 0.5rem;
  }
  
  button {
    padding: 0.5rem;
    background-color: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #3d8b40;
  }
  
  li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
  }
  
  li:nth-child(odd) {
    background-color: #f9f9f9;
  }
  </style>
  