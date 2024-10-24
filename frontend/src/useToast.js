import { ref } from 'vue';

const show = ref(false);
const toastMessage = ref('');
const toastType = ref('');

const showToast = (message, type = 'success') => {
    toastMessage.value = message;
    toastType.value = type;
    show.value = true;

    setTimeout(() => {
        show.value = false;
    }, 3000); // Hide after 3 seconds
};

export const useToast = () => {
    return {
        show,
        toastMessage,
        toastType,
        showToast,
    };
};
