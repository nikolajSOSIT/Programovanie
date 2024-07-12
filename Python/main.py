import vulkan as vk

instance_create_info = vk.VkInstanceCreateInfo(
    sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
    pNext=None,
    flags=0,
    pApplicationInfo=application_info,
    enabledLayerCount=len(layers),
    ppEnabledLayerNames=layers,
    enabledExtensionCount=len(extensions),
    ppEnabledExtensionNames=extensions,
)