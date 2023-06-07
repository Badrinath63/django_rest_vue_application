<template>
 <h1>Register Here</h1>

<div>
    <div class="register">
      <form v-on:submit.prevent="doRegister">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" class="form-control" id="email" v-model="email" />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" class="form-control" id="password" v-model="password" />
        </div>
        <div class="form-group">
          <label for="full_name">Full Name</label>
          <input type="text" class="form-control" id="full_name" v-model="full_name" />
        </div>


        <div class="form-group">
          <button type="submit">Register</button>
        </div>
        {{msg}}
      </form>
    </div>
  </div>



 <h1>Login Here</h1>

<div>
    <div class="login">
      <form v-on:submit.prevent="doLogin">
        <div class="form-group">
          <label for="email1">Email</label>
          <input type="email" class="form-control" id="email1" v-model="email1" />
        </div>
        <div class="form-group">
          <label for="password1">Password</label>
          <input type="password" class="form-control" id="password1" v-model="password1" />
        </div>

        <div class="form-group">
          <button type="submit">Login</button>
        </div>
        {{msg2}}
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
 name: 'UserRegister',
 data() {
    return {
      email: "",
      password: "",
      full_name:"",
      msg:"",
      msg2:"",
      email1:"",
      password1:"",
    };
  },
  methods: {
    async doRegister() {
      try {

        // Send a POST request to the API
        const response = await axios.post("http://127.0.0.1:8000/signup",
          {
            email: this.email,
            password: this.password,
            full_name: this.full_name,
          }
        );
        // Append the returned data to the tasks array

        // Reset the title and description field values.
        this.email = "";
        this.password = "";
        this.full_name="";
         console.log(response.data);

         this.msg = "successfully completed registration";


      } catch (error) {
        // Log the error
         this.msg = "Problem in registration";
        console.log(error);
      }
    },
  async doLogin() {
      try {

        // Send a POST request to the API
        const response = await axios.post("http://127.0.0.1:8000/login",
          {
            email: this.email1,
            password: this.password1,

          }
        );
        // Append the returned data to the tasks array

        // Reset the title and description field values.
        this.email1 = "";
        this.password1 = "";

         console.log(response.data);

        this.msg2 = "login successfully";



      } catch (error) {
        // Log the error
         this.msg2 = "Invalid cred";
        console.log(error);
      }
    },
    },
  created() {
    // Fetch tasks on page load

  },
};
</script>