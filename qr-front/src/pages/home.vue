<template>
    <div class="w-full m-auto">
    <TabGroup  v-if="store.store">
      <TabList class="!pr-[0px] container mx-auto flex w-auto gap-3 sticky top-0 z-20 bg-white !py-4 overflow-x-auto">  
        <Tab
          v-for="category in store.store?.categories"
          as="template"
          :key="category.id"
          v-slot="{ selected }"
        >
          <button
            :class="[
              'p-2.5 px-4 text-sm rounded-sm bg-slate-100 focus:outline-none',
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
                :src="food.images[0].image"
              />
              <div class="py-4 px-1 mt-2 gap-6 flex justify-between">
                <div>
                  <h3 class="font-medium text-xl leading-5 shantell-sans-regular text-orange-400">
                  {{ food.name }}
                </h3>
                <li class="mt-2 text-xs font-normal leading-4 text-gray-500">
                  {{ food.description }}
                </li>
                </div>
                <div class="flex flex-col gap-1 items-center">
                  <p
                    class="whitespace-nowrap  shantell-sans-regular  text-lg"
                    :class="[food.discount_price ? '' : 'hidden']"
                  >
                    {{ food.discount_price }} ₸
                  </p>
                  <p
                    class="text whitespace-nowrap shantell-sans-regular text-lg"
                    :class="[
                      food.discount_price ? 'line-through text-gray-500 text-sm' : '',
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
import { onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();


const loadStore = async (slug:string) => {
  const storeData: Store = (await getStore(slug)).data;
  store.setStore(storeData);
};
onMounted(() => {
  console.log(route.params);
  const slug = route.params.slug.toString();
  loadStore(slug);
});

</script>