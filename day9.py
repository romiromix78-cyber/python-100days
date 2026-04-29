# 🌱野菜の月別作業チェッカー ver.5 改
import os
from datetime import datetime,timedelta

# 野菜ごとの栽培日数データ（タプルで管理）

GROW_DAYS = {
    "トマト":   (90, "植え付けから収穫まで約90日"),
    "大根":     (60, "種まきから収穫まで約60日"),
    "ほうれん草":(40, "種まきから収穫まで約40日"),
    "キュウリ":  (60, "植え付けから収穫まで約60日"),
}

# --- 野菜の月別作業データ（day6 から引継ぎ） ---

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
        {"months": range(9, 11), "label": "📋 9~10月:秋まきスタート!", "tasks":["9月上旬～10月上旬　1箇所に4～5粒播種","株を片付けて土を休ませる"]},
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
    {"months": range(1, 4),  "label": "📋 1~3月：準備期間",   "tasks": ["品種を選んでおく（接ぎ木苗がおすすめ）", "支柱・ネットの準備"]},
    {"months": range(4, 6),  "label": "📋 4~5月：植え付け",   "tasks": ["霜が終わったら苗を植える", "支柱を立てて誘引する"]},
    {"months": range(6, 9),  "label": "📋 6~8月：収穫期",     "tasks": ["毎日収穫する（大きくなりすぎ注意）", "水やりをたっぷり"]},
    {"months": range(9, 13),  "label": "📋 9~12月：片付け",     "tasks": ["株を片付けて土を休ませる", "来年に向けて堆肥を入れておく"]},
],
}

# ===== ファイル名の定数 =====
SAVE_FILE = "my_vegetables.txt"
PLANTING_FILE = "planting_dates.txt" #植え付け日の記録
LOG_FILE = "work_log.txt" #作業記録ログ

# ===== 今日追加した共通関数（リファクタリング）=====
def input_number(prompt, min_val, max_val):
    #数字の入力と範囲チェックをまとめた関数

    value = input(prompt).strip()
    if not value.isdigit():
        print("⚠️  数字を入力してください")
        return None
    num = int(value)
    if num <min_val or num > max_val:
        print(f"⚠️ {min_val} ～{max_val} の数字を入力してください") 
        return None
    return num

def show_vegtable_list(my_vegtables):
    #登録中の野菜を番号付きで表示する
    for i, veg in enumerate(my_vegetables):
        print(f" {i + 1}, {veg}")

# ===== ファイルの読み書き関数 (day7からの引継ぎ）=====
def load_vegtables():
    #ファイルから野菜リストを読み込む
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            vegetables = [line.strip() for line in f.readlines() if line.strip()]
            print(f"💾 {SAVE_FILE} を読み込みました")
            return vegetables
    else:
        print("📝 初回起動です。育てている野菜を登録してください！")
        return []

def save_vegtables(vegetables):
    #野菜リストをファイルに保存する
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        for veg in vegetables:
            f.write(veg + "\n")
    print(f"💾 {SAVE_FILE} に保存しました")

# ===== 作業データ取得関数 (day6から引継ぎ）=====            

def get_tasks(vegetable, month):
    #野菜のデータが辞書にあるか確認
    if vegetable not in VEGETABLE_DATA:
        return "データなし",["この野菜はまだ登録されていません。"]
    
    #月に合うデータを探す
    for data in VEGETABLE_DATA[vegetable]:
        if month in data["months"]:
            return data["label"], data["tasks"]
        
    return "該当なし", ["この月のデータが見つかりませんでした"]

# ===== 野菜の登録・削除関数 (input_number関数を活用）=====

# 野菜を追加登録する関数
def add_vegetable(my_vegetables):
    print("\n登録できる野菜:",",".join(VEGETABLE_DATA.keys()))
    name = input("追加する野菜名を入力してください >>").strip()

    if name not in VEGETABLE_DATA:
        print(f"⚠️  「{name}」はデータがありません。上記から選んでください")
    elif name in my_vegetables:
        print(f"⚠️  「{name}」はすでに登録されています")
    else:
        my_vegetables.append(name)
        print(f"✅ 「{name}」を追加しました！")

# 野菜を削除する関数
def remove_vegetable(my_vegetables):
    if not my_vegetables:
        print(f"⚠️  登録されている野菜がありません") 
        return
    print("\n登録中の野菜:")
    show_vegtable_list(my_vegetables) #共通関数を使うようにした
    num = input_number("削除する番号を入力してください >>", 1, len(my_vegetables))
    if num is None:
        return
    removed = my_vegetables.pop(num - 1) #pop()でリストから取り出して削除      
    print(f"🗑️  「{removed}」を削除しました")

# ===== 植え付け日を登録して収穫予定日を計算 (day8から引継ぎ）=====

