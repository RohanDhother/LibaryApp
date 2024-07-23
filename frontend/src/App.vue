<template>
  <div class="container">
    <div class="row">
      <div class="row">
        <h1>
          Library App
        </h1>
      </div>
      <div class="row mt-4">
        <div class="col-md-6">
          <BooksTable />
        </div>
        <div class="col-md-6">
          <ReadersTable />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BooksTable from "./components/BooksTable/BooksTable.vue";
import ReadersTable from "./components/ReadersTable/ReadersTable.vue";

export default {
  name: "App",
  components: {
    BooksTable,
    ReadersTable
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
