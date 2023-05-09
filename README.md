# UNO Game With Python

## ![스크린샷(77)](https://user-images.githubusercontent.com/42289726/236804666-2108baed-ea26-4b97-a6c1-438a7ec7b17c.png)

---

## 설명

- Pygame UNO는 Python과 Pygame 라이브러리를 사용하여 구현된 UNO 게임입니다.

## 설치 방법

1. 이 레포지토리를 클론하거나 다운로드합니다.
2. 프로젝트 폴더로 이동한 다음, 필요한 라이브러리를 설치합니다.
   - pip install -r requirements.txt
3. 게임을 실행합니다.
   - python main.py

## 게임 방법

- 기본 규칙은 다음과 같습니다:

1. 카드 분류: UNO 카드 덱은 총 108장으로 구성되어 있으며, 이 중 76장은 숫자 카드(0-9), 24장은 액션 카드(스킵, 리버스, 드로우 투), 그리고 8장은 와일드 카드(와일드, 와일드 드로우 포)로 구성되어 있습니다. 각 카드는 빨강, 녹색, 파랑, 노랑의 4가지 색상 중 하나를 가지고 있습니다.

2. 카드 분배: 각 플레이어에게 7장의 카드가 나누어지고, 남은 카드는 덱으로 놓여집니다. 덱의 맨 위 카드를 공개하여 디스카드 더미를 시작합니다.

3. 게임 진행: 플레이어는 시계 방향으로 차례를 진행합니다. 플레이어는 자신의 차례에 디스카드 더미 맨 위의 카드와 일치하는 숫자나 색상의 카드를 낼 수 있습니다. 액션 카드나 와일드 카드를 사용하여 상황을 바꿀 수도 있습니다.

4. 액션 카드:

- 스킵(Skip): 다음 플레이어의 차례를 건너뛰게 합니다.
- 리버스(Reverse): 게임의 방향을 바꾸어, 반대 방향의 플레이어가 차례를 진행하게 합니다.
- 드로우 투(Draw Two): 다음 플레이어는 2장의 카드를 뽑고 차례를 넘깁니다.

5. 와일드 카드:

- 와일드(Wild): 플레이어는 이 카드를 낸 후 원하는 색상을 선택할 수 있습니다. 다음 플레이어는 선택한 색상의 카드를 내야 합니다.
- 와일드 드로우 포(Wild Draw Four): 플레이어는 원하는 색상을 선택한 후, 다음 플레이어는 4장의 카드를 뽑고 차례를 넘깁니다.
- 리로드(reload): 플레이어는 이 카드를 낸 후, 자신의 카드를 덱에 전부 넣고 원래의 손패 수만큼 덱에서 가져와 손패를 채웁니다.

6. UNO 외치기 (계속): 플레이어가 마지막 카드를 낼 차례가 되면, 그 플레이어는 "UNO"를 외쳐야 합니다. 만약 다른 플레이어가 "UNO"를 외치지 않은 플레이어를 지목하면, "UNO"를 외치지 않은 플레이어는 덱에서 두 장의 카드를 뽑아야 합니다.

7. 승리: 먼저 손에 있는 모든 카드를 소진한 플레이어가 승리합니다. 게임이 끝날 때 다른 플레이어들의 손에 남아 있는 카드의 점수가 승리한 플레이어에게 부여됩니다. 숫자 카드는 해당 숫자만큼의 점수가, 액션 카드는 20점, 와일드 카드는 50점으로 계산됩니다. 일반적으로 미리 정한 점수에 도달한 플레이어가 최종 승자가 됩니다.

8. 무승부: 덱에서 남은 카드가 없고 플레이어들이 카드를 내지 못할 경우, 무승부로 게임이 종료됩니다. 이 경우 모든 플레이어의 손에 남아 있는 카드의 점수를 합산하고, 점수가 가장 낮은 플레이어가 승리합니다.

## 조작 방법및 예시

## 시작 메뉴 창

## ![StartMenuScreen](https://user-images.githubusercontent.com/42289726/232302391-fa6d41cc-36e8-4ea2-b11d-0dfae2ec1a31.png)

## 3 종류의 size

---

### 세팅 메뉴 사용 예시

- small size
  <img src=https://user-images.githubusercontent.com/42289726/232302423-58b1ca85-0c84-400f-9f1e-beaf1add180c.png width="480" height="270"/>

- medium size
  <img src=https://user-images.githubusercontent.com/42289726/232302427-021ac335-187b-43e5-a417-4a5d2681fb34.png width="640" height="360"/>

- large size
  <img src=https://user-images.githubusercontent.com/42289726/232302429-f0a01e5b-ce5b-4963-9eaf-04d732226d34.png width="800" height="450"/>

---

## 키보드 세팅 메뉴

---

- Key Setting Menu Screen
  ![KeySetting](https://user-images.githubusercontent.com/42289726/232302434-2f1acec4-c207-493d-b3a7-f1d119869c3c.png)

- Key setting Example
  ![Pygame Uno 2023-04-16 19-10-31](https://user-images.githubusercontent.com/42289726/232302150-a034bfde-9a7a-48ac-afa0-6bb3a3c55b96.gif)
