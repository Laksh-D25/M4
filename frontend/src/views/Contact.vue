<template>
    <div class="relative isolate bg-[#DB4A2B]">
        <div class="mx-auto grid max-w-7xl grid-cols-1 lg:grid-cols-2">
            <div class="relative px-6 pb-20 pt-24 sm:pt-32 lg:static lg:px-8 lg:py-48">
                <div class="mx-auto max-w-xl lg:mx-0 lg:max-w-lg">
                    <div class="absolute inset-y-0 left-0 -z-10 w-full overflow-hidden bg-[#E4E2DD] ring-1 ring-gray-900/10 lg:w-1/2">
                        <svg class="absolute inset-0 h-full w-full stroke-gray-200 [mask-image:radial-gradient(100%_100%_at_top_right,#E4E2DD,transparent)]" aria-hidden="true">
                            <defs>
                            <pattern id="83fd4e5a-9d52-42fc-97b6-718e5d7ee527" width="200" height="200" x="100%" y="-1" patternUnits="userSpaceOnUse">
                                <path d="M130 200V.5M.5 .5H200" fill="none" />
                            </pattern>
                            </defs>
                            <rect width="100%" height="100%" stroke-width="0" fill="white" />
                            <svg x="100%" y="-1" class="overflow-visible fill-gray-50">
                            <path d="M-470.5 0h201v201h-201Z" stroke-width="0" />
                            </svg>
                            <rect width="100%" height="100%" stroke-width="0" fill="url(#83fd4e5a-9d52-42fc-97b6-718e5d7ee527)" />
                        </svg>
                    </div>
                    <h2 class="text-3xl font-bold tracking-tight text-[#DB4A2B]">Get in touch</h2>
                    <p class="mt-6 text-lg leading-8 text-gray-600">Proin volutpat consequat porttitor cras nullam gravida at. Orci molestie a eu arcu. Sed ut tincidunt integer elementum id sem. Arcu sed malesuada et magna.</p>
                    <dl class="mt-10 space-y-4 text-base leading-7 text-gray-600">
                    <div class="flex gap-x-4">
                        <dt class="flex-none">
                        <span class="sr-only">Address</span>
                        <BuildingOffice2Icon class="h-7 w-6 text-[#DB4A2B]" aria-hidden="true" />
                        </dt>
                        <dd>#273 Chamrajpete<br />Bangalore, Karnataka - 560018</dd>
                    </div>
                    <div class="flex gap-x-4">
                        <dt class="flex-none">
                        <span class="sr-only">Telephone</span>
                        <PhoneIcon class="h-7 w-6 text-[#DB4A2B]" aria-hidden="true" />
                        </dt>
                        <dd><a class="hover:text-gray-900" href="tel:+91 7975948835">+91 7975948835</a></dd>
                    </div>
                    <div class="flex gap-x-4">
                        <dt class="flex-none">
                        <span class="sr-only">Email</span>
                        <EnvelopeIcon class="h-7 w-6 text-[#DB4A2B]" aria-hidden="true" />
                        </dt>
                        <dd><a class="hover:text-gray-900" href="mailto:laksh.d@bcah.christuniversity.in">laksh.d@bcah.christuniversity.in</a></dd>
                    </div>
                    </dl>
                </div>
            </div>
            <form @submit.prevent="sendEmail" method="POST" class="px-6 pb-24 pt-20 sm:pb-32 lg:px-8 lg:py-48">
                <div class="mx-auto max-w-xl lg:mr-0 lg:max-w-lg">
                    <div class="grid grid-cols-1 gap-x-8 gap-y-6 sm:grid-cols-2">
                        <div>
                            <label for="first-name" class="block text-sm font-semibold leading-6 text-[#E4E2DD]">First name</label>
                            <div class="mt-2.5">
                                <input v-model="firstName" type="text" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-[#DB4A2B] focus:ring-2 focus:ring-inset focus:ring-[#E4E2DD] sm:text-sm sm:leading-6" />
                            </div>
                        </div>
                        <div>
                            <label for="last-name" class="block text-sm font-semibold leading-6 text-[#E4E2DD]">Last name</label>
                            <div class="mt-2.5">
                                <input v-model="lastName" type="text" name="last-name" id="last-name" autocomplete="family-name" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-[#DB4A2B] focus:ring-2 focus:ring-inset focus:ring-[#E4E2DD] sm:text-sm sm:leading-6" />
                            </div>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="email" class="block text-sm font-semibold leading-6 text-[#E4E2DD]">Email</label>
                            <div class="mt-2.5">
                                <input v-model="email" type="email" name="email" id="email" autocomplete="email" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-[#DB4A2B] focus:ring-2 focus:ring-inset focus:ring-[#E4E2DD] sm:text-sm sm:leading-6" />
                            </div>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="phone-number" class="block text-sm font-semibold leading-6 text-[#E4E2DD]">Phone number</label>
                            <div class="mt-2.5">
                                <input v-model="phone" type="tel" name="phone-number" id="phone-number" autocomplete="tel" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-[#DB4A2B] focus:ring-2 focus:ring-inset focus:ring-[#E4E2DD] sm:text-sm sm:leading-6" />
                            </div>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="message" class="block text-sm font-semibold leading-6 text-[#E4E2DD]">Message</label>
                            <div class="mt-2.5">
                                <textarea v-model="message" name="message" id="message" rows="4" class="block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-[#DB4A2B] focus:ring-2 focus:ring-inset focus:ring-[#E4E2DD] sm:text-sm sm:leading-6" />
                            </div>
                        </div>
                    </div>
                    <div class="mt-8 flex justify-end">
                        <button type="submit" class="rounded-md bg-[#E4E2DD] px-3.5 py-2.5 text-center text-sm font-semibold text-[#DB4A2B] shadow-sm hover:bg-[#E4E2EE] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E4E2DD]">Send message</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { BuildingOffice2Icon, EnvelopeIcon, PhoneIcon } from '@heroicons/vue/24/outline'
    import axios from 'axios';
    import { ref } from 'vue';
    import { useToast } from '../useToast';

    const firstName = ref('');
    const lastName = ref('');
    const email = ref('');
    const phone = ref('');
    const message = ref('');

    const { showToast } = useToast();

    function sendEmail() {
        const data = {
            firstName: firstName.value,
            lastName: lastName.value,
            email: email.value,
            phone: phone.value,
            message: message.value,
        }
        axios.post('http://127.0.0.1:5000/api/contactus', data).then(response => {
            console.log(response.data);
            showToast('Successfully sent!\nThank you for contacting us.', 'success');
        })
        .catch(error => {
            console.log(error);
            showToast(`Error Occured ${ error }`, 'error');
        });

        firstName.value = '';
        lastName.value = '';
        email.value = '';
        phone.value = '';
        message.value = '';
    }
</script>