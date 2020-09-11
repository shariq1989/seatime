<template>
  <div class="document">
    <DocumentComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import DocumentComponent from "../components/DocumentComponent";

export default {
  name: 'Document',
  components: {
    DocumentComponent,
  }
}
</script>
