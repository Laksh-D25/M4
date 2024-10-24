<template>
    <div class="animate-pulse fixed top-0 left-0 w-full h-full flex justify-center items-center bg-[#E4E2DD] z-[999]" v-if="!isLoaded">
        <div>
            <div class="mr-2 text-[#DB4A2B] text-5xl animate-left">music.</div>
            <div class="mr-2 text-[#DB4A2B] text-5xl animate-leftSide">mood.</div>
            <div class="mr-2 text-[#DB4A2B] text-5xl animate-rightSide">mashup.</div>
            <div class="mr-2 text-[#DB4A2B] text-5xl animate-right">machine</div>
        </div>
    </div>
</template>

<script setup>
    import { onMounted, ref } from 'vue';
    let isLoaded = ref(false)

    onMounted(() => {
        document.onreadystatechange = () => {
            if (document.readyState === 'complete') {
                isLoaded.value = true
            }
        }
    })
</script>

<style scoped>
@keyframes left {
    40% {
        transform: translateX(-80px);
    }
    50% {
        transform: translateX(0);
    }
    60% {
        transform: translateX(80px);
    }
}

@keyframes leftSide {
    40% {
        transform: translateX(-40px);
    }
    50% {
        transform: translateX(0);
    }
    60% {
        transform: translateX(40px);
    }
}

@keyframes right {
    40% {
        transform: translateX(80px);
    }
    50% {
        transform: translateX(0);
    }
    60% {
        transform: translateX(-80px);
    }
}

@keyframes rightSide {
    40% {
        transform: translateX(40px);
    }
    50% {
        transform: translateX(0);
    }
    60% {
        transform: translateX(-40px);
    }
}

@keyframes pulse {
    0% {
        opacity: 1;
    }
    50% {
        opacity: 0.95;
    }
    100% {
        opacity: 1;
    }
}

.animate-left {
    animation: left 1s infinite 0.1s ease-in-out;
}

.animate-leftSide {
    animation: leftSide 1s infinite 0.05s ease-in-out;
}

.animate-right {
    animation: right 1s infinite 0.1s ease-in-out;
}

.animate-rightSide {
    animation: rightSide 1s infinite 0.05s ease-in-out;
}

.animate-pulse {
    animation: pulse 1s infinite 0.1s;
}
</style>