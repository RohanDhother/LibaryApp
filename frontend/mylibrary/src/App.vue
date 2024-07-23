<template>
  <h1>
    Library App
  </h1>
  <div class="row">
    <div class="col-md-6 m-3">
      <BooksTable />
    </div>
  </div>
</template>

<script>
import BooksTable from "./components/BooksTable/BooksTable.vue";

export default {
  name: "App",
  components: {
    BooksTable
  },
  async mounted() {
    console.log("test");
    let response = await fetch("http://127.0.0.1:8000/books/");
    const data = await response.json();
    console.log("data:", data);
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
