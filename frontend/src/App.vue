<script setup lang="ts">
</script>

<template>
  <div id="app">
    <header>
      <h1>TaskZen</h1>
    </header>
    <main>
      <task-list></task-list>
    </main>
  </div>
</template>


<script>
import TaskList from "./components/TaskList.vue";

export default {
  components: {
    TaskList,
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f0f0f0;
}

header {
  background-color: #4caf50;
  padding: 1rem 2rem;
  color: white;
}

main {
  padding: 2rem;
}
</style>
