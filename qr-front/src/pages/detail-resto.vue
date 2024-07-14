<template>
  <LoadingComponent :is-loading="isLoading"></LoadingComponent>
  <div v-if="store.store" class="w-full m-auto  min-h-[100vh] bg-[#F4F4F6]">
    <header class="w-full h-[200px]">
      <div class="z-10 relative text-white m-auto container flex-col justify-between h-full !py-5 flex">
        <div class="flex justify-end">
          <button @click="cardStorage.isActive.value = true" class="p-3 hover:bg-white rounded-xl hover:text-black">
            <ShoppingCartIcon class="w-6 h-6"></ShoppingCartIcon>
          </button>
        </div>
        <div>
          <h2 class="text-xl font-bold">{{ store.store?.name }}</h2>
          <p class="mt-1 font-normal text-slate-300">
            {{ store.store?.address }}
          </p>
        </div>
      </div>
      <img
        class="top-0 absolute w-full h-[200px] object-cover"
        :src="store.store?.image"
        alt=""
      />
      <div class="top-0 absolute w-full h-[200px] gradient-black"></div>
    </header>
     <div class="grid grid-cols-1 gap-3 px-4 mt-4"
     :class="{
       'lg:grid-cols-3': store.store.params?.adaptive
     }">
       <CategoryItem @click="navigateTo(category.id)" :item="category" v-for="category in store.store?.categories"></CategoryItem>
    </div>
  </div>
  <div v-else class="min-h-[100vh] flex justify-center items-center flex-col">
    <NotFoundIcon width="100" height="100"></NotFoundIcon>
    <h2 class="text-2xl mt-4">Вы кажется ошиблись адресом, попробуйте другой адрес</h2>
    <div class="primary-background px-10 cursor-pointer py-3 rounded-xl text-white mt-4" @click="router.back()">
      Назад
    </div>
  </div>
</template>

<script setup lang="ts">
import { store } from "../store";
import { Store, getStore } from "../api/main";
import { onMounted, ref } from "vue";
import {useRoute, useRouter} from "vue-router";
import {ShoppingCartIcon} from "@heroicons/vue/24/outline";
import {CardStorage} from "@/storages/card-storage.ts";
import CategoryItem from "@/components/CategoryItem.vue";
import LoadingComponent from "@/components/loading-component.vue";
import NotFoundIcon from "@/assets/NotFoundIcon.vue";


const cardStorage = CardStorage.getInstance();


const isOpen = ref(false);

function setIsOpen(value: boolean) {
  isOpen.value = value;
}

// const seatchText = ref("");
// const searchData = computed(() => {
//   const data: any = [];
//   let lower = seatchText.value.toLowerCase();
//   store.store?.categories.forEach((category) => {
//     category.foods.forEach((food) => {
//       if (food.name.toLowerCase().includes(lower)) {
//         data.push(food);
//       }
//     });
//   });
//   store.store?.categories.forEach((category) => {
//     if (category.title.toLowerCase().includes(lower)) {
//       if (category.foods.length != 0) {
//         data.push(category);
//       }
//     }
//   });
//
//   return data;
// });

const route = useRoute();
const router = useRouter();
const isLoading = ref(false);

function setParams(store: Store) {
  const root = document.documentElement;
      console.log(store.params.mainColor)
  if (store.params.mainColor != undefined) {

      root.style.setProperty('--main-color', store.params.mainColor);
  }

}

const loadStore = async (slug: string) => {
  isLoading.value = true;
  try {
    const storeData: Store = (await getStore(slug)).data;
    store.setStore(storeData);
    document.title = store.store?.name ?? "Easy menu";
    setParams(store.store);
  } finally {
    isLoading.value = false;
  }
};
onMounted(() => {
  const slug = route.params.slug.toString();
  loadStore(slug);
});

const navigateTo = (id: number) => {
  router.push({
    name: 'foods',
    params: {
      categoryId: id
    }
  })
}
</script>
