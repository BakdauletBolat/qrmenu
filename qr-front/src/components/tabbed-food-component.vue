<script setup lang="ts">
import { Tab, TabGroup, TabList } from '@headlessui/vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { onMounted, ref } from 'vue';

const props = defineProps<{ items: { title: string; id: string }[] }>();
const selectedIndex = ref(0);
const tabListHeight = ref(0);

onMounted(() => {
  tabListHeight.value =
    8 + (document.getElementById('tabList')?.offsetHeight ?? 0);
  props.items.forEach((item, index) => {
    const itemSelector = document.getElementById(item.id);
    ScrollTrigger.create({
      trigger: itemSelector,
      start: () => 'top ' + (tabListHeight.value + 2),
      end: () => 'bottom ' + tabListHeight.value,
      onEnter: () => {
        selectedIndex.value = index;
        scrollTabListToActiveTab(index);
      },
      onEnterBack: () => {
        selectedIndex.value = index;
        scrollTabListToActiveTab(index);
      },
    });
  });

  ScrollTrigger.addEventListener('refreshInit', () => {
    tabListHeight.value =
      8 + (document.getElementById('tabList')?.offsetHeight ?? 0);
  });
});
const scrollToSection = (item: { title: string; id: string }) => {
  const escapedId = `#${CSS.escape(item.id)}`;
  gsap.to(window, {
    scrollTo: {
      y: escapedId,
      offsetY: tabListHeight.value,
    },
  });
};

const scrollTabListToActiveTab = (index: number) => {
  const tabList = document.getElementById('tabList');
  const activeTab = tabList?.children[index] as HTMLElement;

  if (activeTab && tabList) {
    const tabListRect = tabList.getBoundingClientRect();
    const activeTabRect = activeTab.getBoundingClientRect();

    if (activeTabRect.left < tabListRect.left || activeTabRect.right > tabListRect.right) {
      const offset = activeTabRect.left < tabListRect.left
        ? activeTabRect.left - tabListRect.left - 30
        : activeTabRect.right - tabListRect.right + 30;

      tabList.scrollBy({
        left: offset,
        behavior: 'smooth'
      });
    }
  }
};

</script>

<template>
  <TabGroup
    :selected-index="selectedIndex"
    @change="(index) => (selectedIndex = index)"
  >
    <TabList
      id="tabList"
      class="
        py-3
        px-4
        sticky
        flex
        w-full
        overflow-x-scroll
        rounded
        top-0
      "
    >
      <Tab v-for="item in items" as="template" v-slot="{ selected }">
        <button
          @click="scrollToSection(item)"
          :class="{
            'primary-background text-white': selected
          }"
          class="relative p-3 rounded-lg uppercase group"
        >
          <span class="text-nowrap">
            {{ item.title }}
          </span>
        </button>
      </Tab>
    </TabList>
  </TabGroup>
</template>
