<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>楽天証券 NISA成長投資枠 ファンド分析インフォグラフィック</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', 'Noto Sans JP', sans-serif;
            background-color: #EFF6FF; /* Light Background */
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px; /* Default max-width */
            margin-left: auto;
            margin-right: auto;
            height: 300px; /* Default height */
            max-height: 400px; /* Default max-height */
        }
        @media (min-width: 768px) { /* md breakpoint */
            .chart-container {
                height: 350px;
            }
        }
        .stat-card h3 {
            color: #1A75D2; /* Secondary Blue */
        }
        .section-title {
            color: #0A488B; /* Primary Blue */
        }
        /* Custom styles for HTML flow chart */
        .flowchart-step {
            background-color: #FFFFFF;
            border: 2px solid #1A75D2;
            color: #0A488B;
            padding: 1rem;
            border-radius: 0.5rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .flowchart-arrow {
            font-size: 2rem;
            color: #1A75D2;
            margin: 0.5rem 0;
            align-self: center;
        }
        .tooltip-custom {
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 8px;
            border-radius: 4px;
            font-size: 0.875rem;
            pointer-events: none;
        }
        .table-responsive {
            overflow-x: auto;
        }
        table th, table td {
            white-space: nowrap;
        }
        /* <!-- 
            Infographic Narrative Plan Summary:
            1. Introduction: NISA Growth Investment Framework overview.
            2. Top Fund Highlights: Key metrics of top 2-3 funds.
            3. Ranking Overview Table: Top 10 funds comparison.
            4. Fund Type Analysis: By region and strategy (Donut charts).
            5. Cost Comparison: Trust fees (Bar chart).
            6. Risk-Return Distribution: Scatter plot.
            7. Net Asset Growth: Current net assets (Bar chart).
            8. Investor Considerations: Key points list.
            9. NISA Usage Flow: HTML/CSS flowchart.
            10. 30-Year Investment Simulation: Text and Bar chart. (NEW)
            11. Conclusion.

            Color Palette Selection: Brilliant Blues (with accents)
            - Primary Blue: #0A488B
            - Secondary Blue: #1A75D2
            - Accent Green: #2ECC71
            - Accent Yellow: #F1C40F
            - Light Background: #EFF6FF
            - Card Background: #FFFFFF
            - Text Dark: #1F2937
            - Text Light: #6B7280

            Visualization Choices Summary (Confirming NO SVG, NO MERMAID JS):
            - NISA Overview: Single Big Number (HTML/Tailwind) - Goal: Inform. Justification: Direct info.
            - Top Fund Highlights (Net Assets, Returns): Single Big Number (HTML), Bar Chart (Chart.js Canvas) - Goal: Inform/Compare. Justification: Quick highlights.
            - Ranking Table: HTML Table (HTML/Tailwind) - Goal: Organize/Compare. Justification: Detailed comparison.
            - Fund Type Analysis (Region/Strategy - Net Asset Share): Donut Chart (Chart.js Canvas) - Goal: Compare (composition). Justification: Visual proportion.
            - Cost Comparison (Trust Fees): Bar Chart (Chart.js Canvas) - Goal: Compare. Justification: Clear cost difference.
            - Risk-Return Distribution (StdDev vs Returns): Scatter Plot (Chart.js Canvas) - Goal: Relationships. Justification: Visualize risk/reward.
            - Net Asset Comparison: Bar Chart (Chart.js Canvas) - Goal: Compare. Justification: Fund size.
            - Investor Considerations: List with Unicode Icons (HTML/Tailwind) - Goal: Organize/Inform. Justification: Concise advice.
            - NISA Usage Flow: Flow Chart (Structured HTML/CSS with Tailwind, Unicode arrows) - Goal: Organize. Justification: Step-by-step guide.
            - 30-Year Simulation: Bar Chart (Chart.js Canvas) and Text (HTML/Tailwind) - Goal: Compare/Inform. Justification: Long-term projection. (NEW)

            Confirmation: NEITHER Mermaid JS NOR SVG were used anywhere in this output.
        --> */
    </style>
</head>
<body class="bg-slate-50 text-gray-800">

    <header class="bg-[#0A488B] text-white py-8 px-4 text-center">
        <h1 class="text-4xl font-bold mb-2">楽天証券 NISA成長投資枠</h1>
        <p class="text-xl">人気ファンド徹底分析インフォグラフィック</p>
    </header>

    <nav class="sticky top-0 bg-white/80 backdrop-blur-md shadow-md z-50">
        <div class="container mx-auto px-4 py-3 flex flex-wrap justify-center space-x-2 md:space-x-4">
            <a href="#nisa-overview" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">NISA概要</a>
            <a href="#top-funds" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">注目ファンド</a>
            <a href="#ranking-table" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">ランキング</a>
            <a href="#fund-analysis" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">タイプ別分析</a>
            <a href="#cost-comparison" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">コスト比較</a>
            <a href="#risk-return" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">リスクとリターン</a>
            <a href="#simulation" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">30年積立シミュレーション</a>
            <a href="#considerations" class="text-sm md:text-base text-[#1A75D2] hover:text-[#0A488B] font-medium">投資の心得</a>
        </div>
    </nav>

    <main class="container mx-auto p-4 md:p-8">

        <section id="nisa-overview" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-6 section-title">NISA成長投資枠とは？</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                2024年から始まった新しいNISA制度における「成長投資枠」は、年間240万円まで、最大1,200万円の非課税保有限度額内で、投資信託や国内外の株式など幅広い商品に投資できる制度です。つみたて投資枠よりも多様な選択肢があり、より積極的な資産形成を目指すことができます。
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
                <div class="bg-white p-6 rounded-lg shadow-lg text-center stat-card">
                    <h3 class="text-2xl font-semibold mb-2">年間投資枠</h3>
                    <p class="text-5xl font-bold text-[#0A488B]">240<span class="text-2xl">万円</span></p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg text-center stat-card">
                    <h3 class="text-2xl font-semibold mb-2">非課税保有限度額</h3>
                    <p class="text-5xl font-bold text-[#0A488B]">1,200<span class="text-2xl">万円</span></p>
                    <p class="text-sm text-gray-600">(NISA全体では1,800万円)</p>
                </div>
            </div>
            <p class="text-center mt-6 text-gray-600 text-sm">
                出所：楽天証券NISA成長投資枠トップ30ファンド詳細分析レポート（2025年5月27日時点情報に基づく）
            </p>
        </section>

        <section id="top-funds" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">今、注目のトップファンド</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                楽天証券のNISA成長投資枠で特に人気を集めている代表的なファンドをいくつかご紹介します。これらのファンドは、多くの投資家から支持され、大きな純資産総額を誇っています。
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#0A488B] mb-2">eMAXIS Slim 米国株式(S&P500)</h3>
                    <p class="text-sm text-gray-600 mb-1">純資産総額: <span class="font-bold text-lg">67,377</span> 億円 (2025/5/27)</p>
                    <p class="text-sm text-gray-600 mb-3">信託報酬: <span class="font-bold text-lg">0.0814%</span> (年率・税込)</p>
                    <div class="chart-container h-48 md:h-56">
                        <canvas id="sp500ReturnChart"></canvas>
                    </div>
                    <p class="text-sm text-gray-700 mt-3">S&P500指数に連動し、低コストで米国主要企業500社に分散投資。長期投資のコアとして人気。</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#0A488B] mb-2">eMAXIS Slim 全世界株式(オルカン)</h3>
                    <p class="text-sm text-gray-600 mb-1">純資産総額: <span class="font-bold text-lg">57,910</span> 億円 (2025/5/27)</p>
                    <p class="text-sm text-gray-600 mb-3">信託報酬: <span class="font-bold text-lg">0.05775%</span> (年率・税込)</p>
                    <div class="chart-container h-48 md:h-56">
                        <canvas id="allCountryReturnChart"></canvas>
                    </div>
                    <p class="text-sm text-gray-700 mt-3">MSCI ACWIに連動。1本で全世界の株式に低コストで国際分散投資。グローバルな成長を捉える。</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg md:col-span-1 lg:col-span-1">
                    <h3 class="text-xl font-semibold text-[#0A488B] mb-2">iFreeNEXT FANG+インデックス</h3>
                    <p class="text-sm text-gray-600 mb-1">純資産総額: <span class="font-bold text-lg">5,776</span> 億円 (2025/5/27)</p>
                    <p class="text-sm text-gray-600 mb-3">信託報酬: <span class="font-bold text-lg">0.7755%</span> (年率・税込)</p>
                     <div class="chart-container h-48 md:h-56">
                        <canvas id="fangPlusReturnChart"></canvas>
                    </div>
                    <p class="text-sm text-gray-700 mt-3">米国の主要ハイテク10銘柄に集中投資。高い成長期待がある一方、高ボラティリティが特徴。</p>
                </div>
            </div>
             <p class="text-center mt-6 text-gray-600 text-sm">
                各ファンドのリターンデータは2025年4月30日時点のものです。
            </p>
        </section>

        <section id="ranking-table" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">上位ファンド徹底比較 (トップ10)</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                楽天証券NISA成長投資枠の残高ランキング上位10ファンドの主要情報を一覧で比較できます。ファンド名、運用会社、主な投資対象、リターン、信託報酬、純資産額などを確認し、ご自身の投資戦略に合うファンドを見つけましょう。
            </p>
            <div class="bg-white p-4 md:p-6 rounded-lg shadow-lg table-responsive">
                <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">順位</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ファンド名</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">運用会社</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">主要投資対象</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">1年リターン(%)</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">信託報酬(%)</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">純資産額(億円)</th>
                            <th class="px-3 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">一言概要</th>
                        </tr>
                    </thead>
                    <tbody id="fundRankingsTableBody" class="bg-white divide-y divide-gray-200">
                    </tbody>
                </table>
            </div>
            <p class="text-center mt-6 text-gray-600 text-sm">
                リターンは特記ない限り年率。データ時点: 純資産額2025/5/27、リターンはファンドにより異なる(主に2025/4/30または2025/5/23)。詳細は各ファンド情報をご確認ください。
            </p>
        </section>

        <section id="fund-analysis" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">投資スタイル別に見る人気ファンド</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                投資家の戦略や嗜好は様々です。ここでは、純資産総額を基に、人気のファンドを投資対象地域別と投資戦略別に分類し、その構成比を見てみましょう。
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#0A488B] mb-4 text-center">投資対象地域別 純資産シェア (上位3種)</h3>
                    <p class="text-sm text-gray-600 mb-4 text-center">eMAXIS Slimシリーズの代表的な地域特化型ファンドの純資産額から見たシェアです。</p>
                    <div class="chart-container h-72 md:h-80">
                        <canvas id="regionShareChart"></canvas>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#0A488B] mb-4 text-center">投資戦略別 純資産シェア (代表5種)</h3>
                     <p class="text-sm text-gray-600 mb-4 text-center">主要な投資戦略を持つファンドの純資産額から見たシェアです。</p>
                    <div class="chart-container h-72 md:h-80">
                        <canvas id="strategyShareChart"></canvas>
                    </div>
                </div>
            </div>
             <p class="text-center mt-6 text-gray-600 text-sm">
                純資産額データは2025年5月27日時点。
            </p>
        </section>

        <section id="cost-comparison" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">コストを制する者が投資を制す：信託報酬比較</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                投資信託のコスト、特に信託報酬は長期的なリターンに大きく影響します。ランキング上位ファンドの信託報酬を比較し、低コスト運用の重要性を確認しましょう。
            </p>
            <div class="bg-white p-6 rounded-lg shadow-lg">
                 <div class="chart-container" style="height: 400px; max-height: 500px;">
                    <canvas id="trustFeeChart"></canvas>
                </div>
            </div>
             <p class="text-center mt-6 text-gray-600 text-sm">
                信託報酬は年率・税込。
            </p>
        </section>

        <section id="risk-return" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">あなたに合うのは？リスク・リターン分布</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                ファンドのリスク（標準偏差）とリターン（過去3年間の年率リターン）を散布図で示します。一般的に、高いリターンを期待できるファンドはリスクも高くなる傾向があります。ご自身のリスク許容度に合ったファンド選びの参考にしてください。
            </p>
            <div class="bg-white p-6 rounded-lg shadow-lg">
                <div class="chart-container" style="height: 400px; max-height: 500px;">
                    <canvas id="riskReturnScatterChart"></canvas>
                </div>
            </div>
             <p class="text-center mt-6 text-gray-600 text-sm">
                リターン、標準偏差のデータ時点はファンドにより異なります。3年リターンがないファンドは表示されていません。
            </p>
        </section>
        
        <section id="net-assets-comparison" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">どれだけ選ばれている？純資産総額ランキング</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                純資産総額は、そのファンドがどれだけ多くの投資家から資金を集めているかを示す指標の一つです。ランキング上位ファンドの純資産総額を見てみましょう。
            </p>
            <div class="bg-white p-6 rounded-lg shadow-lg">
                <div class="chart-container" style="height: 400px; max-height: 500px;">
                    <canvas id="netAssetsChart"></canvas>
                </div>
            </div>
            <p class="text-center mt-6 text-gray-600 text-sm">
                純資産総額データは2025年5月27日時点。
            </p>
        </section>

        <section id="simulation" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">30年間毎月5万円積立シミュレーション</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                主要ファンドに毎月5万円を30年間積み立てた場合の評価額を、過去の実績リターン（5年リターン優先、次いで3年、1年）を基にシミュレーションしました。総投資額は18,000,000円です。
                <strong class="text-red-600">これは過去のデータに基づく試算であり、将来の成果を保証するものではありません。</strong>参考情報としてご覧ください。
            </p>
            <div class="bg-white p-6 rounded-lg shadow-lg mb-8">
                <div class="chart-container" style="height: 450px; max-height: 600px;">
                    <canvas id="simulationChart"></canvas>
                </div>
            </div>
            <div id="simulationDetails" class="grid grid-cols-1 md:grid-cols-2 gap-6">
                
            </div>
            <p class="text-center mt-6 text-gray-600 text-sm">
                シミュレーションは税金や手数料を考慮していません。リターンデータはファンドにより参照期間が異なります。
            </p>
        </section>

        <section id="considerations" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">賢い投資家になるための5つの心得</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                NISA成長投資枠を有効活用し、賢く資産形成を進めるために、以下のポイントを心に留めておきましょう。
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#1A75D2] mb-2 flex items-center"><span class="text-2xl mr-2">🎯</span>投資目標と期間</h3>
                    <p class="text-gray-700">ライフプランに合わせた目標設定と、それに必要な期間を明確にしましょう。</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#1A75D2] mb-2 flex items-center"><span class="text-2xl mr-2">⚖️</span>リスク許容度</h3>
                    <p class="text-gray-700">自身が許容できるリスクの範囲を理解し、無理のないファンドを選びましょう。</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#1A75D2] mb-2 flex items-center"><span class="text-2xl mr-2">🧺</span>分散投資</h3>
                    <p class="text-gray-700">異なる資産や地域に分散することで、ポートフォリオ全体のリスクを低減させましょう。</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg">
                    <h3 class="text-xl font-semibold text-[#1A75D2] mb-2 flex items-center"><span class="text-2xl mr-2">💰</span>コスト意識</h3>
                    <p class="text-gray-700">信託報酬などのコストは長期リターンに影響します。低コストを意識しましょう。</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-lg lg:col-span-2">
                    <h3 class="text-xl font-semibold text-[#1A75D2] mb-2 flex items-center"><span class="text-2xl mr-2">🔄</span>情報収集と見直し</h3>
                    <p class="text-gray-700">定期的に運用状況を確認し、市場や自身の状況変化に合わせてポートフォリオを見直しましょう。</p>
                </div>
            </div>
        </section>
        
        <section id="nisa-usage-flow" class="mb-12 scroll-mt-20">
            <h2 class="text-3xl font-bold text-center mb-8 section-title">NISA成長投資枠 活用ステップ</h2>
            <p class="text-lg text-gray-700 mb-6 text-center max-w-3xl mx-auto">
                NISA成長投資枠を始めるための基本的なステップをご紹介します。計画的に進めましょう。
            </p>
            <div class="flex flex-col md:flex-row justify-around items-center space-y-4 md:space-y-0 md:space-x-4">
                <div class="flowchart-step"><span>1. NISA口座開設</span><p class="text-xs mt-1">証券会社を選び口座を開設</p></div>
                <div class="flowchart-arrow hidden md:block">➔</div>
                <div class="flowchart-arrow block md:hidden">⬇</div>
                <div class="flowchart-step"><span>2. 投資方針決定</span><p class="text-xs mt-1">目標・リスク許容度を明確に</p></div>
                <div class="flowchart-arrow hidden md:block">➔</div>
                <div class="flowchart-arrow block md:hidden">⬇</div>
                <div class="flowchart-step"><span>3. ファンド選定</span><p class="text-xs mt-1">情報収集し商品を選択</p></div>
                <div class="flowchart-arrow hidden md:block">➔</div>
                <div class="flowchart-arrow block md:hidden">⬇</div>
                <div class="flowchart-step"><span>4. 投資実行</span><p class="text-xs mt-1">積立設定またはスポット購入</p></div>
                <div class="flowchart-arrow hidden md:block">➔</div>
                 <div class="flowchart-arrow block md:hidden">⬇</div>
                <div class="flowchart-step"><span>5. 定期的な確認</span><p class="text-xs mt-1">運用状況をチェックし見直し</p></div>
            </div>
        </section>


        <section class="text-center py-8">
            <p class="text-gray-700">NISA成長投資枠を賢く活用し、あなたの未来のための資産形成を始めましょう。</p>
            <a href="https://www.rakuten-sec.co.jp/nisa/" target="_blank" rel="noopener noreferrer" class="mt-4 inline-block bg-[#1A75D2] text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:bg-[#0A488B] transition duration-300">
                楽天証券でNISAを詳しく見る
            </a>
        </section>

    </main>

    <footer class="bg-[#0A488B] text-white text-center p-6 mt-12">
        <p class="text-sm">&copy; 2025 NISA成長投資枠分析インフォグラフィック. All rights reserved.</p>
        <p class="text-xs mt-1">本情報は、楽天証券NISA成長投資枠トップ30ファンド詳細分析レポート(2025年5月27日時点の情報に基づく)等を参考に作成されています。投資判断はご自身の責任において行ってください。過去の実績は将来の成果を保証するものではありません。</p>
    </footer>

    <script>
        const fundData = [
            { rank: 1, name: 'eMAXIS Slim 米国株式（S&P500）', shortName: 'Slim S&P500', manager: '三菱UFJアセット', strategy: 'S&P500連動、低コスト', target: '米国株(S&P500)', return1Y: -0.2, return3Y: 15.2, return5Y: 21.9, stdDev1Y: 19.97, trustFee: 0.0814, netAssets: 67377, summary: '米国代表株500社に低コスト分散。' },
            { rank: 2, name: 'eMAXIS Slim 全世界株式（オール・カントリー）', shortName: 'Slimオルカン', manager: '三菱UFJアセット', strategy: 'MSCI ACWI連動、低コスト', target: '全世界株(ACWI)', return1Y: 0.2, return3Y: 14.0, return5Y: 19.6, stdDev1Y: 13.63, trustFee: 0.05775, netAssets: 57910, summary: '1本で世界中に低コスト国際分散。' },
            { rank: 3, name: '楽天・プラス・S&P500インデックス・ファンド', shortName: '楽天+S&P500', manager: '楽天投信投資顧問', strategy: 'S&P500連動、低コスト、楽天ポイント', target: '米国株(S&P500)', return1Y: 2.62, return3Y: null, return5Y: null, stdDev1Y: 20.41, trustFee: 0.077, netAssets: 5201, summary: '楽天版 低コストS&P500投信。' },
            { rank: 4, name: '楽天・プラス・オールカントリー株式インデックス・ファンド', shortName: '楽天+オルカン', manager: '楽天投信投資顧問', strategy: 'MSCI ACWI連動、低コスト、楽天ポイント', target: '全世界株(ACWI)', return1Y: 2.77, return3Y: null, return5Y: null, stdDev1Y: 18.60, trustFee: 0.0561, netAssets: 3588, summary: '楽天版 低コスト全世界株投信。' },
            { rank: 5, name: 'iFreeNEXT FANG+インデックス', shortName: 'FANG+', manager: '大和アセット', strategy: 'NYSE FANG+連動、ハイテク10銘柄集中', target: '米国ハイテク株10銘柄', return1Y: 19.18, return3Y: 44.09, return5Y: 36.29, stdDev1Y: 31.38, trustFee: 0.7755, netAssets: 5776, summary: '米ハイテク大手に集中、高成長狙い。' },
            { rank: 6, name: '楽天・全米株式インデックス・ファンド', shortName: '楽天VTI', manager: '楽天投信投資顧問', strategy: 'CRSP USトータル・マーケット連動', target: '米国株全体(約4000銘柄)', return1Y: 2.04, return3Y: 18.35, return5Y: 21.52, stdDev1Y: 20.49, trustFee: 0.162, netAssets: 16865, summary: 'S&P500より広範な米国株に分散。' },
            { rank: 7, name: '楽天・シュワブ・高配当株式・米国ファンド（四半期決算型）', shortName: '楽天SCHD', manager: '楽天投信投資顧問', strategy: 'SCHD ETF投資、米国高配当株、年4回分配', target: '米国高配当株(約100銘柄)', return1Y: -27.98, return3Y: null, return5Y: null, stdDev1Y: 18.90, trustFee: 0.192, netAssets: 1433, summary: '米国高配当株でインカム狙い。' },
            { rank: 8, name: '楽天・プラス・NASDAQ-100インデックス・ファンド', shortName: '楽天+NASDAQ100', manager: '楽天投信投資顧問', strategy: 'Nasdaq-100連動、米ハイテク・成長企業', target: '米国株(Nasdaq100)', return1Y: 4.25, return3Y: null, return5Y: null, stdDev1Y: 25.39, trustFee: 0.198, netAssets: 915, summary: '米ハイテク・成長企業へ投資。' },
            { rank: 9, name: '三菱UFJ 純金ファンド', shortName: '純金ファンド', manager: '三菱UFJアセット', strategy: '国内金価格連動、現物ETF投資', target: '国内金価格(金の果実ETF)', return1Y: 28.13, return3Y: 25.11, return5Y: 19.51, stdDev1Y: 16.29, trustFee: 0.99, netAssets: 4022, summary: '金価格投資、インフレヘッジ。' },
            { rank: 10, name: 'eMAXIS Slim 先進国株式インデックス', shortName: 'Slim先進国株', manager: '三菱UFJアセット', strategy: 'MSCIコクサイ連動、低コスト', target: '日本除く先進国株', return1Y: 3.26, return3Y: 18.50, return5Y: 21.40, stdDev1Y: 18.89, trustFee: 0.09889, netAssets: 8555, summary: '日本除く先進国株に低コスト分散。' }
        ];

        const PALETTE = {
            primaryBlue: '#0A488B',
            secondaryBlue: '#1A75D2',
            accentGreen: '#2ECC71',
            accentYellow: '#F1C40F',
            accentRed: '#E74C3C',
            textDark: '#1F2937',
            textLight: '#6B7280',
            lightBlue: '#AED6F1',
            midBlue: '#5DADE2',
            chartColors: ['#1A75D2', '#2ECC71', '#F1C40F', '#E74C3C', '#8E44AD', '#3498DB', '#1ABC9C', '#F39C12', '#D35400', '#2980B9']
        };
        
        function formatLabel(label, maxLength = 16) {
            if (typeof label !== 'string' || label.length <= maxLength) {
                return label;
            }
            const words = label.split(' ');
            const lines = [];
            let currentLine = '';
            for (const word of words) {
                if ((currentLine + word).length > maxLength && currentLine.length > 0) {
                    lines.push(currentLine.trim());
                    currentLine = word;
                } else {
                    currentLine += (currentLine.length > 0 ? ' ' : '') + word;
                }
            }
            if (currentLine.length > 0) {
                lines.push(currentLine.trim());
            }
            return lines;
        }

        const commonChartOptions = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: PALETTE.textDark,
                        font: { size: 10 }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0,0,0,0.8)',
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    callbacks: {
                        title: function(tooltipItems) {
                            const item = tooltipItems[0];
                            let label = item.chart.data.labels[item.dataIndex];
                            if (Array.isArray(label)) {
                              return label.join(' ');
                            }
                            return label;
                        },
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += new Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY', minimumFractionDigits: 0, maximumFractionDigits: 0 }).format(context.parsed.y);
                            }
                            return label;
                        }
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: PALETTE.textLight, font: { size: 10 } },
                    grid: { display: false }
                },
                y: {
                    ticks: { 
                        color: PALETTE.textLight, 
                        font: { size: 10 },
                        callback: function(value) {
                            return new Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY', notation: 'compact' }).format(value);
                        }
                    },
                    grid: { color: '#E5E7EB' }
                }
            }
        };
        
        // Top Fund Return Charts
        if (document.getElementById('sp500ReturnChart')) {
            new Chart(document.getElementById('sp500ReturnChart'), {
                type: 'bar',
                data: {
                    labels: ['1年', '3年', '5年'],
                    datasets: [{
                        label: '年率リターン (%)',
                        data: [fundData[0].return1Y, fundData[0].return3Y, fundData[0].return5Y],
                        backgroundColor: [PALETTE.secondaryBlue, PALETTE.accentGreen, PALETTE.primaryBlue],
                    }]
                },
                options: {...commonChartOptions, indexAxis: 'y', scales: { ...commonChartOptions.scales, y: { ...commonChartOptions.scales.y, ticks: {...commonChartOptions.scales.y.ticks, callback: function(value) {return value + '%';}}}}}
            });
        }

        if (document.getElementById('allCountryReturnChart')) {
            new Chart(document.getElementById('allCountryReturnChart'), {
                type: 'bar',
                data: {
                    labels: ['1年', '3年', '5年'],
                    datasets: [{
                        label: '年率リターン (%)',
                        data: [fundData[1].return1Y, fundData[1].return3Y, fundData[1].return5Y],
                        backgroundColor: [PALETTE.secondaryBlue, PALETTE.accentGreen, PALETTE.primaryBlue],
                    }]
                },
                options: {...commonChartOptions, indexAxis: 'y', scales: { ...commonChartOptions.scales, y: { ...commonChartOptions.scales.y, ticks: {...commonChartOptions.scales.y.ticks, callback: function(value) {return value + '%';}}}}}
            });
        }
        
        if (document.getElementById('fangPlusReturnChart')) {
            new Chart(document.getElementById('fangPlusReturnChart'), {
                type: 'bar',
                data: {
                    labels: ['1年', '3年', '5年'],
                    datasets: [{
                        label: '年率リターン (%)',
                        data: [fundData[4].return1Y, fundData[4].return3Y, fundData[4].return5Y],
                        backgroundColor: [PALETTE.secondaryBlue, PALETTE.accentGreen, PALETTE.primaryBlue],
                    }]
                },
                options: {...commonChartOptions, indexAxis: 'y', scales: { ...commonChartOptions.scales, y: { ...commonChartOptions.scales.y, ticks: {...commonChartOptions.scales.y.ticks, callback: function(value) {return value + '%';}}}}}
            });
        }

        // Ranking Table
        const tableBody = document.getElementById('fundRankingsTableBody');
        if (tableBody) {
            fundData.slice(0, 10).forEach(fund => {
                const row = tableBody.insertRow();
                row.insertCell().textContent = fund.rank;
                row.insertCell().textContent = fund.name;
                row.insertCell().textContent = fund.manager;
                row.insertCell().textContent = fund.target;
                row.insertCell().textContent = fund.return1Y !== null ? fund.return1Y.toFixed(2) : 'N/A';
                row.insertCell().textContent = fund.trustFee.toFixed(4);
                row.insertCell().textContent = fund.netAssets.toLocaleString();
                row.insertCell().textContent = fund.summary;
                 Array.from(row.cells).forEach(cell => cell.classList.add('px-3', 'py-2', 'text-sm', 'text-gray-700'));
            });
        }

        // Region Share Chart
        if (document.getElementById('regionShareChart')) {
            const sp500Assets = fundData.find(f => f.shortName === 'Slim S&P500').netAssets;
            const allCountryAssets = fundData.find(f => f.shortName === 'Slimオルカン').netAssets;
            const developedCountryAssets = fundData.find(f => f.shortName === 'Slim先進国株').netAssets;
            new Chart(document.getElementById('regionShareChart'), {
                type: 'doughnut',
                data: {
                    labels: ['米国株式(S&P500)', '全世界株式(オルカン)', '先進国株式'],
                    datasets: [{
                        data: [sp500Assets, allCountryAssets, developedCountryAssets],
                        backgroundColor: [PALETTE.primaryBlue, PALETTE.secondaryBlue, PALETTE.accentGreen],
                        hoverOffset: 4
                    }]
                },
                options: {...commonChartOptions, plugins: {...commonChartOptions.plugins, tooltip: {...commonChartOptions.plugins.tooltip, callbacks: { ...commonChartOptions.plugins.tooltip.callbacks, label: function(context) { let label = context.label || ''; if (label) { label += ': '; } if (context.parsed !== null) { label += new Intl.NumberFormat('ja-JP').format(context.parsed) + ' 億円'; } return label;}}}}}
            });
        }
        
        // Strategy Share Chart
        if (document.getElementById('strategyShareChart')) {
             const strategyAssets = [
                fundData.find(f => f.shortName === 'Slim S&P500').netAssets, 
                fundData.find(f => f.shortName === 'Slimオルカン').netAssets, 
                fundData.find(f => f.shortName === 'FANG+').netAssets,       
                fundData.find(f => f.shortName === '楽天SCHD').netAssets,     
                fundData.find(f => f.shortName === '純金ファンド').netAssets   
            ];
            new Chart(document.getElementById('strategyShareChart'), {
                type: 'doughnut',
                data: {
                    labels: ['S&P500型', '全世界株式型', 'ハイテク集中型(FANG+)', '高配当型', '金投資型'],
                    datasets: [{
                        data: strategyAssets,
                        backgroundColor: [PALETTE.primaryBlue, PALETTE.secondaryBlue, PALETTE.accentYellow, PALETTE.accentGreen, PALETTE.midBlue],
                        hoverOffset: 4
                    }]
                },
                options: {...commonChartOptions, plugins: {...commonChartOptions.plugins, tooltip: {...commonChartOptions.plugins.tooltip, callbacks: { ...commonChartOptions.plugins.tooltip.callbacks, label: function(context) { let label = context.label || ''; if (label) { label += ': '; } if (context.parsed !== null) { label += new Intl.NumberFormat('ja-JP').format(context.parsed) + ' 億円'; } return label;}}}}}
            });
        }

        // Trust Fee Chart
        if (document.getElementById('trustFeeChart')) {
            const top10Funds = fundData.slice(0, 10);
            new Chart(document.getElementById('trustFeeChart'), {
                type: 'bar',
                data: {
                    labels: top10Funds.map(f => formatLabel(f.shortName, 10)),
                    datasets: [{
                        label: '信託報酬 (年率 %)',
                        data: top10Funds.map(f => f.trustFee),
                        backgroundColor: PALETTE.chartColors,
                    }]
                },
                options: {...commonChartOptions, 
                    scales: {
                        ...commonChartOptions.scales,
                        y: { ...commonChartOptions.scales.y, title: { display: true, text: '信託報酬 (%)', color: PALETTE.textDark }, ticks: {...commonChartOptions.scales.y.ticks, callback: function(value) {return value.toFixed(4) + '%';}}}
                    },
                    plugins: {...commonChartOptions.plugins, tooltip: {...commonChartOptions.plugins.tooltip, callbacks: { ...commonChartOptions.plugins.tooltip.callbacks, label: function(context) { let label = context.dataset.label || ''; if (label) { label += ': '; } if (context.parsed.y !== null) { label += context.parsed.y.toFixed(4) + '%'; } return label;}}}}
                }
            });
        }

        // Risk-Return Scatter Chart
        if (document.getElementById('riskReturnScatterChart')) {
            const scatterData = fundData
                .filter(f => f.return3Y !== null && f.stdDev1Y !== null)
                .map(f => ({
                    x: f.stdDev1Y,
                    y: f.return3Y,
                    label: f.shortName
                }));

            new Chart(document.getElementById('riskReturnScatterChart'), {
                type: 'scatter',
                data: {
                    datasets: [{
                        label: 'ファンド',
                        data: scatterData.map(d => ({x: d.x, y: d.y})),
                        backgroundColor: PALETTE.secondaryBlue,
                        pointRadius: 6,
                        pointHoverRadius: 8
                    }]
                },
                options: {
                    ...commonChartOptions,
                    plugins: {
                        ...commonChartOptions.plugins,
                        tooltip: {
                             ...commonChartOptions.plugins.tooltip,
                            callbacks: {
                                label: function(context) {
                                    const fund = scatterData[context.dataIndex];
                                    return `${fund.label}: (リスク ${fund.x.toFixed(2)}%, リターン ${fund.y.toFixed(2)}%)`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: { ...commonChartOptions.scales.x, title: { display: true, text: 'リスク (標準偏差1年 %)', color: PALETTE.textDark }, ticks: {...commonChartOptions.scales.x.ticks, callback: function(value) {return value + '%';}}},
                        y: { ...commonChartOptions.scales.y, title: { display: true, text: 'リターン (3年年率 %)', color: PALETTE.textDark }, ticks: {...commonChartOptions.scales.y.ticks, callback: function(value) {return value + '%';}}}
                    }
                }
            });
        }
        
        // Net Assets Chart
        if (document.getElementById('netAssetsChart')) {
            const top10FundsNetAssets = fundData.slice(0, 10).sort((a,b) => b.netAssets - a.netAssets);
            new Chart(document.getElementById('netAssetsChart'), {
                type: 'bar',
                data: {
                    labels: top10FundsNetAssets.map(f => formatLabel(f.shortName, 10)),
                    datasets: [{
                        label: '純資産総額 (億円)',
                        data: top10FundsNetAssets.map(f => f.netAssets),
                        backgroundColor: PALETTE.chartColors,
                    }]
                },
                options: {...commonChartOptions,
                    scales: {
                        ...commonChartOptions.scales,
                        y: { ...commonChartOptions.scales.y, title: { display: true, text: '純資産総額 (億円)', color: PALETTE.textDark }, ticks: {...commonChartOptions.scales.y.ticks, callback: function(value) { return new Intl.NumberFormat('ja-JP', { notation: 'compact' }).format(value);}}}
                    },
                    plugins: {...commonChartOptions.plugins, tooltip: {...commonChartOptions.plugins.tooltip, callbacks: { ...commonChartOptions.plugins.tooltip.callbacks, label: function(context) { let label = context.dataset.label || ''; if (label) { label += ': '; } if (context.parsed.y !== null) { label += new Intl.NumberFormat('ja-JP').format(context.parsed.y) + ' 億円'; } return label;}}}}
                }
            });
        }

        // 30-Year Simulation
        const P = 50000; // Monthly investment
        const years = 30;
        const n_months = years * 12; // Total number of months
        const totalInvested = P * n_months;

        function calculateFV(monthlyPayment, annualRate, numberOfMonths) {
            if (annualRate === null || isNaN(annualRate)) return null;
            const r = annualRate / 100;
            if (r <= -1) return 0; // Avoid issues with (1+r) being zero or negative for monthly root
            const monthlyRate = Math.pow(1 + r, 1/12) - 1;
            if (monthlyRate === 0) return monthlyPayment * numberOfMonths; // No growth, just principal
            return monthlyPayment * ( (Math.pow(1 + monthlyRate, numberOfMonths) - 1) / monthlyRate );
        }

        const simulationResults = fundData.slice(0, 10).map(fund => {
            let annualReturn = null;
            let returnPeriod = '';
            if (fund.return5Y !== null) {
                annualReturn = fund.return5Y;
                returnPeriod = '5年';
            } else if (fund.return3Y !== null) {
                annualReturn = fund.return3Y;
                returnPeriod = '3年';
            } else if (fund.return1Y !== null) {
                annualReturn = fund.return1Y;
                returnPeriod = '1年';
            }
            
            const fv = calculateFV(P, annualReturn, n_months);
            return {
                name: fund.shortName,
                fullName: fund.name,
                annualReturn: annualReturn,
                returnPeriod: returnPeriod,
                futureValue: fv
            };
        }).sort((a,b) => (b.futureValue || 0) - (a.futureValue || 0)); // Sort by FV descending

        const simulationDetailsContainer = document.getElementById('simulationDetails');
        if (simulationDetailsContainer) {
            simulationResults.forEach(res => {
                let note = '';
                if (res.annualReturn !== null && res.annualReturn < 0 && res.futureValue < totalInvested) {
                    note = '注: シミュレーションに使用した過去リターンがマイナスだったため、評価額が総投資額を下回っています。';
                } else if (res.annualReturn === null) {
                     note = '注: 過去リターンデータが利用できないため、シミュレーションできませんでした。';
                } else if (res.returnPeriod === '1年' || res.returnPeriod === '6ヶ月') {
                    note = `注: ${res.returnPeriod}という短期間のリターンに基づく長期シミュレーションであり、結果の変動が大きい可能性があります。`;
                }


                const detailHtml = `
                    <div class="bg-white p-4 rounded-lg shadow">
                        <h4 class="text-md font-semibold text-[#0A488B] mb-1">${res.fullName} (${res.name})</h4>
                        <p class="text-xs text-gray-600">使用リターン (年率): ${res.annualReturn !== null ? res.annualReturn.toFixed(2) + '%' : 'N/A'} (${res.returnPeriod}実績)</p>
                        <p class="text-xs text-gray-600">総投資額: ${totalInvested.toLocaleString()} 円</p>
                        <p class="text-sm text-gray-700 font-bold">30年後評価額: ${res.futureValue !== null ? Math.round(res.futureValue).toLocaleString() + ' 円' : '計算不可'}</p>
                        ${note ? `<p class="text-xs text-red-500 mt-1">${note}</p>` : ''}
                    </div>
                `;
                simulationDetailsContainer.innerHTML += detailHtml;
            });
        }
        
        if (document.getElementById('simulationChart')) {
            const filteredResults = simulationResults.filter(r => r.futureValue !== null);
            new Chart(document.getElementById('simulationChart'), {
                type: 'bar',
                data: {
                    labels: filteredResults.map(r => formatLabel(r.name, 10)),
                    datasets: [{
                        label: '30年後 評価額 (円)',
                        data: filteredResults.map(r => r.futureValue),
                        backgroundColor: PALETTE.chartColors,
                    }]
                },
                options: {...commonChartOptions,
                    scales: {
                        ...commonChartOptions.scales,
                        y: { 
                            ...commonChartOptions.scales.y, 
                            title: { display: true, text: '評価額 (円)', color: PALETTE.textDark },
                        }
                    }
                }
            });
        }

    </script>
</body>
</html>
