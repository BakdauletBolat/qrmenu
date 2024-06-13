<template>
  <LoadingComponent :is-loading="isLoading"></LoadingComponent>
  <div v-if="store.store" class="w-full m-auto  min-h-[100vh] bg-[#F4F4F6]">
<!--    <Dialog title="Поиск" v-model="isOpen" >-->
<!--        <div class="container mx-auto flex gap-3"-->
<!--          ><input-->
<!--            v-model="seatchText"-->
<!--            class="w-full p-2.5 px-4 text-sm rounded-sm bg-slate-100 focus:outline-none"-->
<!--            placeholder="Поиск"-->
<!--          />-->
<!--          </div>-->
<!--        <div class="container mx-auto">-->
<!--          <div class="mt-5 flex flex-col gap-4">-->
<!--            <SwitherCard :data="data" v-for="data in searchData"></SwitherCard>-->
<!--          </div>-->
<!--        </div>-->
<!--    </Dialog>-->
    <header class="w-full h-[200px]">
      <div
        class="z-10 relative text-white m-auto container flex-col justify-between h-full !py-5 flex"
      >
        <div class="flex justify-end">
<!--          <button-->
<!--            @click="setIsOpen(true)"-->
<!--            class="p-3 hover:bg-white rounded-xl hover:text-black"-->
<!--          >-->
<!--            <svg-->
<!--              xmlns="http://www.w3.org/2000/svg"-->
<!--              fill="none"-->
<!--              viewBox="0 0 24 24"-->
<!--              stroke-width="1.5"-->
<!--              stroke="currentColor"-->
<!--              class="w-6 h-6"-->
<!--            >-->
<!--              <path-->
<!--                stroke-linecap="round"-->
<!--                stroke-linejoin="round"-->
<!--                d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"-->
<!--              />-->
<!--            </svg>-->
<!--          </button>-->
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
     <div class="grid grid-cols-3 gap-3 px-4 mt-4">
       <CategoryItem @click="navigateTo(category.id)" :item="category" v-for="category in store.store?.categories"></CategoryItem>
    </div>
  </div>
  <div v-else class="min-h-[100vh] flex justify-center items-center flex-col">
    <NotFoundIcon width="100" height="100"></NotFoundIcon>
    <h2 class="text-2xl mt-4">Вы кажется ошиблись адресом, попробуйте другой адрес</h2>
    <div class="bg-slate-700 px-10 cursor-pointer py-3 rounded-xl text-white mt-4" @click="router.back()">
      Назад
    </div>
  </div>
</template>

<script setup lang="ts">
import { store } from "../store";
import { Store, getStore } from "../api/main";
import { onMounted, ref } from "vue";
import {useRoute, useRouter} from "vue-router";
import SwitherCard from "../components/swither-card.vue";
import {ShoppingCartIcon} from "@heroicons/vue/24/outline";
import Dialog from '@/components/Dialog';
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

const loadStore = async (slug: string) => {
  isLoading.value = true;
  try {
    const storeData: Store = (await getStore(slug)).data;
    store.setStore(storeData);
    document.title = store.store?.name ?? "Easy menu";
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
