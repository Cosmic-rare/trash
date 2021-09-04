var app = new Vue({
  el: '#app',
  data: {
    count: 0,
    msg: "Hello Vue.js!",
    num: 0,

	  frameworks: [
		{ name: 'Vue', creator: 'Evan You', stars: 79760 },
		{ name: 'React', creator: 'Facebook', stars: 85623 },
		{ name: 'Angular', creator: 'Google', stars: 31976 },
	  ],

	  frame: "vue"
  },
  methods: {
  	countup: function() {
  		this.count += 3
  	},
	  
  	crear: function() {
  		this.count = 0;
  	}
  }
})
