import axios from 'axios'

class ProductService {

	async addProduct(schema: any):Promise<any> {
		console.log(schema)

		return new Promise((resolve, reject) => {
			axios.post('products/', schema)
			.then((resp) => {
				resolve(resp)
			})
			.catch((err) => {
				console.log(err.response.data)
			})
		})
	}


	async get_all():Promise<any> {
		return new Promise((resolve, reject) => {
			axios.get('products/')
			.then((resp) => {
				resolve(resp)
			})
			.catch((err) => {
				console.log(err.response.data)
			})
		})
	}

	async get_count():Promise<any>{
		return new Promise((resolve, reject) => {
			axios.get('products/get_count/')
			.then((resp) => {
				resolve(resp)
			})
		})
	}
}

export default new ProductService