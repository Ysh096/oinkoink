# README

새로 알게 된 것들 정리!



## 1. naturaltime (N분 전 표시)

django는 humanize라는 앱이 이미 깔려 있지만 비활성화 상태이다. created_at 같은 걸로 시간을 나타낼 때 sep 9, pm 6:48 이런 식으로 나타내는게 아니라 몇 분 전, 몇 시간 전 이런 식으로 나타내고 싶다면 이 humanize 앱을 활성화하고 naturaltime 필터를 이용하면 된다.

1. settings.py의 installed_app에 django.contrib.humanize 추가

2. 사용을 원하는 html 페이지에서 load humanize

3. 다음과 같이 필터 적용

   ```html
   <p class="info">{{ oink.created_at|naturaltime }}</p>
   ```

   

## 2. django를 베이스로 Vue 적용하기

1. base.html에 vue cdn 적용(아니면 그냥 사용하려는 html 페이지에서 적용해도 됨)

`<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`

3. base.html에 적용한 경우 block 생성해서 다른 템플릿에서 쓸 수 있게 만들기

   ```html
   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
   {% block script %}
   {% endblock script %}
   ```

4. 이제 사용하고자 하는 템플릿에서 block 안에 vue 문법 적용

   ```vue
   {% block script %}
   <script>
     new Vue({
       el: '#feedapp',
       delimiters: ['[[', ']]'],
       data () {
         return {
           oinks: [],
           body: '',
           oinker: '{{ request.user.username }}',
           created_at: 'Now',
         }
       },
       methods: {
         submitOink() {
           console.log('submitOink');
   
           if (this.body.length > 0) {
             var oink = {
               'body': this.body,
               'oinker': this.oinker,
               'created_at': this.created_at
             };
   
             this.oinks.unshift(oink);
   
             // send to backend
             fetch('/api/add_oink/', {
               method: 'POST',
               headers: {
                 'Content-Type': 'application/json',
                 'X-CSRFToken': '{{ csrf_token }}'
               },
               credentials: 'same-origin',
               body: JSON.stringify(oink)
             })
             .then((response) => {
               console.log(response)
             })
             .catch((error) => {
               console.log(error)
             })
           }
           this.body = ''
         }
       }
     })
   </script>
   {% endblock script %}
   ```

   이렇게 작성하면 data에 있는 내용은 화면을 새로고침 하지 않아도 갱신된다.

