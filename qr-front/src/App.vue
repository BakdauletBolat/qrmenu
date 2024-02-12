<template>
  <Dialog :open="isOpen" @close="setIsOpen">
    <DialogPanel class="fixed overflow-y-scroll p-3 pt-6 z-40 h-[100vh] top-0 bg-white w-full">
      <DialogTitle class="container mx-auto flex gap-3"
        ><input
          v-model="seatchText"
          class="w-full p-2.5 px-4 text-sm rounded-sm bg-slate-100 focus:outline-none"
          placeholder="Поиск"
        />
        <button @click="setIsOpen(false)">Закрыть</button></DialogTitle
      >
      <div class="container mx-auto">
        <div class="mt-5 flex flex-col gap-4">
          <SwitherCard :data="data" v-for="data in searchData"></SwitherCard>
        </div>
      </div>
    </DialogPanel>
  </Dialog>
  <header class="w-full h-[200px]">
    <div
      class="z-10 relative text-white m-auto container flex-col justify-between h-full !py-5 flex"
    >
      <div class="flex justify-end">
        <button
          @click="setIsOpen(true)"
          class="p-3 hover:bg-white rounded-xl hover:text-black"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
            />
          </svg>
        </button>
      </div>
      <div>
        <h2 class="text-3xl font-bold">{{ store.store?.name }}</h2>
        <p class="text-xl mt-1 font-normal text-slate-300">
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
  <router-view> </router-view>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { store } from "./store";
import { Store, getStore } from "./api/main";
import { ref, computed } from "vue";
import { Dialog, DialogPanel, DialogTitle } from "@headlessui/vue";
import SwitherCard from "./components/swither-card.vue";
const isOpen = ref(false);

function setIsOpen(value: boolean) {
  isOpen.value = value;
}

const seatchText = ref('');
const searchData = computed(() => {
  const data: any = [];
  let lower = seatchText.value.toLowerCase();
  store.store?.categories.forEach((category) => {
    category.foods.forEach((food) => {
      if (food.name.toLowerCase().includes(lower)) {
        data.push(food);
      }
    });
  });
  store.store?.categories.forEach((category)=>{
    if (category.title.toLowerCase().includes(lower)) {
      if (category.foods.length != 0) {
        data.push(category);
      }
      
    }
  })

  return data;
})

const slug = "random";
const loadStore = async () => {
  const storeData: Store = (await getStore(slug)).data;
  store.setStore(storeData);
};
onMounted(() => {
  loadStore();
});
</script>
