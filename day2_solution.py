def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            print(prefix_products)
            prefix_products.append(prefix_products[-1] * num)
            print(prefix_products)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    print('i m in suffix_now')
    for num in reversed(nums):
        print(suffix_products)
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
            print(suffix_products)
        else:
            suffix_products.append(num)
            print(suffix_products)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result

nums=[1,2,3,4,5]
print(products(nums))
