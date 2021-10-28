import {reactive} from 'vue'

interface CategoryType{
	category: String,
}


const CategoryStore = reactive({
	categories: [] as CategoryType[]
})


export default CategoryStore