def register_planting(my_vegetables):
    if not my_vegetables:
        print("⚠️  野菜が登録されていません")
        return
    print("\n植え付け日を登録する野菜を選んでください。")
    show_vegtable_list(my_vegetables) 
    num = input_number("番号を入力してください >> ", 1, len(my_vegetables))
    if num is None:
        return
    veg = my_vegetables[num - 1]
    date_input = input(f" 「{veg}」 の植え付け日を入力してください(例:2025-03-15)>>").strip()
    try:
        planting_date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("日付の形式が正しくありません（例: 2026-03-15)")    
        return    
    #  タプルから栽培日数と備考を取り出す（アンパック）
    if veg in GROW_DAYS:
        days, note = GROW_DAYS[veg]
        harvest_date = planting_date + timedelta(days=days)
        today = datetime.now()
        
        #残り日数の計算（予定日　-　今日）
        remaining = (harvest_date - today).days

        print(f"\n🌱 {veg} の栽培スケジュール")
        print(f"　植え付け日　　:{planting_date.strftime('%Y年%m月%d日')}")
        print(f"　収穫予定日　　:{harvest_date.strftime('%Y年%m月%d日')} ({note}) ")

        if remaining > 0:
            print(f"  収穫まであと　:{remaining} 日！")

        elif -30 <= remaining <= -14:
            #予定日から14日以上30日以内の場合（remainingが　-14～-30　の時）
            print(f"  収穫まであと　:{abs(remaining)} 日過ぎています。そろそろ収穫を！")

            #植え付け日をファイルに保存（上書き保存で最新を管理）
        with open(PLANTING_FILE, "a", encoding="utf-8") as f:
            f.write(f"{date_input} | {veg} | 収穫予定: {harvest_date.strftime('%Y年%m月%d日')}\n")
        print(f"💾 植え付け日を {PLANTING_FILE} に保存しました")

    else:
        print(f"⚠️ 「{veg}」の栽培日数データがありません")  

# ===== 作業を記録する（デフォルト引数を追加） =====
def log_work(my_vegetables):
    if not my_vegetables:
        print("⚠️  野菜が登録されていません")
        return
    print("\n作業を記録する野菜を選んでください:")
    show_vegtable_list(my_vegetables)  #共通関数を使うようにした
    num = input_number("番号を入力してください>>", 1, len(my_vegetables))
    if num is None:
        return
    veg = my_vegetables[num - 1]
    work = input(f" 「{veg}」で今日やった作業をを入力してください>>").strip()    
    
    if not work:
        print("⚠️ 作業内容を入力してください")
        return
    today_str = datetime.now().strftime("%Y年%m月%d日")

    #"a" （追記）モードで書き込む
    with open(LOG_FILE, "a", encoding="utf-8",newline="") as f:
        f.write(f"{today_str} | {veg} | {work}\n")

    print(f"✅ 記録しました！{today_str} | {veg} | {work}\n") 

# ===== 作業を見る (引数を追加)=====         
def show_log(filename=LOG_FILE, last_n=10):
    #filename: 読み込むファイル（デフォルト: work_log.txt)
    #last_n  : 表示する行数（デフォルト: 直近10件）

    if not os.path.exists(filename):
        print("⚠️ まだ作業記録がありません")
        return
    
    print(f"\n 📖 作業記録（直近{last_n}）件")
    print("=" * 45)
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("記録がありません")
    else:
        for line in lines[-last_n:]:
            print(" ", line.strip())
    print("=" * 45)            

# ===== メイン処理 =====

print("=" *45)
print("🌱 野菜の月別作業チェッカー  ver.5")
print("=" *45)

# 起動時にファイルから野菜リストを読み込む
my_vegetables = load_vegtables()
now_month = datetime.now().month
print(f"\n📅 今月は {now_month}月 です\n")

# ===== メイン処理 =====

while True:
    #登録中の野菜を表示
    if my_vegetables:
        print(f"\n🌾 登録中: {','.join(my_vegetables)}")
    else:
        print("\n🌾 登録中の野菜はありません")

    print("\n何をしますか？")
    print(" 1. 今月の作業を確認する")
    print(" 2. 野菜の追加登録する")
    print(" 3. 野菜を削除する")
    print(" 4. 植え付け日を登録して収穫予定日を確認する")
    print(" 5. 今日の作業を記録する")
    print(" 6. 作業記録を見る")
    print(" 7. 終了する")

    choice = input("\n番号を入力してください ").strip()

# --- 1. 作業確認 ---
    
    if choice == "1":
        if not my_vegetables:
                print("⚠️  野菜が登録されていません。まず「2」で登録してください")
                continue

        print(f"\n📅 {now_month} 月の作業\n" + "=" * 45)
        for veg in my_vegetables:
                label, tasks = get_tasks(veg, now_month)
                print(f"\n 【{veg}】の作業")
                print(f"{label}")
                for task in tasks:
                    print(f"  ✓ {task}")
                print("=" * 45)

    # --- 2. 野菜を追加 ---
    elif choice == "2":
        add_vegetable(my_vegetables) #追加関数

# --- 3. 野菜を削除 ---
    elif choice == "3":
        remove_vegetable(my_vegetables) #削除関数

# --- 4. 植え付け日を登録して収穫予定日の確認 ---      
    elif choice == "4":
        register_planting(my_vegetables)

# --- 5. 今日の作業の確認 ---
    elif choice == "5":
        log_work(my_vegetables)

# --- 6. 作業記録を見る ---
    elif choice == "6":
        show_log()

# --- 7. 終了 ---
    elif choice == "7":
        save_vegtables(my_vegetables)
        print("\n🌿 またいつでも使ってね！")
        break

    else:
        print("⚠️  1～7の番号を入力してください")

