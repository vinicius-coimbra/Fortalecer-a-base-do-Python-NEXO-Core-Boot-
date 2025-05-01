import time

while True:
    print('[1] composiçáo do traje\n'
    '[2] protocolos de inicializacão\n'
    '[3] status de energia\n'
    '[4] memorias anteriores\n'
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
             print('\nnucleo NEXO > composição do traje\n'
            '\n'
            'Camadas Ativadas:' + '\n'
             '├─ [✓] Fibras de Carbono Vivas' + '\n' +
             '├─ [✓] Liga Óssea Reforçada' + '\n' +
             '├─ [✓] Núcleo Arcano de Condutividade' + '\n' +
             '└─ [✓] Malha de Isolamento Sensorial' + '\n' +
             '└─ [x] Eco de Memória Residual' + '\n' + '\n' +
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

             print(' - [✓] Verificação de Identidade')
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