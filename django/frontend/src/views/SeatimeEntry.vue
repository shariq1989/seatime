<template>
    <div class="seatime_entry">
        <SeatimeEntryComponent/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import SeatimeEntryComponent from "../components/SeatimeEntryComponent";

    export default {
        name: 'SeatimeEntry',
        components: {
            SeatimeEntryComponent,
        }
    }
</script>
