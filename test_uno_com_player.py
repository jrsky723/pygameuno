import pytest
from game.uno_com_player import UnoComPlayer

def test_is_human():
    com_player = UnoComPlayer("Computer 1")
    assert com_player.is_human() == False

# UnoComPlayer 클래스가 is_human 메소드를 올바르게 
# 오버라이드하는지 확인하는 간단한 테스트 케이스를 포함하고 있습니다.