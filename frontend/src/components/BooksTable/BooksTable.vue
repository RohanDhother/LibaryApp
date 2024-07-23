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
                    <div v-if="book.taken_by===null">
                        Not assigned
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
    data: function() {
        return {
            books: []
        }
    },
    async mounted() {
        let response = await fetch("http://127.0.0.1:8000/books/");
        this.books = await response.json();
    }
}

</script>