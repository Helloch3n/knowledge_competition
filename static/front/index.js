new Vue({
    el: '#app',
    data: {
        questions: [],
        selected: {
            0: null,
            1: null,
            2: null,
            3: null,
            4: null,
            5: null,
            6: null,
            7: null,
            8: null,
            9: null,
        }
    },
    methods: {
        changeSelected(selected, index) {
            this.selected[index] = selected
        },
        submitAnswers() {
            // 将用户选择的答案发送到后台;
            // axios.defaults.headers.common["X-CSRFToken"] = "{{ csrf_token() }}";
            axios.post('/result/', {
                selected: this.selected
            })
                .then(function (response) {
                    var status = response.data.status;
                    // alert(status)
                    if (status == 'success') {
                        window.location.href = '/score/'
                    } else {
                        alert("Error!")
                    }
                })
                .catch(function (error) {
                    alert("Error!");
                });
        }
    }
    ,
    created() {
// 发送 ajax 请求
        axios.get('/question/').then(response => {
            // console.log(response.data) // 得到返回结果数据
            this.questions = response.data
        }).catch(error => {
            console.log(error.message)
        })
    },
})