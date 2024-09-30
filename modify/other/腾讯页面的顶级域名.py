import json

# 在 js 文件中 domain-buy.zh.d3fd69005e.js
qh = {
    "TENCENT_CLOUD_TLD": [".cn", ".com", ".net", ".xyz", ".wang", ".ac.cn", ".com.cn", ".net.cn", ".中国", ".网址", ".在线", ".top", ".club", ".vip", ".beer", ".work", ".fashion", ".luxe", ".yoga", ".love", ".online", ".mobi", ".中文网", ".ltd", ".chat", ".group", ".pub", ".run", ".city", ".live", ".info", ".pro", ".red", ".网店", ".kim", ".blue", ".pet", ".移动", ".space", ".tech", ".host", ".site", ".fun", ".store", ".ski", ".pink", ".design", ".ink", ".wiki", ".email", ".video", ".company", ".plus", ".center", ".cool", ".fund", ".gold", ".guru", ".life", ".show", ".team", ".today", ".world", ".zone", ".social", ".bio", ".black", ".green", ".lotto", ".organic", ".poker", ".promo", ".vote", ".archi", ".voto", ".网站", ".商店", ".企业", ".娱乐", ".游戏", ".fit", ".website", ".press", ".icu", ".art", ".asia", ".org.cn", ".biz", ".集团", ".我爱你", ".games", ".sale", ".media", ".studio", ".band", ".fyi", ".cab", ".market", ".news", ".vin", ".tax", ".shopping", ".mba", ".cash", ".cafe", ".technology", ".ren", ".fans", ".co", ".cloud", ".shop", ".law", ".link", ".bj.cn", ".tj.cn", ".sh.cn", ".cq.cn", ".he.cn", ".ha.cn", ".sx.cn", ".nm.cn", ".ln.cn", ".jl.cn", ".hl.cn", ".js.cn", ".zj.cn", ".ah.cn", ".fj.cn", ".jx.cn", ".sd.cn", ".hb.cn", ".hn.cn", ".gd.cn", ".gx.cn", ".hi.cn", ".sc.cn", ".gz.cn", ".yn.cn", ".xz.cn", ".sn.cn", ".gs.cn", ".qh.cn", ".nx.cn", ".xj.cn", ".tw.cn", ".hk.cn", ".mo.cn", ".fan"],
    "BJ_TENCENT_CLOUD_TLD": [".cn", ".com", ".net", ".ac.cn", ".com.cn", ".net.cn", ".org.cn", ".中国", ".bj.cn", ".tj.cn", ".sh.cn", ".cq.cn", ".he.cn", ".ha.cn", ".sx.cn", ".nm.cn", ".ln.cn", ".jl.cn", ".hl.cn", ".js.cn", ".zj.cn", ".ah.cn", ".fj.cn", ".jx.cn", ".sd.cn", ".hb.cn", ".hn.cn", ".gd.cn", ".gx.cn", ".hi.cn", ".sc.cn", ".gz.cn", ".yn.cn", ".xz.cn", ".sn.cn", ".gs.cn", ".qh.cn", ".nx.cn", ".xj.cn", ".tw.cn", ".hk.cn", ".mo.cn"],
    "GZ_TENCENT_CLOUD_TLD": [".cn", ".ac.cn", ".com.cn", ".net.cn", ".org.cn", ".中国", ".cc", ".tv", ".bj.cn", ".tj.cn", ".sh.cn", ".cq.cn", ".he.cn", ".ha.cn", ".sx.cn", ".nm.cn", ".ln.cn", ".jl.cn", ".hl.cn", ".js.cn", ".zj.cn", ".ah.cn", ".fj.cn", ".jx.cn", ".sd.cn", ".hb.cn", ".hn.cn", ".gd.cn", ".gx.cn", ".hi.cn", ".sc.cn", ".gz.cn", ".yn.cn", ".xz.cn", ".sn.cn", ".gs.cn", ".qh.cn", ".nx.cn", ".xj.cn", ".tw.cn", ".hk.cn", ".mo.cn"],
    "WEST_TLD": [".cn", ".ac.cn", ".com.cn", ".net.cn", ".org.cn", ".bj.cn", ".tj.cn", ".sh.cn", ".cq.cn", ".he.cn", ".ha.cn", ".sx.cn", ".nm.cn", ".ln.cn", ".jl.cn", ".hl.cn", ".js.cn", ".zj.cn", ".ah.cn", ".fj.cn", ".jx.cn", ".sd.cn", ".hb.cn", ".hn.cn", ".gd.cn", ".gx.cn", ".hi.cn", ".sc.cn", ".gz.cn", ".yn.cn", ".xz.cn", ".sn.cn", ".gs.cn", ".qh.cn", ".nx.cn", ".xj.cn", ".tw.cn", ".hk.cn", ".mo.cn"],
    "XINNET_TLD": [".com", ".cn", ".ac.cn", ".com.cn", ".net.cn", ".org.cn", ".bj.cn", ".tj.cn", ".sh.cn", ".cq.cn", ".he.cn", ".ha.cn", ".sx.cn", ".nm.cn", ".ln.cn", ".jl.cn", ".hl.cn", ".js.cn", ".zj.cn", ".ah.cn", ".fj.cn", ".jx.cn", ".sd.cn", ".hb.cn", ".hn.cn", ".gd.cn", ".gx.cn", ".hi.cn", ".sc.cn", ".gz.cn", ".yn.cn", ".xz.cn", ".sn.cn", ".gs.cn", ".qh.cn", ".nx.cn", ".xj.cn", ".tw.cn", ".hk.cn", ".mo.cn"]
}

# 转换为列表字典
result = [{"domain": domain} for tlds in qh.values() for domain in tlds]

# 输出结果
print(result)

# 输出到文件
with open('src_tencent_domain.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("域名已成功保存到 domains.json 文件中。")
