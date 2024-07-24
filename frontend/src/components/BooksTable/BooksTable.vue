<template>
    <div class="row">
        <div class="row">
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
                        <th>
                            time left on loan
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
                        <td :class="formatTimeLeft(book)">
                            {{ book.timeleft }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="row">
            <p>
                Every book loan lasts 72 hours.
            </p>
        </div>
    </div>
</template>
<script>
import moment from 'moment';
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
            if (!confirm("By taking this book out now, you have started the clock on the book loan. Please return this book within 72 hours.")) {
                document.getElementsByTagName('select')[0].value = "Assign Book";
                return;
            }
            let response = await fetch("http://127.0.0.1:8000/books/" + id + "/", {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(
                    {
                        'reader_id': value,
                        'loan_start_date': moment()

                    })
            });
            if (response.ok) {
                await this.getBooks();
            }
        },
        formatTimeLeft: function (book) {
            if(book.loan_start_date === null){
                book.timeleft = "not";
                return '';
            }
            let timeLeft = this.getTimeLeft(book.loan_start_date);
            book.timeleft = timeLeft;
            if(timeLeft[0] != "-"){
                return 'positive-time-left';
            }
            else{
                return 'negative-time-left';
            }
        },
        getTimeLeft: function (loan_start_date) {
            let loanStartDate = moment(loan_start_date);
            let currentDate = moment();
            let loanEndDate = loanStartDate.add(72, 'hours');
            let duration = moment.duration(loanEndDate.diff(currentDate))
            let days = Math.floor(duration.asDays());
            let hours = Math.floor(duration.asHours() - days * 24);
            let minutes = Math.floor(duration.asMinutes() - days * 24 * 60 - hours * 60);
            let seconds = Math.floor(duration.asSeconds() - days * 24 * 60 * 60 - hours * 60 * 60 - minutes * 60);
            let timeLeft = `${days}d ${hours}h ${minutes}m ${seconds}s`;
            return timeLeft;
        }
    }
}

</script>
<style>
p {
    text-align: left;
}
.positive-time-left {
    color: green !important;
}

.negative-time-left {
    color: red !important;
}
</style>