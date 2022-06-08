nums = []

for i in range(0, 5):
    nums.append(float(input('Insira um valor: ')))

soma = sum(nums)
soma = soma + nums[i]

med = soma / 5

maior_num = 0

for i in nums:
    if maior_num == 0 or i > maior_num:
        maior_num = i

print(f'Números: {nums}')
print(f'Soma dos números: {soma}')
print(f'A média desses números: {med}')
print(f'Maior número: {maior_num}')
