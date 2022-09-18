import pandas as pd
import random

#lendo os dados da planilha do Excel data.csv
df = pd.read_csv(r'C:\Users\User\Documents\python\simulador_copa\data.csv')
df.head()

class Team:
    BEST_SCORE = 1837.6 #score do Brasil segundo o ranking da FIFA (maior de todos)
    #Definindo um construtor com os atributos adequados (tendo em vista as células do data.csv)
    def __init__(self, cellData):
        teamData = cellData.split('|')
        self.name = teamData[0]
        self.score = float(teamData[1])
        
    #função motivate vai ser criada dando uma porcentagem para cada seleção com base no Brasil (seleção mais forte no ranking da FIFA)
    def motivate(self):
        self.lastMotivation = random.uniform(70, (self.score * 100) / Team.BEST_SCORE)
        return self.lastMotivation
    
#mapa com chave sendo o grupo e o valor as seleções
bestTeamsByGroup = {}
for label, content in df.items():
    team1 = Team(content[0])
    team2 = Team(content[1])
    team3 = Team(content[2])
    team4 = Team(content[3])
    bestTeamsByGroup[label] = sorted([ team1, team2, team3, team4 ], key=Team.motivate, reverse=True)

#imprimindo os grupos ordenados pelas duas melhores seleções de cada grupo
for grupo, motivatedTeams in bestTeamsByGroup.items():
    print(f'Grupo {grupo}: ', end='')
    for team in motivatedTeams:
        print(f'{team.name} ({team.lastMotivation:.2f})', end='')
    print()

#variáveis criadas para os dois melhores de cada grupo
team1A = bestTeamsByGroup['A'][0]
team2A = bestTeamsByGroup['A'][1]
team1B = bestTeamsByGroup['B'][0]
team2B = bestTeamsByGroup['B'][1]
team1C = bestTeamsByGroup['C'][0]
team2C = bestTeamsByGroup['C'][1]
team1D = bestTeamsByGroup['D'][0]
team2D = bestTeamsByGroup['D'][1]
team1E = bestTeamsByGroup['E'][0]
team2E = bestTeamsByGroup['E'][1]
team1F = bestTeamsByGroup['F'][0]
team2F = bestTeamsByGroup['F'][1]
team1G = bestTeamsByGroup['G'][0]
team2G = bestTeamsByGroup['G'][1]
team1H = bestTeamsByGroup['H'][0]
team2H = bestTeamsByGroup['H'][1]

#variáveis das oitavas para definir as quartas de finais
quarter1 = team1A if team1A.motivate() > team2B.motivate() else team2B
quarter2 = team1C if team1C.motivate() > team2D.motivate() else team2D
quarter3 = team1E if team1E.motivate() > team2F.motivate() else team2F
quarter4 = team1G if team1G.motivate() > team2H.motivate() else team2H
quarter5 = team1B if team1B.motivate() > team2A.motivate() else team2A
quarter6 = team1D if team1D.motivate() > team2C.motivate() else team2C
quarter7 = team1F if team1F.motivate() > team2E.motivate() else team2E
quarter8 = team1H if team1H.motivate() > team2G.motivate() else team2G

print("OITAVAS DE FINAIS:")

print(f'{team1A.name} ({team.lastMotivation:.2f}) X {team2B.name} ({team.lastMotivation:.2f})')
print(f'{team1C.name} ({team.lastMotivation:.2f}) X {team2D.name} ({team.lastMotivation:.2f})')
print(f'{team1E.name} ({team.lastMotivation:.2f}) X {team2F.name} ({team.lastMotivation:.2f})')
print(f'{team1G.name} ({team.lastMotivation:.2f}) X {team2H.name} ({team.lastMotivation:.2f})')
print(f'{team1B.name} ({team.lastMotivation:.2f}) X {team2A.name} ({team.lastMotivation:.2f})')
print(f'{team1D.name} ({team.lastMotivation:.2f}) X {team2C.name} ({team.lastMotivation:.2f})')
print(f'{team1F.name} ({team.lastMotivation:.2f}) X {team2E.name} ({team.lastMotivation:.2f})')
print(f'{team1H.name} ({team.lastMotivation:.2f}) X {team2G.name} ({team.lastMotivation:.2f})')

print("QUARTAS DE FINAIS:")

semi1 = quarter1 if quarter1.motivate() > quarter2.motivate() else quarter2
semi2 = quarter3 if quarter3.motivate() > quarter4.motivate() else quarter4
semi3 = quarter5 if quarter5.motivate() > quarter6.motivate() else quarter6
semi4 = quarter7 if quarter7.motivate() > quarter8.motivate() else quarter8

print(f'{quarter1.name} ({quarter1.lastMotivation:.2f}) X {quarter2.name} ({quarter2.lastMotivation:.2f})')
print(f'{quarter3.name} ({quarter3.lastMotivation:.2f}) X {quarter4.name} ({quarter4.lastMotivation:.2f})')
print(f'{quarter5.name} ({quarter5.lastMotivation:.2f}) X {quarter6.name} ({quarter6.lastMotivation:.2f})')
print(f'{quarter7.name} ({quarter7.lastMotivation:.2f}) X {quarter8.name} ({quarter8.lastMotivation:.2f})')

print("SEMIFINAIS:")

final1 = None
terceiro1 = None
if semi1.motivate() > semi2.motivate():
    final1 = semi1
else:
    final1 = semi2
    
final2 = None
terceiro2 = None
if semi3.motivate() > semi4.motivate():
    final2 = semi3
    terceiro2 = semi4
else:
    final2 = semi4
    terceiro2 = semi3
    
print(f'{semi1.name} ({semi1.lastMotivation:.2f}) X {semi2.name} ({semi2.lastMotivation:.2f})')
print(f'{semi3.name} ({semi3.lastMotivation:.2f}) X {semi4.name} ({semi4.lastMotivation:.2f})')

print("FINAL")

winner = final1 if final1.motivate() > final2.motivate() else final2
second = final1 if final1.lastMotivation < final2.lastMotivation else final2

print(f'Campeao: {winner.name} ({winner.lastMotivation:.2f})')
print(f'Vice: {second.name} ({second.lastMotivation:.2f})')
