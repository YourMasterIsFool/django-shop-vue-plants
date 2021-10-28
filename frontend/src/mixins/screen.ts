import {ref, onMounted} from 'vue'


const width = ref<Number>(screen.width);


function getSizeScreen(){
	width.value = window.innerWidth
}

window.onresize = getSizeScreen
window.onload = getSizeScreen
	


export {
	width
}