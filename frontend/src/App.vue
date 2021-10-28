<script lang="ts">
import { defineAsyncComponent, onBeforeMount, onMounted, ref } from 'vue';


export default {
  components: {
  
  },
  setup(){

  }
}

</script>

<template>
  <div class="relative bg-white text-black">
    <div class="transition-all duration-300 ">
         
       <router-view>
        
       </router-view>
    </div>
   
  </div>
</template>
<style type="scss">
   
</style>