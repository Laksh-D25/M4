<template>
  <div class="flex flex-col w-full bg-[#DB4A2B] justify-center items-center">
    <h1 class="mx-2 text-center text-4xl font-bold text-[#E4E2DD] mt-5">Welcome to the Test Center</h1>
    <div class="my-10">
      <div :class="['flex items-center justify-center h-64 bg-gray-200 rounded-lg', !cameraOn ? 'hidden' : 'block']">
        <video id="camera-feed" autoplay class="rounded-lg w-full h-full"></video>
      </div>
      <div :class="['p-2 flex flex-col items-center justify-center h-64 bg-[#E4E2DD] rounded-lg lg:px-8 lg:mx-0 mx-3', cameraOn ? 'hidden' : 'block']">
        <VideoCameraSlashIcon class="text-[#DB4A2B] h-12 w-12"/>
        <p class="text-gray-500 text-center lg:my-0 my-3">{{ errorMessage }}</p>
      </div>
    </div>

    <div class="mt-4 flex lg:flex-row flex-col justify-center items-center">
      <button @click="toggleCamera" class="m-[5px] py-[10px] px-[20px] font-[16px] rounded-lg bg-[#E4E2DD] text-[#DB4A2B] flex items-center gap-x-2">
        {{ cameraOn ? 'Turn Off Camera' : 'Turn On Camera' }} <VideoCameraSlashIcon v-if="cameraOn" class="text-[#DB4A2B] h-5 w-5"/> <VideoCameraIcon v-else class="text-[#DB4A2B] h-5 w-5"/>
      </button>
      <button :class="['p-4 rounded-lg bg-[#E4E2DD] text-[#DB4A2B] m-[5px] py-[10px] px-[20px] font-[16px]', cameraOn ? 'cursor-pointer' : 'cursor-not-allowed']" @click="detectMood" :disabled="!cameraOn">Detect Mood & Get Songs</button>
    </div>

    <!-- Song Recommendation Section -->
    <h3 class="mx-2 text-center text-3xl font-bold text-[#E4E2DD] my-5">Recommended Songs:</h3>
    <div v-if="songs.length > 0" class="mt-4 mb-10">
      <h3 class="mx-2 text-center text-xl font-bold text-[#E4E2DD] my-5"> Your Mood - {{ songs[0]['mood'] }} </h3>
      <ul role="list" class="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <li v-for="song in songs" :key="song.name" class="col-span-1 flex flex-col divide-y divide-gray-200 rounded-lg bg-[#E4E2DD] text-center shadow hover:scale-110">
          <div class="flex flex-1 flex-col p-8">
            <img class="mx-auto h-32 w-32 flex-shrink-0 rounded-full" :src="song.image" alt="Song Album Art" />
            <h3 class="mt-6 text-sm font-medium text-gray-900">{{ song.name }}</h3>
            <dl class="mt-1 flex flex-grow flex-col justify-between">
              <dt class="sr-only">Artist</dt>
              <dd class="text-sm text-gray-500">{{ song.artist }}</dd>
              <dt class="sr-only">Genre</dt>
              <dd class="mt-3">
                <span class="inline-flex items-center rounded-full bg-[#DB4A2B] px-2 py-1 text-xs font-medium text-[#E4E2DD]">{{ song.genre }}</span>
              </dd>
            </dl>
          </div>
          <div>
            <div class="flex">
              <div class="flex w-full">
                <a :href="song.url" class="relative w-full items-center justify-center rounded-lg border border-1 border-[#E4E2DD]/2 py-4 text-sm font-semibold text-gray-900 flex items-center gap-x-1 hover:bg-[#878683] hover:text-[#E4E2DD]">
                  Go to Song
                  <ArrowTopRightOnSquareIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
                </a>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div v-else class="my-4 lg:mx-0 mx-3">
      <div class="relative block w-full rounded-lg border-2 border-dashed border-[#878683] bg-[#E4E2DD] p-12 lg:px-40 text-center hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        <SignalSlashIcon class="mx-auto h-20 w-20 text-[#DB4A2B]" aria-hidden="true" />
        <span class="mt-2 block text-sm font-semibold text-gray-900">No songs here...</span>
        <p class="mt-2 block text-base font-semibold text-gray-500">No songs found for this mood.<br>Here are a list of things you can do:</p>
        <ul role="list" class="mt-1 list-disc">
          <li class="text-sm font-semibold text-gray-500">
            Turn on your Camera/Check Camera Permissions
          </li>
          <li class="text-sm font-semibold text-gray-500">
            Click on the "Detect Mood & Get Songs" button
          </li>
          <li class="text-sm font-semibold text-gray-500">
            Contact Us - <a class="text-[#DB4A2B]" href="mailto:laksh.d@bcah.christuniversity.in">Send a mail</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, onBeforeUnmount } from 'vue';
import DetectRTC from 'detectrtc';
import { VideoCameraSlashIcon, VideoCameraIcon, ArrowTopRightOnSquareIcon, SignalSlashIcon } from '@heroicons/vue/24/outline';
import { useToast } from '../useToast'

const cameraOn = ref(false);
const stream = ref(null);
const errorMessage = ref("Camera switched off or No access given.");
const songs = ref([]);
const { showToast } = useToast();

// Check for webcam permissions on mounted
onMounted(() => {
  DetectRTC.load(() => {
    if (!DetectRTC.hasWebcam) {
      errorMessage.value = "No webcam detected or permission denied.";
      showToast(errorMessage.value, 'error');
    }
  });
});

async function toggleCamera() {
  if (cameraOn.value) {
    // Turn off the camera
    if (stream.value) {
      let tracks = stream.value.getTracks();
      tracks.forEach(track => track.stop());
      showToast("Camera turned off", 'warning');
    }
    stream.value = null;
    cameraOn.value = false;
  } else {
    // Turn on the camera
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
      stream.value = mediaStream;

      // Set the stream to the video element after the DOM has updated
      await nextTick(); // Ensure DOM is updated
      const video = document.getElementById('camera-feed');
      if (video) {
        video.srcObject = mediaStream;
        cameraOn.value = true;
        showToast("Camera turned on", 'info');
      }
    } catch (error) {
      showToast(`Error accessing camera: ${ error }`, 'error');
      handleCameraError(error);
    }
  }
}

function handleCameraError(error) {
  if (error.name === "NotAllowedError") {
    errorMessage.value = "Camera access was denied. Please allow camera permissions.";
  } else if (error.name === "NotFoundError") {
    errorMessage.value = "No camera found. Please check your device.";
  } else {
    errorMessage.value = "An error occurred while accessing the camera. Please check your device.";
  }
}

async function detectMood() {
  const video = document.getElementById('camera-feed');
  if (video) {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);

    // Convert the canvas to an image blob
    canvas.toBlob(async (blob) => {
      const formData = new FormData();
      formData.append('image', blob);

      // Send the image to the backend for mood detection
      const response = await fetch('http://127.0.0.1:5000/api/detect-emotion', {
        method: 'POST',
        body: formData,
        mode: 'cors'
      });

      const data = await response.json();
      await getSongs(data.emotion);  // Get recommended songs based on detected mood
    });
  }
}

async function getSongs(mood) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/recommend-songs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mood })
    });

    const data = await response.json();
    songs.value = data.songs;
    showToast("Songs fetched successfully", 'success');
  } catch (error) {
    showToast(`Error fetching songs: ${ error }`, 'error');
  }
}

// Stop the camera stream on unmount
onBeforeUnmount(() => {
  if (stream.value) {
    let tracks = stream.value.getTracks();
    tracks.forEach(track => track.stop());
  }
});
</script>

