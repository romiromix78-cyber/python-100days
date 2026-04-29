# 🌱野菜の月別作業チェッカー ver.3

from datetime import datetime


# --- 野菜の月別作業データ（辞書で管理） ---

VEGETABLE_DATA = {
    "トマト":[
        {"months": range(1, 3), "label": "📋 1~2月:準備期間", "tasks":["品種を選んで種を購入","土づくり・堆肥の準備"]},
        {"months": range(3, 5), "label": "📋 3~4月:種蒔き・育苗", "tasks":["室内で種まき（3月中旬～）","発芽まで土が乾かないように水やり","本葉が2～3枚になったら間引き"]},
        {"months": range(5, 6), "label": "📋 5月:植え付け", "tasks":["霜の心配がなくなったら植付","支柱・誘引の準備"]},
        {"months": range(6, 9), "label": "📋 6~8月:生育・収穫期", "tasks":["2週間に1度,追肥、脇芽かき","赤く色づいたら収穫!"]},
        {"months": range(9, 10), "label": "📋 9~10月:収穫終盤", "tasks":["残っている実を収穫する","株を片付けて土を休ませる"]},
        {"months": range(11, 13), "label": "📋 11~12月:オフシーズン", "tasks":["トマトの栽培はお休みの時期です"]}
    ],

    "大根":[
        {"months": range(1, 3), "label": "📋 1~2月:冬大根の収穫・保存", "tasks":["霜が降りる前に収穫を終わらせる"]},
        {"months": range(3, 5), "label": "📋 3~4月:春まきの準備", "tasks":["土を深く（30㎝以上)耕しておく","4月中旬から種まきOK"]},
        {"months": range(5, 7), "label": "📋 5～6月:春まき・生育・収穫期", "tasks":["1箇所に4～5粒播種","本葉が出たら2本⇒1本に間引と追肥","太ってきたら収穫"]},
        {"months": range(7, 9), "label": "📋 7~8月:夏は難しい時期", "tasks":["秋まきに向けて土づくりをしておく"]},
        {"months": range(9, 11), "label": "📋 9~10月:秋まきスタート!", "tasks":["9月上旬～10月上旬播種1箇所に4～5粒播種残っている実を収穫する","株を片付けて土を休ませる"]},
        {"months": range(11, 13), "label": "📋 11~12月：秋まき大根の収穫", "tasks":["葉が黄色くなり始めたら収穫サイン"]}
    ],

    "ほうれん草":[
        {"months": range(1, 3), "label": "📋 1~2月:冬越し・収穫", "tasks":["ビニールトンネルで保温"]},
        {"months": range(3, 5), "label": "📋 3~4月:春まきスタート", "tasks":["すじまき(1㎝間隔)で種を蒔く","本葉が2～3枚になったら間引く"]},
        {"months": range(5, 7), "label": "📋 5～6月:春まき収穫期", "tasks":["葉が育ってきたら順次収穫する","とう立ちする前に早めに収穫を"]},
        {"months": range(7, 9), "label": "📋 7~8月:夏は難しい時期", "tasks":["夏まき専用品種を選べば可能","なるべく涼しい場所で育てる"]},
        {"months": range(9, 11), "label": "📋 9~10月：秋まきスタート!", "tasks":["2〜3週間おきにずらしてすじまき（1cm間隔）","本葉2〜3枚で間引く"]},
        {"months": range(11, 13), "label": "📋 11~12月：冬越し準備", "tasks":["20cm以上で収穫", "霜が強い地域はビニールトンネルで保温"]}
    ],

    "キュウリ": [
    {"months": range(4, 6),  "label": "4~5月：植え付け",   "tasks": ["霜が終わったら苗を植える", "支柱を立てて誘引する"]},
    {"months": range(6, 9),  "label": "6~8月：収穫期",     "tasks": ["毎日収穫する（大きくなりすぎ注意）", "水やりをたっぷり"]},
],
}

# ===== 野菜と月を渡すと、ラベルと作業リストを返す関数 =====

def get_tasks(vegetable, month):
    #野菜のデータが辞書にあるか確認
    if vegetable not in VEGETABLE_DATA:
        return "データなし",["この野菜はまだ登録されていません。"]
    
    #月に合うデータを探す
    for data in VEGETABLE_DATA[vegetable]:
        if month in data["months"]:
            return data["label"], data["tasks"]
        
    return "該当なし", ["この月のデータが見つかりませんでした"]

# ===== メイン処理 =====

print("=" *45)
print("🌱 野菜の月別作業チェッカー  ver.3")
print("=" *45)

# 今月を自動で取得
now_month = datetime.now().month
print(f"\n📅 今月は {now_month}月 です\n")

# 育てている野菜のリスト（ここを書き換えて使用する）
my_vegtables = ["トマト", "大根", "ほうれん草", "キュウリ"]

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