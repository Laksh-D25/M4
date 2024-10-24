<template>
    <div v-if="visible" :class="toastClasses" class="fixed top-4 right-4 max-w-xs w-full p-4 rounded shadow-lg transition-opacity duration-500 ease-in-out border-x-4" style="z-index: 999;">
        <div class="flex items-center">
            <div class="flex-shrink-0">
                <component :is="toastIcon" class="h-6 w-6" :class="toastIconClasses" aria-hidden="true"></component>
            </div>
            <div class="ml-3">
                <p class="text-sm font-medium">
                    {{ message }}
                </p>
            </div>
            <div class="ml-auto pl-3">
                <button @click="closeToast" class="text-lg leading-5 font-semibold text-gray-900 hover:text-red-600">
                    &times;
                </button>
            </div>
        </div>
    </div>
</template>


<script setup>
    import { ref, computed, watchEffect, onMounted } from 'vue';
    import { CheckCircleIcon, XCircleIcon, InformationCircleIcon, ExclamationTriangleIcon } from '@heroicons/vue/24/outline'
    // Props
    const props = defineProps({
        type: {
            type: String,
            default: 'success',
        },
        message: {
            type: String,
            required: true,
        },
        duration: {
            type: Number,
            default: 3000,
        },
    });

    const visible = ref(false);

    const toastIcon = computed(() => {
        switch (props.type) {
            case 'success':
                return CheckCircleIcon;
            case 'error':
                return XCircleIcon;
            case 'info':
                return InformationCircleIcon;
            case 'warning':
                return ExclamationTriangleIcon;
            default:
                return InformationCircleIcon;
        }
    });

    const toastIconClasses = computed(() => {
        return {
        'text-green-500': props.type === 'success',
        'text-red-500': props.type === 'error',
        'text-blue-500': props.type === 'info',
        'text-yellow-500': props.type === 'warning',
        };
    })

    const toastClasses = computed(() => {
        return {
        'bg-green-200 text-green-500 border-green-500': props.type === 'success',
        'bg-red-200 text-red-500 border-red-500': props.type === 'error',
        'bg-blue-200 text-blue-500 border-blue-500': props.type === 'info',
        'bg-yellow-200 text-yellow-500 border-yellow-500': props.type === 'warning',
        };
    });

    // Methods
    const showToast = () => {
        visible.value = true;
        setTimeout(() => {
        closeToast();
        }, props.duration);
    };

    const closeToast = () => {
        visible.value = false;
    };

    // Lifecycle hook to automatically show toast when component is mounted
    onMounted(() => {
        showToast();
    });
</script>