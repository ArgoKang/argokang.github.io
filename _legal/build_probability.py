"""Build pages/lugh-probability.html — Archmage Lugh random-item probability disclosure.

Numbers below were checked against the game project (ProjectLugh) on 2026-10-20:
- Gear boxes: Data/Tables/LootTableListData.asset, GearBoxProduct.cs, GameRules (pity 10 / 50)
- Gear pools: ItemDatabase _totalGearDatas — 44 regular + 22 boss gear
- Monster chests: Data/ItemData/45_MonsterChest/*.asset, RewardManager.TryDrawChestShard
- Absorption: EconomyManager.GetDefaultAbsorptionRate / GetAbsorptionRate, GameRules card draw rates
- Random vouchers: Data/ItemData/44_GearRelated/*Random.asset, ItemDatabaseSO.GetGearVoucherCandidates
- Gear stone: ItemDatabaseSO.DrawGearStone (6 implemented types)
Update the numbers here when the game data changes, then run this script.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'pages', 'lugh-probability.html')
SHELL = os.path.join(ROOT, 'pages', 'tos.html')   # header/footer are copied from here

REGULAR_GEAR = 44
BOSS_GEAR = 22

GEAR_BOXES = [  # (box key, [(grade key, percent, pool)])
    ('normal', [('common', 70, REGULAR_GEAR), ('magic', 30, REGULAR_GEAR)]),
    ('special', [('common', 20, REGULAR_GEAR), ('magic', 46, REGULAR_GEAR), ('rare', 30, REGULAR_GEAR), ('elite', 4, REGULAR_GEAR)]),
    ('unique', [('magic', 60, REGULAR_GEAR), ('rare', 34, REGULAR_GEAR), ('elite', 4, REGULAR_GEAR), ('bossElite', 2, BOSS_GEAR)]),
]

MONSTER_CHESTS = [  # (chest key, cubes, [(monster grade, percent, min, max)], open points, bonus requirement, bonus weight, unlock stage)
    ('c0', (5, 10), [('normal', 100, 10, 20)], 1, 10, 1, 0),
    ('c1', (10, 30), [('normal', 90, 20, 30), ('elite', 10, 5, 10)], 2, 20, 0.5, 1),
    ('c2', (30, 50), [('normal', 70, 20, 30), ('elite', 30, 5, 10)], 5, 50, 0.25, 3),
    ('c3', (50, 80), [('elite', 75, 20, 30), ('boss', 25, 5, 10)], 10, 100, 0.1, 5),
    ('c4', (80, 150), [('boss', 90, 20, 30), ('named', 10, 5, 10)], 0, 200, 0.05, 10),
]

ABSORB = [  # monster grade: (Absorption Card, Hyper Card, Prism Card) base success %
    ('normal', (50, 75, 100)),
    ('elite', (30, 50, 100)),
    ('boss', (10, 30, 70)),
    ('named', (0, 10, 30)),
]
CARD_DRAW = (75, 20, 5)  # Absorption / Hyper / Prism when absorbing by card draw

STONE_TYPES = ['oneHand', 'twoHand', 'clothing', 'gloves', 'belt', 'boots']

T = {
'en': {
    'title': 'Archmage Lugh Probability Info',
    'date': 'As of October 20, 2026',
    'intro': 'This page discloses the probabilities of the random items in Archmage Lugh, as required by Korea\'s Game Industry Promotion Act and app store policies. Results are decided at random according to these probabilities. Percentages are rounded to three decimal places. We will announce any change in advance.',
    'grade': 'Grade', 'chance': 'Chance', 'perItem': 'Chance per item',
    'h_gear': '1. Gear Boxes',
    'gear_note': 'The grade is decided first, then one gear item is picked with equal chance: from the %d boss gear items for Boss Elite, otherwise from the %d regular gear items.' % (BOSS_GEAR, REGULAR_GEAR),
    'normal': 'Normal Box', 'special': 'Special Box', 'unique': 'Unique Box',
    'common': 'Common', 'magic': 'Magic', 'rare': 'Rare', 'elite': 'Elite', 'bossElite': 'Boss Elite',
    'pity_h': 'Unique Box guarantees',
    'pity': ['If 10 openings in a row give neither Elite nor Boss Elite, the 10th gives Elite. The count resets when you get Elite or Boss Elite.',
             'If 50 openings in a row give no Boss Elite, the 50th gives Boss Elite. Both counts reset when you get Boss Elite.',
             'If both apply to the same opening, Boss Elite takes priority. The remaining counts are shown on the box screen.',
             'Boss Elite gear is boss gear of Elite grade.'],
    'h_chest': '2. Monster Chests',
    'chest': 'Chest', 'cubes': 'Cubes', 'shards': 'Monster shards (grade chance · amount)',
    'c0': 'Monster Chest', 'c1': 'Veteran Chest', 'c2': 'Champion Chest', 'c3': 'Alpha Chest', 'c4': 'Overlord Chest',
    'mg_normal': 'Normal', 'mg_elite': 'Elite', 'mg_boss': 'Boss', 'mg_named': 'Named',
    'chest_notes': ['Each chest gives cubes and one kind of monster shard. Amounts are picked with equal chance within the range shown.',
                    'The shard is one monster, picked with equal chance, from the monsters of that grade you have discovered or unlocked.',
                    'If you have no monster of a grade yet, that grade\'s chance is shared among the remaining grades in proportion. Example: before you meet any boss, an Alpha Chest gives Elite shards 100%.',
                    'If none of the chest\'s grades is available, the grade drops one step at a time until one is, and the amount doubles with each step.'],
    'bonus_h': 'Bonus chests',
    'bonus_intro': 'Opening chests earns points. When you reach the requirement of the current bonus chest, you receive it. The next bonus chest is picked by weight from the chests whose unlock stage you have cleared.',
    'points': 'Points per opening', 'req': 'Bonus requirement', 'weight': 'Weight', 'unlock': 'Unlock stage', 'allChance': 'Chance with all unlocked',
    'h_absorb': '3. Absorption',
    'absorb_intro': 'After you defeat a dungeon boss, you get 3 tries to absorb it. The success rate depends on the card and the monster\'s grade.',
    'monsterGrade': 'Monster grade', 'cardA': 'Absorption Card', 'cardH': 'Hyper Card', 'cardP': 'Prism Card',
    'absorb_notes': ['The 2nd try has 1.5× the base rate and the 3rd try 2× the base rate (up to 100%).',
                     'If the first two tries both used a Prism Card and failed, the 3rd try succeeds 100%.',
                     'A failed try returns some shards. This amount is fixed, not random.'],
    'draw_h': 'Absorbing by card draw',
    'draw_intro': 'When you absorb by card draw, the card is picked as follows:',
    'card': 'Card',
    'h_voucher': '4. Random Gear Vouchers',
    'voucher': 'Voucher', 'pool': 'Pool',
    'vE': 'Random Elite Gear', 'vB': 'Random Boss Elite Gear',
    'poolE': '%d regular gear items (Elite grade)' % REGULAR_GEAR, 'poolB': '%d boss gear items (Elite grade)' % BOSS_GEAR,
    'h_stone': '5. Gear Enhancement Stone',
    'stone_intro': 'When received, it turns into one of the following part stones with equal chance:',
    'part': 'Part stone',
    'oneHand': 'One-hand weapon', 'twoHand': 'Two-hand weapon', 'clothing': 'Clothing', 'gloves': 'Gloves', 'belt': 'Belt', 'boots': 'Boots',
    'h_hist': 'Change history',
    'hist': ['October 20, 2026: first published'],
},
'ko': {
    'title': '대마법사 루 확률 정보',
    'date': '2026년 10월 20일 기준',
    'intro': '「게임산업진흥에 관한 법률」과 앱마켓 정책에 따라 「대마법사 루」의 확률형 아이템 정보를 공개합니다. 결과는 아래 확률에 따라 무작위로 정해지며, 확률은 소수점 넷째 자리에서 반올림했습니다. 확률이 바뀌면 미리 알립니다.',
    'grade': '등급', 'chance': '확률', 'perItem': '장비 1종당 확률',
    'h_gear': '1. 장비 상자',
    'gear_note': '등급이 먼저 정해진 뒤, 그 안에서 장비 1개가 같은 확률로 정해집니다. 보스 엘리트는 보스 장비 %d종, 그 외 등급은 일반 장비 %d종 중에서 나옵니다.' % (BOSS_GEAR, REGULAR_GEAR),
    'normal': '일반 상자', 'special': '특별 상자', 'unique': '유니크 상자',
    'common': '일반', 'magic': '매직', 'rare': '희귀', 'elite': '엘리트', 'bossElite': '보스 엘리트',
    'pity_h': '유니크 상자 획득 보장(천장)',
    'pity': ['엘리트와 보스 엘리트가 나오지 않고 연속으로 10회째 열면, 10회째에 엘리트가 확정됩니다. 엘리트나 보스 엘리트를 얻으면 횟수가 초기화됩니다.',
             '보스 엘리트가 나오지 않고 연속으로 50회째 열면, 50회째에 보스 엘리트가 확정됩니다. 보스 엘리트를 얻으면 두 횟수가 모두 초기화됩니다.',
             '두 조건이 같은 회차에 겹치면 보스 엘리트가 우선합니다. 남은 횟수는 상자 화면에 표시됩니다.',
             '보스 엘리트 장비는 엘리트 등급의 보스 장비입니다.'],
    'h_chest': '2. 몬스터 상자',
    'chest': '상자', 'cubes': '큐브', 'shards': '몬스터 조각 (등급 확률 · 수량)',
    'c0': '몬스터 상자', 'c1': '정예 상자', 'c2': '챔피언 상자', 'c3': '우두머리 상자', 'c4': '지배자 상자',
    'mg_normal': '일반', 'mg_elite': '엘리트', 'mg_boss': '보스', 'mg_named': '네임드',
    'chest_notes': ['상자마다 큐브와 몬스터 조각 1종이 나옵니다. 수량은 표시된 범위 안에서 같은 확률로 정해집니다.',
                    '조각은 해당 등급에서 이용자가 발견하거나 해금한 몬스터 중 1종이 같은 확률로 정해집니다.',
                    '아직 해당 등급의 몬스터가 없으면, 그 등급의 확률은 남은 등급에 비율대로 나뉩니다. 예: 보스를 아직 만나지 못했다면 우두머리 상자는 엘리트 조각 100%입니다.',
                    '상자의 모든 등급에 대상 몬스터가 없으면, 대상이 있는 등급까지 한 단계씩 내려가며 단계마다 수량이 2배가 됩니다.'],
    'bonus_h': '보너스 상자',
    'bonus_intro': '상자를 열 때마다 포인트가 쌓이고, 현재 걸린 보너스 상자의 요구치를 채우면 그 상자를 받습니다. 다음 보너스 상자는 해금 스테이지를 클리어한 상자 중에서 가중치에 따라 정해집니다.',
    'points': '열 때 포인트', 'req': '보너스 요구치', 'weight': '가중치', 'unlock': '해금 스테이지', 'allChance': '모두 해금 시 확률',
    'h_absorb': '3. 흡수',
    'absorb_intro': '던전 보스를 쓰러뜨리면 흡수 기회가 3번 주어집니다. 성공률은 사용한 카드와 몬스터 등급에 따라 다릅니다.',
    'monsterGrade': '몬스터 등급', 'cardA': '흡수 카드', 'cardH': '하이퍼 카드', 'cardP': '프리즘 카드',
    'absorb_notes': ['두 번째 시도는 기본 확률의 1.5배, 세 번째 시도는 2배가 적용됩니다(최대 100%).',
                     '앞의 두 번을 모두 프리즘 카드로 시도해 실패했다면 세 번째 시도는 100% 성공합니다.',
                     '실패하면 조각 일부를 돌려받습니다. 이 수량은 정해져 있으며 무작위가 아닙니다.'],
    'draw_h': '카드 뽑기로 흡수',
    'draw_intro': '카드 뽑기로 흡수할 때 카드는 다음 확률로 정해집니다.',
    'card': '카드',
    'h_voucher': '4. 장비 랜덤권',
    'voucher': '랜덤권', 'pool': '대상',
    'vE': '엘리트 장비 랜덤권', 'vB': '보스 엘리트 장비 랜덤권',
    'poolE': '일반 장비 %d종 (엘리트 등급)' % REGULAR_GEAR, 'poolB': '보스 장비 %d종 (엘리트 등급)' % BOSS_GEAR,
    'h_stone': '5. 장비 강화 스톤',
    'stone_intro': '받는 순간 아래 부위 스톤 중 하나로 같은 확률로 바뀝니다.',
    'part': '부위 스톤',
    'oneHand': '한손 무기', 'twoHand': '양손 무기', 'clothing': '상의', 'gloves': '장갑', 'belt': '벨트', 'boots': '신발',
    'h_hist': '변경 이력',
    'hist': ['2026년 10월 20일: 최초 게시'],
},
'pt-BR': {
    'title': 'Probabilidades de Archmage Lugh',
    'date': 'Atualizado em 20 de outubro de 2026',
    'intro': 'Esta página divulga as probabilidades dos itens aleatórios de Archmage Lugh, conforme a Lei de Promoção da Indústria de Jogos da Coreia e as políticas das lojas de apps. Os resultados são definidos aleatoriamente segundo estas probabilidades. As porcentagens são arredondadas para três casas decimais. Avisaremos com antecedência sobre qualquer alteração.',
    'grade': 'Grau', 'chance': 'Chance', 'perItem': 'Chance por item',
    'h_gear': '1. Caixas de equipamento',
    'gear_note': 'Primeiro o grau é definido; depois, um equipamento é escolhido com chance igual: entre os %d equipamentos de chefe para Chefe Elite, ou entre os %d equipamentos comuns nos demais graus.' % (BOSS_GEAR, REGULAR_GEAR),
    'normal': 'Caixa Normal', 'special': 'Caixa Especial', 'unique': 'Box Exclusiva',
    'common': 'Comum', 'magic': 'Mágico', 'rare': 'Raro', 'elite': 'Elite', 'bossElite': 'Chefe Elite',
    'pity_h': 'Garantias da Box Exclusiva',
    'pity': ['Se 10 aberturas seguidas não derem Elite nem Chefe Elite, a 10ª dá Elite. A contagem reinicia ao obter Elite ou Chefe Elite.',
             'Se 50 aberturas seguidas não derem Chefe Elite, a 50ª dá Chefe Elite. As duas contagens reiniciam ao obter Chefe Elite.',
             'Se as duas valerem na mesma abertura, Chefe Elite tem prioridade. As contagens restantes aparecem na tela da caixa.',
             'Equipamento Chefe Elite é equipamento de chefe de grau Elite.'],
    'h_chest': '2. Baús de monstro',
    'chest': 'Baú', 'cubes': 'Cubos', 'shards': 'Fragmentos de monstro (chance do grau · quantidade)',
    'c0': 'Baú de Monstro', 'c1': 'Baú de Veterano', 'c2': 'Baú de Campeão', 'c3': 'Baú do Alfa', 'c4': 'Baú de Soberano',
    'mg_normal': 'Comum', 'mg_elite': 'Elite', 'mg_boss': 'Chefe', 'mg_named': 'Nomeado',
    'chest_notes': ['Cada baú dá cubos e um tipo de fragmento de monstro. As quantidades são escolhidas com chance igual dentro do intervalo indicado.',
                    'O fragmento é de um monstro, escolhido com chance igual, entre os monstros daquele grau que você já descobriu ou desbloqueou.',
                    'Se você ainda não tem monstros de um grau, a chance desse grau é dividida proporcionalmente entre os graus restantes. Ex.: antes de encontrar um chefe, o Baú do Alfa dá fragmentos Elite 100%.',
                    'Se nenhum grau do baú estiver disponível, o grau desce um nível por vez até haver um disponível, e a quantidade dobra a cada nível.'],
    'bonus_h': 'Baús bônus',
    'bonus_intro': 'Abrir baús rende pontos. Ao atingir o requisito do baú bônus atual, você o recebe. O próximo baú bônus é escolhido por peso entre os baús cuja fase de desbloqueio você já concluiu.',
    'points': 'Pontos por abertura', 'req': 'Requisito do bônus', 'weight': 'Peso', 'unlock': 'Fase de desbloqueio', 'allChance': 'Chance com todos desbloqueados',
    'h_absorb': '3. Absorção',
    'absorb_intro': 'Ao derrotar o chefe da masmorra, você tem 3 tentativas de absorvê-lo. A taxa de sucesso depende da carta e do grau do monstro.',
    'monsterGrade': 'Grau do monstro', 'cardA': 'Carta de Absorção', 'cardH': 'Carta Hyper', 'cardP': 'Carta Prisma',
    'absorb_notes': ['A 2ª tentativa tem 1,5× a taxa base e a 3ª tentativa 2× a taxa base (até 100%).',
                     'Se as duas primeiras tentativas usaram Carta Prisma e falharam, a 3ª tentativa tem 100% de sucesso.',
                     'Uma tentativa falha devolve alguns fragmentos. Essa quantidade é fixa, não aleatória.'],
    'draw_h': 'Absorção por sorteio de carta',
    'draw_intro': 'Ao absorver por sorteio de carta, a carta é escolhida assim:',
    'card': 'Carta',
    'h_voucher': '4. Vales de equipamento aleatório',
    'voucher': 'Vale', 'pool': 'Itens possíveis',
    'vE': 'Equip. Elite aleatório', 'vB': 'Equip. Chefe Elite aleatório',
    'poolE': '%d equipamentos comuns (grau Elite)' % REGULAR_GEAR, 'poolB': '%d equipamentos de chefe (grau Elite)' % BOSS_GEAR,
    'h_stone': '5. Pedra de Aprimoramento',
    'stone_intro': 'Ao ser recebida, vira uma das pedras abaixo com chance igual:',
    'part': 'Pedra',
    'oneHand': 'Arma de uma mão', 'twoHand': 'Arma de duas mãos', 'clothing': 'Roupa', 'gloves': 'Luvas', 'belt': 'Cinto', 'boots': 'Botas',
    'h_hist': 'Histórico de alterações',
    'hist': ['20 de outubro de 2026: primeira publicação'],
},
}


def pct(x, lang):
    s = ('%.3f' % x).rstrip('0').rstrip('.')
    return (s.replace('.', ',') if lang == 'pt-BR' else s) + '%'


def table(head, rows, ind):
    h = ''.join('<th>%s</th>' % c for c in head)
    b = ''.join('\n%s\t\t<tr>%s</tr>' % (ind, ''.join('<td>%s</td>' % c for c in r)) for r in rows)
    return ('%s<div class="table-wrap"><table>\n%s\t<thead><tr>%s</tr></thead>\n%s\t<tbody>%s\n%s\t</tbody>\n%s</table></div>'
            % (ind, ind, h, ind, b, ind, ind))


def ul(items, ind):
    return '%s<ul>\n%s\n%s</ul>' % (ind, '\n'.join('%s\t<li>%s</li>' % (ind, i) for i in items), ind)


def block(lang):
    t = T[lang]
    i = '\t\t\t\t\t'
    out = ['%s<h1>%s</h1>' % (i, t['title']), '%s<p><strong>%s</strong></p>' % (i, t['date']), '%s<p>%s</p>' % (i, t['intro'])]

    out.append('%s<h2>%s</h2>' % (i, t['h_gear']))
    out.append('%s<p>%s</p>' % (i, t['gear_note']))
    for box, grades in GEAR_BOXES:
        out.append('%s<h3>%s</h3>' % (i, t[box]))
        out.append(table([t['grade'], t['chance'], t['perItem']],
                         [[t[g], pct(p, lang), pct(p / pool, lang)] for g, p, pool in grades], i))
        if box == 'unique':
            out.append('%s<div class="box">\n%s\t<p><strong>%s</strong></p>\n%s\n%s</div>' % (i, i, t['pity_h'], ul(t['pity'], i + '\t'), i))

    out.append('%s<h2>%s</h2>' % (i, t['h_chest']))
    rows = []
    for key, cubes, shards, *_ in MONSTER_CHESTS:
        s = '<br />'.join('%s %s · %d~%d' % (t['mg_' + g], pct(p, lang), lo, hi) for g, p, lo, hi in shards)
        rows.append([t[key], '%d~%d' % cubes, s])
    out.append(table([t['chest'], t['cubes'], t['shards']], rows, i))
    out.append(ul(t['chest_notes'], i))
    out.append('%s<h3>%s</h3>' % (i, t['bonus_h']))
    out.append('%s<p>%s</p>' % (i, t['bonus_intro']))
    total = sum(c[5] for c in MONSTER_CHESTS)
    out.append(table([t['chest'], t['points'], t['req'], t['unlock'], t['weight'], t['allChance']],
                     [[t[k], str(pts), str(req), str(st), ('%g' % w).replace('.', ',') if lang == 'pt-BR' else '%g' % w, pct(w / total * 100, lang)]
                      for k, _, _, pts, req, w, st in MONSTER_CHESTS], i))

    out.append('%s<h2>%s</h2>' % (i, t['h_absorb']))
    out.append('%s<p>%s</p>' % (i, t['absorb_intro']))
    out.append(table([t['monsterGrade'], t['cardA'], t['cardH'], t['cardP']],
                     [[t['mg_' + g]] + [pct(r, lang) for r in rates] for g, rates in ABSORB], i))
    out.append(ul(t['absorb_notes'], i))
    out.append('%s<h3>%s</h3>' % (i, t['draw_h']))
    out.append('%s<p>%s</p>' % (i, t['draw_intro']))
    out.append(table([t['card'], t['chance']], [[t[c], pct(p, lang)] for c, p in zip(('cardA', 'cardH', 'cardP'), CARD_DRAW)], i))

    out.append('%s<h2>%s</h2>' % (i, t['h_voucher']))
    out.append(table([t['voucher'], t['pool'], t['perItem']],
                     [[t['vE'], t['poolE'], pct(100 / REGULAR_GEAR, lang)], [t['vB'], t['poolB'], pct(100 / BOSS_GEAR, lang)]], i))

    out.append('%s<h2>%s</h2>' % (i, t['h_stone']))
    out.append('%s<p>%s</p>' % (i, t['stone_intro']))
    out.append(table([t['part'], t['chance']], [[t[k], pct(100 / len(STONE_TYPES), lang)] for k in STONE_TYPES], i))

    out.append('%s<h2>%s</h2>' % (i, t['h_hist']))
    out.append(ul(t['hist'], i))
    return '\n'.join(out)


NAMES = {'en': 'English', 'ko': '한국어', 'pt-BR': 'Português (Brasil)'}
shell = open(SHELL, encoding='utf-8').read()
a = shell.index('<div class="wrap">', shell.index('<main class="legal">')) + len('<div class="wrap">')
b = shell.index('</div>\n\t\t</main>')
blocks = ['\t\t\t\t<!-- %s -->\n\t\t\t\t<div data-lang-block lang="%s"%s>\n%s\n\t\t\t\t</div>'
          % (NAMES[l], l, '' if l == 'en' else ' hidden', block(l)) for l in ['en', 'ko', 'pt-BR']]
page = shell[:a] + '\n\n' + '\n\n'.join(blocks) + '\n\n\t\t\t' + shell[b:]
page = page.replace('data-i18n="meta.title.tos">Terms of Service - V-High', 'data-i18n="meta.title.probability">Archmage Lugh Probability Info - V-High')
page = page.replace('<a href="tos.html" class="active" data-i18n="nav.tos">', '<a href="tos.html" data-i18n="nav.tos">')
open(PAGE, 'w', encoding='utf-8').write(page)
print('built', PAGE)
