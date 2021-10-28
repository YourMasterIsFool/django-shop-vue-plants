
import {reactive} from 'vue'

interface ProductModel {
	product_name: String,
	category: String,
	gender: String,
	type: String,
	description: String,
	price: Float,
	date: String
}

const ProductStore = reactive({
	products: [] as ProductModel[]
})

export  {
	ProductStore
}