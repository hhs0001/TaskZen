<!-- src/components/RegisterForm.vue -->
<template>
    <div>
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Registrar</button>
      </form>
    </div>
  </template>
  
  <script>
  import { registerUser } from "../api";
  
  export default {
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      async register() {
        try {
          const user = {
            username: this.username,
            password: this.password,
          };
          const userId = await registerUser(user); // Armazenar o retorno da chamada
          this.$emit('register-success', userId);  // Emitir o userId no evento
        } catch (error) {
          console.error(error);
          alert('Registro falhou');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    font-family: Arial, sans-serif;
  }
  
  h2 {
    color: #333;
    margin-bottom: 1.5rem;
  }
  
  form {
    display: flex;
    flex-direction: column;
    width: 300px;
    padding: 1rem;
    border: 1px solid #e1e1e1;
    border-radius: 5px;
  }
  
  input {
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: none;
    border-radius: 5px;
    border: 1px solid #e1e1e1;
  }
  
  button {
    padding: 0.5rem;
    background-color: #0070f3;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }
  
  button:hover {
    background-color: #0051bb;
  }
  </style>
  
  