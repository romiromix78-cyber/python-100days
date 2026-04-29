# 🌱野菜の月別作業チェッカー ver.2

from datetime import datetime


# --- 特定の野菜と月の「作業リスト」を返す関数 ---
def get_tasks(vegetable, month):
    #初期化（見つからなかった時のデフォルト値）
    label = "データなし"
    tasks = ["この野菜のデータはまだ登録されていません"]

# --- 🍅 トマト ---
    if vegetable == "トマト":
        if 1 <= month <= 2:
            label = "📋 1~2月:準備期間"
            tasks = ["品種を選んで種を購入", "土づくり・堆肥の準備"]
        elif 3 <= month <=4:
            label = "📋 3~4月:種蒔き・育苗"
            tasks = ["室内で種まき（3月中旬～）", "発芽まで土が乾かないように水やり", "本葉が2～3枚になったら間引き"]
        elif month == 5:
            label = "5月:植え付け"
            tasks = ["霜の心配がなくなったら植付", "支柱・誘引の準備"]
        elif 6 <= month <= 8:
            label = "📋 6~8月:生育・収穫期"
            tasks = ["2週間に1度,追肥、脇芽かき", "赤く色づいたら収穫!"]
        elif 9 <= month <= 10:
            label = "📋 9~10月:収穫終盤"
            tasks = ["残っている実を収穫する", "株を片付けて土を休ませる"]
        else:
            label = "📋 11~12月:オフシーズン"
            tasks = ["トマトの栽培はお休みの時期です"]                

    # ---  🌿大根 ---
    elif vegetable == "大根":
        if 1 <= month <=2:
            label = "📋 1~2月:冬大根の収穫・保存"
            tasks = ["霜が降りる前に収穫を終わらせる"]
        elif 3 <= month <=4:
            label = "📋 3~4月:春まきの準備"
            tasks = ["土を深く（30㎝以上)耕しておく", "4月中旬から種まきOK"]
        elif 5 <= month <= 6:
            label = "📋 5～6月:春まき・生育期"
            tasks = ["1箇所に4～5粒播種","本葉が出たら2本⇒1本に間引と追肥"]       
        elif 7 <= month <= 8:
            label = "📋 7~8月:夏は難しい時期"
            tasks = ["秋まきの土づくり"]
        elif 9 <= month <= 10:
            label = "📋 9~10月:秋まきスタート!"
            tasks = ["月上旬～10月上旬播種1箇所に4～5粒播種","本葉が出たら2本⇒1本に間引と追肥"]
        else:
            label = "📋 11~12月:秋まき大根の収穫"
            tasks = ["葉が黄色くなり始めたら収穫サイン"]

    # --- 🌱 ほうれん草  ---
    elif vegetable == "ほうれん草":
        if 1 <= month <=2:
            label = "📋 1~2月:冬越し・収穫"
            tasks = ["ビニールトンネルで保温"]
        elif 3 <= month <=4:
            label = "📋 3~4月:春まきスタート"
            tasks = ["すじまき(1㎝間隔)で種を蒔く","本葉が2～3枚になったら間引く"]
        elif 5 <= month <= 6:
            label = "📋 5～6月:春まき収穫期"
            tasks = ["葉が育ってきたら順次収穫する", "とう立ちしてきたら早めに収穫を"]
        elif 7 <= month <= 8:   
            label = "7~8月：夏は難しい時期"
            tasks = ["夏まき専用品種を選べば可能", "なるべく涼しい場所で育てる"]
        elif 9 <= month <= 10:
            label = "9~10月：秋まきスタート！"
            tasks = ["2〜3週間おきにずらしてすじまき（1cm間隔）", "本葉2〜3枚で間引く"]
        else:
            label = "11~12月：冬越し準備"
            tasks = ["20cm以上で収穫", "霜が強い地域はビニールトンネルで保温"]
    
    return label,tasks


# ===== メイン処理 =====

print("=" *45)
print("🌱 野菜の月別作業チェッカー  ver.2")
print("=" *45)

# 今月を自動で取得
now_month = datetime.now().month
print(f"\n📅 今月は {now_month}月 です\n")

# 育てている野菜のリスト（ここを書き換えて使用する）
my_vegtables = ["トマト", "大根", "ほうれん草"]

print(f"🌾 登録中の野菜: {', '.join(my_vegtables)}")
print("=" * 45)

# --- forループで全野菜をまとめてチエック ---
for veg in my_vegtables:
    label, tasks = get_tasks(veg, now_month)
    
    print(f"\n 【{veg}】の作業")

    print(f"{label}")
    for task in tasks:
        print(f"  ✓ {task}")
    
print("\n" + "=" * 45)
print("✅ 全野菜のチェック完了！")

# --- while ループ:別の付きも確認できる ---

while True:
    another = input("\n別の月の作業も確認しますか？ (y/n) >>")

    if another.lower() == "n":
        print("\n 🌿 またいつでも使ってね！")
        break

    elif another.lower() == "y":
        month_raw = input("何月を確認しますか? (1～12)>> ")

        if not month_raw.isdigit():
            print("⚠️ 数字を入力してください")
            continue #whileの先頭に戻る

        check_month = int(month_raw)

        if check_month <1 or check_month>12:
            print("⚠️  1から12の数字を入力してください")
            continue

        print(f"\n📅 {check_month}月の作業\n " + "=" * 45)

        for veg in my_vegtables:
            label, tasks = get_tasks(veg, check_month)
            print(f"\n🌱 {veg} / 📋{label}")
            for task in tasks:
                print(f" ・{task}")

        print("\n " + "=" * 45)
    
    else:
        print("⚠️  y か n を入力してください")