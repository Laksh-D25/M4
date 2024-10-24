<template>
    <main class="relative isolate bg-[#DB4A2B] pb-20">
        <!-- Header section -->
        <div class="px-6 pt-14 lg:px-8">
            <div class="mx-auto max-w-2xl pt-24 text-center sm:pt-40">
            <h2 class="text-4xl font-bold tracking-tight text-[#E4E2DD] sm:text-6xl">We love MUSIC ♪</h2>
            <p class="mt-6 text-lg leading-8 text-gray-300">Do you love it as much as we do?</p>
            </div>
        </div>

        <!-- Content section -->
        <div class="mx-auto mt-20 max-w-7xl px-6 lg:px-8">
            <div class="mx-auto max-w-2xl lg:mx-0 lg:max-w-none">
                <div class="grid max-w-xl grid-cols-1 gap-8 text-base leading-7 text-gray-300 lg:max-w-none lg:grid-cols-2">
                    <div>
                        <p>Faucibus commodo massa rhoncus, volutpat. Dignissim sed eget risus enim. Mattis mauris semper sed amet vitae sed turpis id. Id dolor praesent donec est. Odio penatibus risus viverra tellus varius sit neque erat velit. Faucibus commodo massa rhoncus, volutpat. Dignissim sed eget risus enim. Mattis mauris semper sed amet vitae sed turpis id.</p>
                        <p class="mt-8">Et vitae blandit facilisi magna lacus commodo. Vitae sapien duis odio id et. Id blandit molestie auctor fermentum dignissim. Lacus diam tincidunt ac cursus in vel. Mauris varius vulputate et ultrices hac adipiscing egestas.</p>
                    </div>
                    <div>
                        <p>Erat pellentesque dictumst ligula porttitor risus eget et eget. Ultricies tellus felis id dignissim eget. Est augue maecenas risus nulla ultrices congue nunc tortor. Enim et nesciunt doloremque nesciunt voluptate.</p>
                        <p class="mt-8">Et vitae blandit facilisi magna lacus commodo. Vitae sapien duis odio id et. Id blandit molestie auctor fermentum dignissim. Lacus diam tincidunt ac cursus in vel. Mauris varius vulputate et ultrices hac adipiscing egestas. Iaculis convallis ac tempor et ut. Ac lorem vel integer orci.</p>
                    </div>
                </div>
                <dl class="mt-16 grid grid-cols-1 gap-x-8 gap-y-12 sm:mt-20 sm:grid-cols-2 sm:gap-y-16 lg:mt-28 lg:grid-cols-4">
                    <div v-for="(stat, statIdx) in stats" :key="statIdx" class="flex flex-col-reverse gap-y-3 border-l border-white/20 pl-6">
                    <dt class="text-base leading-7 text-gray-300">{{ stat.label }}</dt>
                    <dd class="text-3xl font-semibold tracking-tight text-[#E4E2DD]">{{ stat.value }}</dd>
                    </div>
                </dl>
            </div>
        </div>

        <!-- Image section -->
        <div class="mt-32 sm:mt-40 xl:mx-auto xl:max-w-7xl xl:px-8">
            <img src="https://images.unsplash.com/photo-1521737852567-6949f3f9f2b5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2894&q=80" alt="" class="aspect-[9/4] w-full object-cover xl:rounded-3xl" />
        </div>

        <!-- Values section -->
        <div class="mx-auto mt-32 max-w-7xl px-6 sm:mt-40 lg:px-8">
            <div class="mx-auto max-w-2xl lg:mx-0">
            <h2 class="text-3xl font-bold tracking-tight text-[#E4E2DD] sm:text-4xl">Our values</h2>
            <p class="mt-6 text-lg leading-8 text-gray-300">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis.</p>
            </div>
            <dl class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-8 text-base leading-7 text-gray-300 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:gap-x-16">
            <div v-for="value in values" :key="value.name" class="relative pl-9">
                <dt class="inline font-semibold text-[#E4E2DD]">
                <component :is="value.icon" class="absolute left-1 top-1 h-5 w-5 text-indigo-500" aria-hidden="true" />
                {{ value.name }}
                </dt>
                {{ ' ' }}
                <dd class="inline">{{ value.description }}</dd>
            </div>
            </dl>
        </div>

        <!-- Team section -->
        <div class="mx-auto mt-32 max-w-7xl px-6 sm:mt-40 lg:px-8">
            <div class="mx-auto max-w-2xl lg:mx-0">
            <h2 class="text-3xl font-bold tracking-tight text-[#E4E2DD] sm:text-4xl">Our team</h2>
            <p class="mt-6 text-lg leading-8 text-gray-300">Excepturi repudiandae alias ut. Totam aut facilis. Praesentium in neque vel omnis. Eos error odio. Qui fugit voluptatibus eum culpa.</p>
            </div>
            <ul role="list" class="mx-auto mt-20 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-14 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3 xl:grid-cols-4">
            <li v-for="person in team" :key="person.name">
                <img class="aspect-[14/13] w-full rounded-2xl object-cover" :src="person.imageUrl" alt="" />
                <h3 class="mt-6 text-lg font-semibold leading-8 tracking-tight text-[#E4E2DD]">{{ person.name }}</h3>
                <p class="text-base leading-7 text-gray-300">{{ person.role }}</p>
                <p class="text-sm leading-6 text-gray-500">{{ person.location }}</p>
            </li>
            </ul>
        </div>

        <!-- CTA section -->
        <div class="relative isolate -z-10 mt-32 sm:mt-40">
            <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
            <div class="mx-auto flex max-w-2xl flex-col gap-16 bg-[#E4E2DD]/95 px-6 py-16 ring-1 ring-white/10 sm:rounded-3xl sm:p-8 lg:mx-0 lg:max-w-none lg:flex-row lg:items-center lg:py-20 xl:gap-x-20 xl:px-20">
                <img class="h-96 w-full flex-none rounded-2xl object-cover shadow-xl lg:aspect-square lg:h-auto lg:max-w-sm" src="https://images.unsplash.com/photo-1519338381761-c7523edc1f46?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=80" alt="" />
                <div class="w-full flex-auto">
                <h2 class="text-3xl font-bold tracking-tight text-[#DB4A2B] sm:text-4xl">Join our team</h2>
                <p class="mt-6 text-lg leading-8 text-black">Lorem ipsum dolor sit amet consect adipisicing elit. Possimus magnam voluptatum cupiditate veritatis in accusamus quisquam.</p>
                <ul role="list" class="mt-10 grid grid-cols-1 gap-x-8 gap-y-3 text-base leading-7 text-[#DB4A2B] sm:grid-cols-2">
                    <li v-for="benefit in benefits" :key="benefit" class="flex gap-x-3">
                    <CheckCircleIcon class="h-7 w-5 flex-none" aria-hidden="true" />
                    {{ benefit }}
                    </li>
                </ul>
                <div class="mt-10 flex">
                    <a href="#" class="text-sm font-semibold leading-6 text-[#DB4A2B]">See our job postings <span aria-hidden="true">&rarr;</span></a>
                </div>
                </div>
            </div>
            </div>
            
            </div>
    </main>

