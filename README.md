# US_CPI
# 📈 米国消費者物価指数 (CPI) 分析ツール

## 💡 概要

本スクリプトは、**米国消費者物価指数（CPI）**のデータを取得し、経済分析で最も重要視される**前年同月比（YoY）**の変化率をグラフで可視化する単純なPythonツールです。

データは、セントルイス連邦準備銀行（FRED）のAPIから直接取得します。

---

## 📊 使用データと計算内容

| 項目 | 詳細 |
| :--- | :--- |
| **指標** | CPIAUCSL (All Urban Consumers: All Items, Seasonally Unadjusted) |
| **ソース** | FRED (Federal Reserve Economic Data) |
| **計算** | 前年同月比変化率 (CPI MoM Change (%)) を計算し、パーセント表示でプロット |

---

## 🚀 実行環境とセットアップ

### 必要なライブラリ

このコードを実行するには、以下のライブラリが必要です。

```bash
pip install pandas numpy matplotlib pandas-datareader