<template>
    <TransitionRoot appear :show="model" as="template">
      <Dialog as="div" @close="closeModal" class="relative w-full z-[10000]">
        <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-black/25" />
        </TransitionChild>
  
        <div class="fixed inset-0 overflow-y-auto">
          <div
            class="flex min-h-full h-full items-end md:items-center justify-end  text-center"
          >
            <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="translate-y-[500px] md:translate-y-0 md:translate-x-[500px]"
              enter-to="translate-y-0 md:translate-x-0"
              leave="duration-200 ease-in"
              leave-from="translate-y-0 md:translate-x-0"
              leave-to="translate-y-[500px] md:translate-y-0 md:translate-x-[500px]"
            >
              <DialogPanel
                class="w-[500px] transform overflow-scroll rounded-md md:rounded-none bg-white max-h-[80vh] md:max-h-full md:h-full p-6 text-left shadow-xl transition-all"
              >
                <DialogTitle
                  as="template"
                >
                <div class="flex items-center justify-between">
                  <h2 class="text-lg font-medium text-gray-900">{{ title }}</h2>
                  <button type="button"
                    class="-mr-2 flex h-10 w-10 items-center justify-center rounded-md bg-white p-2 text-gray-400"
                    @click="model = false">
                    <span class="sr-only">Close menu</span>
                    <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                  </button>
                </div>
                </DialogTitle>
              <div class="mt-5">
                <slot></slot>
              </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </template>
  
  <script setup lang="ts">
  import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
  } from '@headlessui/vue';
  import { XMarkIcon } from '@heroicons/vue/24/outline'

  const model = defineModel<boolean>();
  defineProps<{
    title: string
  }>();
  
  function closeModal() {
    model.value = false
  }
  </script>
  