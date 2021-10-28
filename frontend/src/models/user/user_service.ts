import axios from 'axios'
import User from './user_model'

class UserService{
	get_profile():Promise<any>{
		return new Promise((resolve, reject) => {
			axios.get('users/me/')
			.then((response) => {
				User.user = response.data			
			})
		})
	}



	update_profile(schema: any):Promise<any>{
		return new Promise((resolve, reject) => {
			axios.post('users/update_profile')
			.then((response) => {
				console.log(response.data)
			})
			.catch((err) => {
				console.log(err)
			})
		})
	}


	register(schema:any):Promise<any>{
		// console.log(schema)
		return new Promise((resolve,reject) => {
			axios.post('auth/users/', schema)
			.then((resp) => {
				 console.log(resp);
				 resolve(resp)
			})
			.catch((err) => {
				reject(err)
			})
		})
	}
}


export default new UserService