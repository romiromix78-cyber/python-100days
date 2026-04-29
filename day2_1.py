#魔法のレシピ分量調整くん
# --- DAY 1-2: 魔法のレシピ分量調整くん（レシピ選択版） ---

print("✨　魔法のレシピ調整を開始します　✨")

print("\n 【レシピを選んでください】")
print("1. スパイスカレー")
print("2. 肉じゃが")
print("3. ハンバーグ")

#2. 作り方たいレシピを選択
choice = int(input("\n番号を入力してください (1-3) >> "))

#2. 作りたい人の人数
guests = int(input("今日は何人分をつくりますか？>>"))

#3. 倍率を計算する
base_people = 4
rate = guests / base_people

if choice == 1:
    # スパイスカレーの材料
    recipe_name = "スパイスカレー"
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

elif choice == 2:
    # 肉じゃがの材料
    recipe_name = "肉じゃが"
    beef = 200.0 # 牛薄切り肉（または豚バラ肉）200g
    potato = 4 # ジャガイモ 4個
    onions = 1 # 玉ねぎ 1個
    carrot = 0.5 # にんじん1/2本
    shirataki = 200.0 # しらたき　1袋(200g）
    stock = 400.0 # だし汁400ml
    sugar = 30.0 # 砂糖 大さじ2
    sake = 30.0 # 酒 大さじ2
    mirin = 30.0 # みりん 大さじ2
    soy_sauce = 60.0 #醬油 大さじ4

        #4. 調整後の分量を表示する
    print(f"\n【{guests}人分の材料リスト】")
    print(f"・牛薄切り肉（または豚バラ肉）：{beef * rate:.1f} g")
    print(f"・ジャガイモ:{potato * rate:.1f} 個")
    print(f"・玉ねぎ:{onions * rate:.1f} 個")
    print(f"・にんじん:{carrot * rate:.1f} 本")
    print(f"・しらたき:{shirataki * rate:.1f} g")
    print(f"・だし汁:{stock * rate:.1f} ml")
    print(f"・砂糖:{sugar * rate:.1f} g")
    print(f"・酒:{sake * rate:.1f} g")
    print(f"・みりん:{mirin * rate:.1f} g")
    print(f"・醤油:{soy_sauce* rate:.1f} g")

elif choice == 3:
    recipe_name = "ハンバーグ"    
    # ハンバーグの材料
    beef_pork_mince = 400.0 #合挽き肉400g
    onions = 1 #玉ねぎ1個
    bread_crumbs = 45.0 #パン粉大さじ6
    milk = 30.0 #牛乳大さじ4
    egg = 1 #卵1個
    nutmeg = 0.2 #ナツメグ少々
    salt = 0.2 #少々
    pepper = 0.2 #少々

    print(f"\n【{guests}人分の材料リスト】")
    print(f"・合挽きひき肉：{beef_pork_mince * rate:.1f} g")
    print(f"・玉ねぎ:{onions * rate:.1f} 個")
    print(f"・パン粉:{bread_crumbs * rate:.1f} g")
    print(f"・牛乳:{milk* rate:.1f} ml")
    print(f"・卵:{egg * rate:.1f} 個")
    print(f"・ナツメグ:{nutmeg * rate:.1f} g")
    print(f"・塩:{salt * rate:.1f} g")
    print(f"・胡椒:{pepper * rate:.1f} g")

else:
    print("正しい番号を入力してください")