</template>

<script setup>
    const stats = [
        { label: 'Founded', value: '2024' },
        { label: 'Our Customers', value: '44K+' },
        { label: 'Assets under holding', value: '₹19 crores' },
        { label: 'New users monthly', value: '6,000+' },
    ]
    const values = [
        {
            name: 'Be world-class',
            description:
            'Aut illo quae. Ut et harum ea animi natus. Culpa maiores et sed sint et magnam exercitationem quia. Ullam voluptas nihil vitae dicta molestiae et. Aliquid velit porro vero.',
        },
        {
            name: 'Share everything you know',
            description:
            'Mollitia delectus a omnis. Quae velit aliquid. Qui nulla maxime adipisci illo id molestiae. Cumque cum ut minus rerum architecto magnam consequatur. Quia quaerat minima.',
        },
        {
            name: 'Always learning',
            description:
            'Aut repellendus et officiis dolor possimus. Deserunt velit quasi sunt fuga error labore quia ipsum. Commodi autem voluptatem nam. Quos voluptatem totam.',
        },
        {
            name: 'Be supportive',
            description:
            'Magnam provident veritatis odit. Vitae eligendi repellat non. Eum fugit impedit veritatis ducimus. Non qui aspernatur laudantium modi. Praesentium rerum error deserunt harum.',
        },
        {
            name: 'Take responsibility',
            description:
            'Sit minus expedita quam in ullam molestiae dignissimos in harum. Tenetur dolorem iure. Non nesciunt dolorem veniam necessitatibus laboriosam voluptas perspiciatis error.',
        },
        {
            name: 'Enjoy downtime',
            description:
            'Ipsa in earum deserunt aut. Quos minus aut animi et soluta. Ipsum dicta ut quia eius. Possimus reprehenderit iste aspernatur ut est velit consequatur distinctio.',
        },
    ]
    const team = [
        {
            name: 'Laksh D',
            role: 'Co-Founder / CTO',
            imageUrl:
            '/img/1.png',
        },
        {
            name: 'Cris Grace',
            role: 'Co-Founder / CEO',
            imageUrl:
            '/img/1.png',
        },
        {
            name: 'Vidhaan D',
            role: 'Head of Marketing & Finance',
            imageUrl:
            '/img/1.png',
        },
        {
            name: 'Oogway',
            role: 'Just There',
            imageUrl:
            '/img/1.png',
        },
    ]

    const benefits = [
    'Competitive salaries',
    'Flexible work hours',
    '30 days of paid vacation',
    'Annual team retreats',
    'Benefits for you and your family',
    'A great work environment',
]

</script>