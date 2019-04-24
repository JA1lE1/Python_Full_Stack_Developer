import re


def main():
	names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "__________"]
	for name in names:
		# ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name)
		# ^瑙勫畾寮�ご  $瑙勫畾缁撳熬  
		# python涓�殑match榛樿�鏄�粠澶村紑濮嬪垽鏂�殑鎵�互锛屽湪match涓�彲浠ヤ笉鍐橿锛屼絾鏄痬atch涓嶄細鍒ゆ柇缁撳熬锛屾墍浠�		# 褰撻渶瑕佷互xxx缁撳熬鐨勬椂鍊�杩橀渶瑕佸啓涓�
		ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
		if ret:
			print("鍙橀噺鍚�%s 绗﹀悎瑕佹眰....閫氳繃姝ｅ垯鍖归厤鍑烘潵鐨勬暟鎹�槸:%s" % (name, ret.group()))
		else:
			print("鍙橀噺鍚�%s 涓嶇�鍚堣�姹�..." % name)


if __name__ == "__main__":
	main()

