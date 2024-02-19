<template>
  <div
    class="w-full h-[50vh] flex justify-center items-center"
    v-if="isLoading"
  >
    <svg
      class="w-[200px]"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 300 150"
    >
      <path
        fill="none"
        stroke="#FB923C"
        stroke-width="15"
        stroke-linecap="round"
        stroke-dasharray="300 385"
        stroke-dashoffset="0"
        d="M275 75c0 31-27 50-50 50-58 0-92-100-150-100-28 0-50 22-50 50s23 50 50 50c58 0 92-100 150-100 24 0 50 19 50 50Z"
      >
        <animate
          attributeName="stroke-dashoffset"
          calcMode="spline"
          dur="2"
          values="685;-685"
          keySplines="0 0 1 1"
          repeatCount="indefinite"
        ></animate>
      </path>
    </svg>
  </div>

  <div v-else class="w-full m-auto">
    <Dialog :open="isOpen" @close="setIsOpen">
      <DialogPanel
        class="fixed overflow-y-scroll p-3 pt-6 z-40 h-[100vh] top-0 bg-white w-full"
      >
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
    <TabGroup v-if="store.store">
      <TabList
        class="!pr-[0px] container mx-auto flex w-auto gap-3 sticky top-0 z-20 bg-white !py-4 overflow-x-auto"
      >
        <Tab
          v-for="category in store.store?.categories"
          as="template"
          :key="category.id"
          v-slot="{ selected }"
        >
          <button
            :class="[
              'p-2.5 px-4 whitespace-nowrap text-sm rounded-sm bg-slate-100 focus:outline-none',
              selected ? 'text-white !bg-orange-400' : 'text-black',
            ]"
          >
            {{ category.title }}
          </button>
        </Tab>
      </TabList>

      <TabPanels class="container mx-auto">
        <TabPanel
          v-for="category in store.store?.categories"
          :key="category.id"
        >
          <div v-if="!category.foods.length">Нету блюд</div>
          <ul class="food-list gap-3">
            <li
              v-for="food in category.foods"
              :key="food.name"
              class="relative rounded hover:cursor-pointer"
            >
              <img
                class="w-full h-[250px] rounded-lg object-cover"
                :src="food.images.length > 0 ? food.images[0].image : 'https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ='"
              />
              <div class="py-4 px-1 mt-2 gap-6 flex justify-between">
                <div>
                  <h3
                    class="font-medium text-xl leading-5 shantell-sans-regular text-orange-400"
                  >
                    {{ food.name }}
                  </h3>
                  <li class="mt-2 text-xs font-normal leading-4 text-gray-500">
                    {{ food.description }}
                  </li>
                </div>
                <div class="flex flex-col gap-1 items-center">
                  <p
                    class="whitespace-nowrap shantell-sans-regular text-lg"
                    :class="[food.discount_price ? '' : 'hidden']"
                  >
                    {{ food.discount_price }} ₸
                  </p>
                  <p
                    class="text whitespace-nowrap shantell-sans-regular text-lg"
                    :class="[
                      food.discount_price
                        ? 'line-through text-gray-500 text-sm'
                        : '',
                    ]"
                  >
                    {{ food.price }} ₸
                  </p>
                </div>
              </div>
            </li>
          </ul>
        </TabPanel>
      </TabPanels>
    </TabGroup>
  </div>
</template>

<script setup lang="ts">
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";
import { store } from "../store";
import { Store, getStore } from "../api/main";
import { onMounted, ref, computed } from "vue";
import { useRoute } from "vue-router";
import { Dialog, DialogPanel, DialogTitle } from "@headlessui/vue";
import SwitherCard from "../components/swither-card.vue";
const isOpen = ref(false);

function setIsOpen(value: boolean) {
  isOpen.value = value;
}

const seatchText = ref("");
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
  store.store?.categories.forEach((category) => {
    if (category.title.toLowerCase().includes(lower)) {
      if (category.foods.length != 0) {
        data.push(category);
      }
    }
  });

  return data;
});

const route = useRoute();
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
</script>
