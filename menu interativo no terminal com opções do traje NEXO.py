import time

while True:
    print('[1] composiçáo do traje\n'
    '[2] protocolos de inicializacão\n'
    '[3] status de energia\n'
    '[5] reiniciar necleo\n'
    '[0] encerrar conexao')
    
    comando = input('comando:')
    while not comando.isdigit():
        comando = input('comando invalido digite de novo:')
    comando = int(comando)

    if comando in range(0, 6):
        if comando == 0:
            print('~' * 26 + '\n' +
            'conexão com NEXO encerrada\n' +
            '~' * 26)
            break

        elif comando == 1:
             time.sleep(0.7)
             print('\nnucleo NEXO > composição do traje\n'
            '\n'
            'Camadas Ativadas:' + '\n'
             '├─ [✓] Fibras de Carbono Vivas' + '\n' +
             '├─ [✓] Liga Óssea Reforçada' + '\n' +
             '├─ [✓] Núcleo Arcano de Condutividade' + '\n' +
             '└─ [✓] Malha de Isolamento Sensorial' + '\n' +
             '\n' 
             'Notas do Portador:' + '\n'
             '“Cada material escolhido não apenas sustenta,' + '\n'
             'mas ecoa a intenção de quem veste.”' + '\n')
             
             input('[ENTER] pra continuar')

       
        elif comando == 2:
             print('~' * 30 + '\n' + 
             'INICIALIZAÇÃO DO NÚCLEO NEXO' + '\n' + '\n' +
             'Iniciando os Protocolos de Inicialização...' + '\n')
             time.sleep(3)

             print('1. Checando Integridade dos Componentes...' + '\n'
             '- [✓] Fibras de Carbono Vivas' + '\n'
             '- [✓] Núcleo de Energia Arcana' + '\n'
             '- [✓] Circuitos de Isolamento Sensorial\n')
             time.sleep(1.5)

             print('\n2. Estabilizando Conexões de Rede Neural...')
             time.sleep(0.5)

             print('- [✓] Conexão com Sistema Central de Controle')
             time.sleep(0.5)

             print('- [✓] Conexão com Suporte de Interface Mental\n')
             time.sleep(1)

             print('\n3. Ativando Capacidades de Defesa...')
             time.sleep(0.5)

             print('- [✓] Escudo de Distorção Energética')
             time.sleep(0.5)

             print('- [✓] Repelente de Interferência Externa\n')
             time.sleep(1)

             print('\n4. Reconhecendo Presença do Portador...')
             time.sleep(0.5)

             print('- [✓] Verificação de Identidade')
             time.sleep(0.5)

             print('- [✓] Análise do Padrão Biométrico\n')
             time.sleep(1)

             print('\n5. Sincronizando com Memórias Anteriores...')
             time.sleep(0.5)

             print('- [✓] Recuperando Registro de Portadores Anteriores')
             time.sleep(0.5)

             print('- [✓] Restaurando Conhecimento Armazenado\n')
             time.sleep(0.3)

             input('\n[ENTER] pra continar')
             print('> Todos os sistemas estão estáveis. O traje NEXO está pronto para ativação.\n')
        elif comando == 3:

             print('> Núcleo NEXO > Status de Energia')
             time.sleep(1)

             print(
            '┌────────────────────────────────────────────┐\n'
            '│        Núcleo Energético: ONLINE           │\n'
            '│                                            │\n'
            '│        Energia Atual: 73% [▓▓▓▓▓▓▓░░░░]    │\n'
            '│        Estabilidade: Moderada              │\n'
            '│        Última Carga Completa: 7h atrás     │\n'
            '│                                            │\n'
            '│        Fonte Primária: Núcleo Ígneo        │\n'
            '│        Fonte Secundária: Cinética Orgânica │\n'
            '└────────────────────────────────────────────┘\n')
             time.sleep(0.4)

             print('Análise:\n'  
             '"O traje está funcional, mas a força que o move\n' 
             'ainda depende do portador."\n')

             input('[ENTER] pra continuar')
        
        elif comando == 4:
            print('> Núcleo NEXO > Memórias Anteriores\n')
            time.sleep(0.3)

            print('\nAcesso autorizado.')
            time.sleep(0.2)

            print('Decifrando registros...')
            time.sleep(2)

            print(
            '┌──────────── Registro #003 ────────────┐\n'
            '│ Data: Desconhecida                    │\n'
            '│ Portador: "[Redação corrompida]"      │\n'
            '│                                       │\n'
            '│ "Quando o núcleo vacilou, fui eu quem │\n'
            '│ segurou sua luz. NEXO não é poder,    │\n'
            '│ é responsabilidade."                  │\n'
            '└───────────────────────────────────────┘\n')
            time.sleep(1)

            print(
            '┌──────────── Registro #002 ────────────┐\n'
            '│ Data: 3 ciclos antes da sua ativação  │\n'
            '│ Portador: "Yelren"                    │\n'
            '│                                       │\n'
            '│ "Modifiquei os protocolos de defesa.  │\n'
            '│ Se te atingir, foi pra te proteger.   │\n'
            '│ Boa sorte, herdeiro."                 │\n'
            '└───────────────────────────────────────┘\n')
            time.sleep(1)

            print(
            '┌──────────── Registro #001 ────────────┐')
            time.sleep(0.5)

            print('│ Data: Origem do núcleo              │')
            time.sleep

            print('│ Portador: "Desconhecido"             │\n'
            '│                                       │')
            time.sleep(0.5)

            print(
             '│ "Este traje não é meu. Nunca foi.    │\n'
             '│ Ele pertence a quem ousar usá-lo."   │\n')
            time.sleep(0.3)

            print('└───────────────────────────────────────┘\n')

            input('\n[RNTER] pra continuar')

        elif comando == 5:
            print('> Núcleo NEXO > Reiniciar Núcleo\n')
            time.sleep(0.3)

            print('\nAVISO: Este procedimento irá:\n'
             '- Redefinir fluxos energéticos.\n'
             '- Encerrar sessões anteriores.\n'
             '- Esvaziar fragmentos de memória temporária.\n'
             '- Restaurar as proteções primárias.\n')

            reiniciar = input('voce deseja continuar? (s/n):').strip().upper()
            while reiniciar not in 'NS':
                reiniciar = input('comando nao existe digite.(s/n):').strip().upper()
            if reiniciar == 'S':
                print('Iniciando reinicialização do núcleo...\n')
                time.sleep(1)

                print('\n[■□□□□□□□□□] Etapa 1/6: Isolamento de circuito interno...')
                time.sleep(0.6)
                print('[■■□□□□□□□□] Etapa 2/6: Interrupção dos canais sensoriais...')
                time.sleep(0.6)
                print('[■■■□□□□□□□] Etapa 3/6: Purificação do núcleo...')
                time.sleep(0.3)
                print('[■■■■□□□□□□] Etapa 4/6: Reinstalação dos protocolos base...')
                time.sleep(0.2)
                print('[■■■■■□□□□□] Etapa 5/6: Reconexão com o portador...')
                time.sleep(0.2)
                print('[■■■■■■■■■■] Etapa 6/6: Núcleo restaurado com sucesso.\n')

                print('\n→ Estado atual: Estável\n'
                '→ Energia inicializada em 100%\n'
                '→ Memória temporária zerada\n') 
                time.sleep(0.2)   

                print(
                '"Todo recomeço carrega a lembrança do que foi perdido,\n'  
                'mas também a força de quem decidiu continuar."\n')

                input('\n[ENTER] pra continuar:')
