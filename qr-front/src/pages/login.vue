<template>
  <div class="max-w-[400px] h-[100vh] flex items-center justify-center mx-auto">
    <div>
      <h1 class="text-2xl">Чтобы сканировать войдите 🍕</h1>
      <div class="flex flex-col gap-3 mt-4">
        <input v-model="form.username" class="focus:outline-0 p-3 border rounded-sm" placeholder="Имя пользователя" />
        <input v-model="form.password" type="password" class="focus:outline-0 p-3 border rounded-sm"  placeholder="Пароль" />
        <button @click="login" class="rounded-sm hover:bg-orange-500 bg-orange-400 p-3 text-white" :class="{
          'bg-slate-400 hover:bg-slate-500': isLoading
        }" :disabled="isLoading">
          {{isLoading ? 'Загрузка': 'Войти'}}
        </button>
        {{errorMessage}}
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import {reactive, ref} from "vue";
import {instance} from "../plugins/axios-instance.ts";
import {useRouter, useRoute} from "vue-router";

const isLoading = ref(false);
const errorMessage = ref('');
const form = reactive({
  username: '',
  password: ''
});

const router = useRouter();
const route = useRoute();
const login = async () => {
  isLoading.value = true;
  console.log(route.query);
  try {
    const res = await instance.post('/token/', {
      'username': form.username,
      'password': form.password
    });
    localStorage.setItem('token', res.data.access);
    errorMessage.value = '';
    await router.push(route.query.redirect?.toString() ?? '');
  }
  catch (e) {
    errorMessage.value = e!.toString();
  }
  finally {
    isLoading.value = false;
  }
}
</script>