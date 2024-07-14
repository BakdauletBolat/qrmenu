<script setup lang="ts">

import {onMounted, ref} from "vue";
import {Category, Food} from "@/api/main.ts";
import {useRoute, useRouter} from "vue-router";
import {instance} from "@/plugins/axios-instance.ts";
import FoodItem from "@/components/FoodItem.vue";
import AppHeaderComponent from "@/components/app-header-component.vue";
import NotFoundIcon from "@/assets/NotFoundIcon.vue";
import LoadingComponent from "@/components/loading-component.vue";

const foods = ref<Food[]>([]);
const category = ref<Category | undefined>(undefined);
const isLoading = ref<boolean>(false);
const route = useRoute();
const router = useRouter();
const loadFoods = () => {
  const categoryId = route.params.categoryId;
  isLoading.value = true;
  instance.get('store/foods/'+categoryId).then(res=>{
    if (res.data.length > 0) {
      foods.value=res.data;
      category.value = res.data[0].category;
    }

  }).catch((e)=>console.log(e)).finally(()=>{
    isLoading.value = false;
  });
}

onMounted(()=>{
  window.scrollTo({
    top:0
  })
  loadFoods();

});

</script>

<template>
  <LoadingComponent :is-loading="isLoading"></LoadingComponent>
  <div class="flex flex-col justify-center items-center min-h-[100vh]" v-if="foods.length < 1">
    <NotFoundIcon width="100" height="100"></NotFoundIcon>
    <h2 class="text-2xl mt-4">Извините, это блюдо временно отсутствует.</h2>
    <div class="primary-background px-10 cursor-pointer py-3 rounded-xl text-white mt-4" @click="router.back()">
      Назад
    </div>
  </div>
  <div v-else>
    <AppHeaderComponent :title="category?.title"></AppHeaderComponent>
  <div class="bg-[#F4F4F6] px-6 pt-4 min-h-[100vh]">
    <div class="grid md:grid-cols-2 gap-4">
    <FoodItem :item="food" v-for="food in foods"></FoodItem>
  </div>
  </div>
  </div>
</template>

<style scoped>

</style>