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
} 


export default new CartService