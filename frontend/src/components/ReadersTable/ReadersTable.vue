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
                    books taken
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
                </td>
            </tr>
        </tbody>
    </table>
</template>
<script>
export default {
    name: "ReadersTable",
    data: function() {
        return {
            readers: []
        }
    },
    async mounted() {
        let response = await fetch("http://127.0.0.1:8000/readers/");
        this.readers = await response.json();
    }
}

</script>