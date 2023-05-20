<script setup lang="ts">
</script>

<template>
  <div id="app">
    <header>
      <h1>TaskZen</h1>
    </header>
    <main>
      <login-form v-if="!loggedIn && !showRegister" @login-success="loginSuccess" @go-to-register="showRegister = true" />
      <register-form v-if="!loggedIn && showRegister" @register-success="loginSuccess" @go-to-login="showRegister = false" />
      <div class="task-container" v-if="loggedIn">
        <task-list ref="taskList" />
      </div>
    </main>
  </div>
</template>

<script>
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
import TaskList from "./components/TaskList.vue";

export default {
  components: {
    LoginForm,
    RegisterForm,
    TaskList,
  },
  data() {
    return {
      loggedIn: false,
      showRegister: false,
    };
  },
  methods: {
    loginSuccess(userId) {
    this.loggedIn = true;
    this.$nextTick(() => {
      this.$refs.taskList.loadTasks(userId);
    });
  },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  background-color: #fafafa;
}

.task-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: stretch;
  width: 100%;
  padding: 1rem;
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center; /* modificado de center para flex-start */
}

header {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  background-color: #0070f3;
  padding: 20px 0;
  color: white;
  text-transform: uppercase;
}

h1 {
  margin: 0;
  font-size: 1.5rem;
}

main {
  display: flex;
  flex-direction: column;
  align-items: center; /* modificado de center para flex-start */
  width: 100%;
  padding: 1rem;
  margin-top: 2rem;
}

</style>


