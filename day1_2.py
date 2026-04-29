# #--- Day 1: レシピの分量計算プログラム　---

# #1.基本となる「2人分」の分量（単位:㎖、g）
# base_people = 2
# olive_oil_base = 30 #大さじ2
# vineger_base = 15 #大さじ1
# salt_base = 2 #小さじ1/3

# #2.今日作りたい人数
# today_gusets = int(input("何人分作りますか？>>"))

# #3.計算する（人数比をかける）
# ratio = today_gusets / base_people

# #4.結果を表示する
# print(f"--{today_gusets}人分のオーガニックドレッシング")

# print(f"オリーブオイル: {olive_oil_base * ratio} ml")
# print(f"お酢: {vineger_base * ratio} ml")
# print(f"お塩： {salt_base *ratio} g")
# print("----------------------------")
# print("美味しくなーれ")


#魔法のレシピ分量調整くん
# --- DAY 1-2: 魔法のレシピ分量調整くん（スパイスカレー編） ---

print("✨　魔法のレシピ調整を開始します　✨")

#1.　基準となる「4人分」の材料(gまたはml）
base_people = 4 
onions = 2     #玉ねぎ　2個
tomato = 200 #トマト缶　1缶
chicken = 500 #鶏肉　500g
turmeric = 5.0 #ターメリック　5g
cumin = 5.0 #クミン　5g
coriander = 10.0 #コリアンダー　10g
ginger = 10.0 #ショウガ　すりおろし　10g
garlic = 5.0 #ニンニク　すりおろし　5g
water = 400 #水 400ml
sugar = 10.0 #砂糖　10g
soy_sauce = 15.0 #醬油　15g
yoghurt = 50.0 #ヨーグルト　50g
salt = 0.2 #少々

#2. 作りたい人の人数
guests = int(input("今日は何人分のカレーをつくりますか？>>"))

#3. 倍率を計算する
rate = guests / base_people

#4. 調整後の分量を表示する
print(f"\n【{guests}人分の材料リスト】")
print(f"・玉ねぎ：{onions * rate:.1f} 個")
print(f"・トマト缶:{tomato * rate:.1f} g")
print(f"・鶏肉:{chicken * rate:.1f} g")
print(f"・ターメリック:{turmeric * rate:.1f} g")
print(f"・クミン:{cumin * rate:.1f} g")
print(f"・コリアンダー:{coriander* rate:.1f} g")
print(f"・ショウガ:{ginger* rate:.1f} g")
print(f"・ニンニク:{garlic* rate:.1f} g")
print(f"・お水:{water * rate:.1f} ml")
print(f"・砂糖:{sugar* rate:.1f} g")
print(f"・醤油:{soy_sauce* rate:.1f} g")
print(f"・ヨーグルト:{yoghurt* rate:.1f} g")
print(f"・塩:{salt* rate:.1f} g")

print(f"\n★　作り方　★")
print(f"1.鶏肉を食べやすい大きさに切り、コショウを振る。玉ねぎは粗みじん切りにする。")
print(f"2.鍋にサラダ油を熱し（1）の玉ねぎを入れ中火～強火で焦がさないように炒める")
print(f"(2)が透き通ってきたら、ニンニク、ショウガを加えて色づくまで火を弱めてさらに炒める")
print(f"クミン,コリアンダー,ターメリックのスパイス類を加えてからよく炒め、トマト缶を加えて水分をとばすように炒める")
print(f"水、塩を加えて沸騰したら(1)の鶏肉を加え、蓋をして時々かき混ぜながら弱火で20～30分煮込む")
print(f"ヨーグルト、醤油を加え、最後に味を見て足りなければ、醬油を加えて味を調える")

print("=== 魔法のレシピ分量調整くん ===")
print("\n 【レシピを選んでください】")
print("1. スパイスカレー")
print("2. 肉じゃが")
print("3. ハンバーグ")

choice = input("\n番号を入力してください (1-3) >> ")

if choice == "1":
    # スパイスカレーの材料
    recipe_name = "スパイスカレー"
    base_people = 4
    #...材料を定義

elif choice == "2":
    # 肉じゃがの材料
    recipe_name = "肉じゃが"
    base_people = 4
    #...材料を定義

elif choice == "3":
    # ハンバーグの材料
    recipe_name = "ハンバーグ"
    base_people = 4
    #...材料を定義

else:
    print("正しい番号を入力してください")



 