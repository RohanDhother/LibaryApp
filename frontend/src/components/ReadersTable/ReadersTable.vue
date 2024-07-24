<template>
    <table class="table table-boredred">
        <thead>
            <tr>
                <th>
                    name
                </th>
                <th>
                    email
                </th>
                <th>
                    No. books taken
                </th>
                <th>

                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-bind:key="reader" v-for="reader in readers">
                <td>
                    {{ reader.name }}
                </td>
                <td>
                    {{ reader.email }}
                </td>
                <td>
                    {{ reader.books_count }}
                </td>
                <td>
                    <div v-if="reader.books_count > 0">
                        <button type="button" class="btn btn-primary" data-bs-toggle="modal"
                            v-on:click="selectedReader = reader" data-bs-target="#reader-books-table-model">
                            View Taken Books
                        </button>
                    </div>
                    <div v-else>
                        no books to view
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
    <div class="modal fade" id="reader-books-table-model" tabindex="-1" aria-labelledby="#reader-books-table-model-label"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel" v-if="selectedReader != null">{{ selectedReader.name }}'s Taken Books</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <table class="table table-bordered">
                        <thead>
                            <tr>
                                <th>
                                    title
                                </th>
                                <th>
                                    author
                                </th>
                                <th>
                                    publication date
                                </th>
                            </tr>
                        </thead>
                        <tbody v-if="selectedReader != null">
                            <tr v-bind:key="book" v-for="book in selectedReader.books">
                                <td>
                                    {{ book.title }}
                                </td>
                                <td>
                                    {{ book.author }}
                                </td>
                                <td>
                                    {{ book.publication_date }}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "ReadersTable",
    data: function () {
        return {
            readers: [],
            selectedReader: null
        }
    },
    async mounted() {
        await this.getReaders();
    },
    methods: {
        async getReaders() {
            let response = await fetch("http://127.0.0.1:8000/readers/");
            this.readers = await response.json();
        }
    }
}

</script>