<template>
  <div class="checklist">
    <ChecklistComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import ChecklistComponent from "../components/ChecklistComponent";

export default {
  name: 'Checklist',
  components: {
    ChecklistComponent,
  }
}
</script>
