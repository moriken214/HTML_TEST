def main():
	# ユーザーに名前を入力してもらい、その名前で挨拶する
	name = input("名前を入力してください: ").strip()
	if not name:
		name = "World"
	print(f"Hello {name}")


if __name__ == "__main__":
	main()