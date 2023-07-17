def lengthOfLongestSubstring(s: str) -> int:

	l1 = []
	count = 0
	maxN = 0
	s = s + ' '
	for i in range(len(s) - 1):
		if (s[i] not in l1) and s[i] != s[i +1 ]:
			l1.append(s[i])
			count += 1
			if count > maxN:
				maxN = count
			else:
				count = 0
		# print(count, maxN)
	print(count, maxN)


s = "pwwkew"
lengthOfLongestSubstring(s)
