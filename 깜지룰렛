import random

OS = [
    "AttackControl",
    "AttackServerHandler"
    "CombatHitboxSystem",
    "DataSaveManager",
    "GamepassPurchase",
    "HealthBarController",
    "IDLEAnimation",
    "IntermissionSystem",
    "JumpDisable",
    "KillCounter",
    "KillPart",
    "KillerRoundManager",
    "LeaderboardBase",
    "LevelBadgeAward",
    "MainAttackLocal",
    "NPCDialogue",
    "NPCDialogue2",
    "OverheadTagInstaller (WithHealthBarController)",
    "PlaceTeleporter",
    "RoundManager(WithIntermissionSystem)",
    "ServiceList",
    "SpectateSystem",
    "Sprint Control",
    "SprintFunction",
    "TouchDamageScript",
    "TypeWriteDialogue"
]

scripts = OS.copy()
random.shuffle(scripts)

print(f"깜지 룰렛 뽑기")

while True :
    
    if not scripts :
        print("\n끝 리셋 하시겠습니까? O / X")
        UC = input().upper() 
        if UC == "O" :
            scripts = OS.copy()
            random.shuffle(scripts)
            print(f"리셋 완료")
            continue
        elif UC == "X":
            print(f"룰렛 종료")
            break

        else :
            print(f"O 또는 X 중에 다시 골라주세요")
            

   
    UI = input("\n'뽑기'를 입력해 오늘의 깜지 숙제 뽑기: ")

    if UI == f"뽑기" :
        P = scripts.pop(0)
        print(f"당첨된 스크립트 : [{P}]")
        print(f"(남은 개수: {len(scripts)})")
    else :
        print(f"제대로 다시 입력 하세요")
