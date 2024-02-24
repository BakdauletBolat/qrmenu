<template>
<div class="relative">
  <div>
      <div class="flex items-center justify-center">
      <div v-if="error" class="bg-orange-400 absolute p-3 text-center rounded-sm top-4 text-white z-10 w-[95%]">{{ error }}</div>
    </div>
    <div class="flex items-center absolute justify-center w-full h-[100vh] z-10">
      <img :src="QRIcon" class="text-white w-20 h-20">
    </div>
     <div v-if="loading" class="flex items-center absolute justify-center w-full h-[100vh] z-10">
      <div class="bg-orange-400 text-white text-3xl p-4 rounded-sm">
        <svg
      class="w-[200px] "
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 300 150"
    >
      <path
        fill="none"
        stroke="#FFFFFF"
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
    </div>
    <router-link to="/">
      <ChevronLeftIcon class="w-8 h-8 absolute left-3 z-10 rounded text-white bg-orange-400 p-1 top-6"></ChevronLeftIcon>
    </router-link>
    <div class="w-full h-[100vh]">
  		<qrcode-stream @camera-on="onCameraOn" :track="paintBoundingBox" @detect="onDetect" @error="onError"></qrcode-stream>
    </div>
  </div>

</div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { QrcodeStream } from 'vue-qrcode-reader';
import QRIcon from '../assets/qr-scan-svgrepo-com.svg';
import { ChevronLeftIcon } from '@heroicons/vue/24/outline';
import {useRouter} from "vue-router";
import axios from 'axios';
import { instance } from '@/plugins/axios-instance';

  const result = ref('')
  const error = ref('');
  const loading = ref(true);

  const router = useRouter();
  const onCameraOn = () => {
      loading.value = false;
  }

  function paintBoundingBox(detectedCodes:any, ctx:any) {
    for (const detectedCode of detectedCodes) {
      const {
        boundingBox: { x, y, width, height }
      } = detectedCode

      ctx.lineWidth = 2
      ctx.strokeStyle = '#007bff'
      ctx.strokeRect(x, y, width, height)
    }
  }

  function onError(err:any) {
    error.value = `[${err.name}]: `

    if (err.name === 'NotAllowedError') {
      error.value += 'you need to grant camera access permission'
    } else if (err.name === 'NotFoundError') {
      error.value += 'no camera on this device'
    } else if (err.name === 'NotSupportedError') {
      error.value += 'secure context required (HTTPS, localhost)'
    } else if (err.name === 'NotReadableError') {
      error.value += 'is the camera already in use?'
    } else if (err.name === 'OverconstrainedError') {
      error.value += 'installed cameras are not suitable'
    } else if (err.name === 'StreamApiNotSupportedError') {
      error.value += 'Stream API is not supported in this browser'
    } else if (err.name === 'InsecureContextError') {
      error.value += 'Camera access is only permitted in secure context. Use HTTPS or localhost rather than HTTP.'
    } else {
      error.value += err.message
    }
  }

  async function onDetect(detectedCodes:any) {
    const qr = detectedCodes[0].rawValue;
    loading.value = true;
   try {
      const parsed = JSON.parse(qr);
      await checkValidQR(parsed.table_id);
      setTimeout(()=>{
        loading.value = false;
        router.push({
        name: 'assign',
        params: {
          id: parsed.table_id
        }
      })
      }, 1000)
   }
   catch (e) {
    if (e!.response != null) {
      error.value = 'Стол уже занят';
    }
    else {
      error.value ="Не правильный формат qr"
    }
      loading.value = false;
   }
  }

  async function checkValidQR(table_id: string) {
    try {
      await instance.get(`table/check-assign/${table_id}/`);
    }
    catch (e) {
      throw e;
    }
  }

</script>