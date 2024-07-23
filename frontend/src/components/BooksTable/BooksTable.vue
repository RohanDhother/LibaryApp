<template>
    <table class="table table-boredred">
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
                <th>
                    taken by
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-bind:key="book" v-for="book in books">
                <td>
                    {{ book.title }}
                </td>
                <td>
                    {{ book.author }}
                </td>
                <td>
                    {{ book.publication_date }}
                </td>
                <td>
                    <div v-if="book.taken_by === null">
                        <select class="form-select" @change="(event) => selectReader(book.id, event.target.value)">
                            <option :value="null">Assign Book</option>
                            <option v-bind:key="reader" v-for="reader in readers" :value="reader.id">
                                {{ reader.name }}
                            </option>
                        </select>
                    </div>
                    <div v-else>
                        {{ book.taken_by }}
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
</template>
<script>
export default {
    name: "BooksTable",
    data: function () {
        return {
            books: [],
            readers: [],
            selectedReader: null
        }
    },
    async mounted() {
        await this.getBooks();
        await this.getReaderNames();
    },
    methods: {
        async getBooks() {
            let response = await fetch("http://127.0.0.1:8000/books/");
            this.books = await response.json();
        },
        async getReaderNames() {
            let response = await fetch("http://127.0.0.1:8000/reader_names/");
            this.readers = await response.json();
        },
        async selectReader(id, value) {
            let response = await fetch("http://127.0.0.1:8000/books/"+id+"/", {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'reader_id': value })
            });
            if(response.ok){
                await this.getBooks();
            }
        }
    }
}

</script>