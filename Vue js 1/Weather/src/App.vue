<script>
import axios from 'axios'

export default {
    data() {
        return {
            city: "",
            error: "",
            info: null 
        }
    },
    computed: {
        cityName() {
            return "«" + this.city + "»" // Если нужно вывести название в кавычках,
            // присваиваем значению cityName набор из "«" + this.city + "»"
        },
        showTemp() {
            return "Температура: " + this.info.main.temp
        },
        showFeelsLike() {
            return "Ощущается как: " + this.info.main.feels_like
        },
        showMinTemp() {
            return "Минимальная температура" + this.info.main.temp_min
        },
        showMaxTemp() {
            return "Максимальная температура" + this.info.main.temp_max
        },
    },
    methods: {
        getWeather() {
            if(this.city.trim().length < 2) {
                this.error = 'Нужно название более одного символа :)'
                return false
            }

            this.error = ""

            axios.get(`https://api.openweathermap.org/data/2.5/weather?q=${this.city}&units=metric&appid=b74c739b60f3aed14a5115a0c6966697`)
            .then(res => (this.info = res.data))
        }
    }
}
</script>

<template>
    <div class="wrapper">
    <h1>Погодное приложение </h1>
    <!-- Если хочется вывести название в кавычках, то <p> будет выглядеть так:
         <p>Узнать погоду в {{ city =="" ? "вашем городе" : "«" + city + "»" }}</p> -->
    <p>Узнать погоду в {{ city =="" ? "вашем городе" : cityName }}</p>
    <!-- Варианты введения данных в приложении
         <input type="text" v-on:input="this.city = $event.target.value" || 
        @:input="this.city = $event.target.value" || 
        v-model="city" placeholder="Введите город"> -->
    <input type="text" v-model="city" placeholder="Введите город">

    <!-- Если мы хотим, чтобы кнопка присутсвоваоа постоянно, то прописываем:
         <button>Получить погоду</button>
        А если мы хотим чтобы кнопка исчезала, и появлялась только при заполнении поля, то:  
    <button v-show="city != ''">Получить погоду</button>
    Можно использовать условия v-if, v-else, чтобы отображать кнопки-->
    <button v-if="city != ''" @click="getWeather()">Получить погоду</button>
    <button disabled v-else>Введите название города</button>
    <p class="error"> {{ error }}</p>

    <div v-if="info != null">
        <p>{{ showTemp }}</p>
        <p>{{ showFeelsLike }}</p>
        <p>{{ showMinTemp }}</p>
        <p>{{ showMaxTemp }}</p>
    </div>
</div>
</template>

<style scoped>

.error {
    color: red;
}
.wrapper {
    width: 450px;
    height: 500px;
    border-radius: 50px;
    padding: 20px;
    background: #1f0f24;
    text-align: center;
    color: #fff;
}

.wrapper h1 {
margin-top: 50px;
}

.wrapper p{
margin-top: 20px;
}

.wrapper input{
    margin-top: 30px;
    background: transparent;
    border: 0;
    border-bottom: 2px solid #110813;
    color: #fcfcfc;
    font-size: 14px;
    padding: 5px 8px;
    outline: none;
}

.wrapper input:focus {
    border-bottom-color: greenyellow;
}

.wrapper button:disabled {
    background: #00bfff;
    cursor: not-allowed;
}

.wrapper button {
background: green;
color: #fff;
border-radius: 10px;
border: 2px solid greenyellow;
padding: 10px 15px;
margin-left: 20px;
cursor: pointer;
transition: transform 500ms ease; 
}

.wrapper button:hover {
    transform: scale(1.1) translateY(-5px);
}

</style>
