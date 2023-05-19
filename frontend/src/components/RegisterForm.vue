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
  form {
    display: flex;
    flex-direction: column;
    width: 300px;
    margin: 0 auto;
  }
  
  input, button {
    margin-bottom: 1rem;
  }
  </style>
  