import {inject} from 'vue'
import axios from 'axios'
import Cart from './cart_model'


class CartService {

	async get_cart():Promise<any>{
		return new Promise((resolve, reject) => {
			axios.get('carts/')
			.then((resp) => {
				Cart.carts = resp.data
				resolve(resp)
			})
			.catch((err) => {
				if(err.response) {
					console.log(err.response.data)
				}
			})
		})
	}



	async add_cart(schema: any):Promise<any>{
		return new Promise((resolve, reject) => {
			axios.post('carts/', schema)
			.then((resp)=> {
				console.log(resp)
			})
		})
	}

	async update_cart(schema):Promise<any>{
		return new Promise((resolve, reject) => {
			axios.patch(`carts/${schema.id}/`, schema)
			.then((resp) => {
				console.log(resp)
			})
		})
	}


	async remove_cart(schema):Promise<any> {
		return new Promise((resolve, reject) => {
			axios.delete(`carts/${schema.id}/`)
			.then((resp) => {
				const index = this.get_index(schema.id)

				Cart.carts.splice(index, 1)
			})
		})
	}

	get_index(id): number {

		const index = Cart.carts.findIndex(item => item.id == id);

		return index
	}
} 


export default new CartService