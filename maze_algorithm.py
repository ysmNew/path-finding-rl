# 좌선(수) 알고리즘 (π*로 예측됨)

class LeftHandedRule:

    def __init__(self, cur_x, cur_y): #현재 위치만 받아온다.
        self.cur_x = cur_x
        self.cur_y = cur_y

    def obsjudge(self, cur_x, cur_y): #현재 위치에서 상하좌우에 장애물이 있는지 확인 (환경정보를 아는게 필요? or 시행착오로 학습?)
        global obslist
        obslist = []
        if done:
            obslist
        # 스텝이 끝나면 호출되어, 장애물과 부딪쳐 에피소드가 종료된 경우 해당 좌표를 obslist에 추가

    def actionpolicy:
        # 방식 1, 모든 경우에 수에 따라 움직일 방향 직접 지정 (상,하,좌,우, 이동가능 or 장애물)
        # 방식 2, 이동한 방향 기준으로 지난 Action에 따라 움직일 방향 지정 (orientd -> 이전액션에 의해 결정됨)
        '''
        (좌측에 장애물이 없으면 -> 좌회전)
        (좌측에 장애물이 있으면 -> 직진)
        (좌측과 앞쪽에 장애물이 있으면 -> 우회전)
        (좌측과 앞쪽과 우측에 장애물이 있으면 -> 뒤로)
        (끝나지 않고 loop를 도는 경우? -> 어쩌지?)
        '''
