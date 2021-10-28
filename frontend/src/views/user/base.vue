<script>
import { defineAsyncComponent, onBeforeMount, onMounted, ref } from 'vue';


const Navigation = defineAsyncComponent({
  loader: () => import('@/components/navigation/Navigation.vue')
})



export default {
  components: {
    Navigation,

  },
  setup(){

    const scrolled = ref(null);

    onMounted(() => {
      window.addEventListener('scroll', function(e) {

        scrolled.value = window.scrollY
      
      })
    })

    return {
      scrolled
    }
  }
}

</script>

<template>
	<div>
		 <div :class="[scrolled ? 'shadow-md' : '']"  class=" fixed z-20 bg-white top-0 h-16 transition-all duration-300  w-full">
		      <Navigation >
		      
		     </Navigation>
    	</div>
    
    
    	<div class="transition-all mt-16 duration-300 lg:px-12 ">
         
	       <router-view>
	        
	       </router-view>
    	</div>
	</div>
</template>