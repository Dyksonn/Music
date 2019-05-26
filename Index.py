from time import sleep
import getpass
import webbrowser
print()
print(' ' * 5, '♫-♫-♫-♫-♫-♫-♫- Music -♪-♪-♪-♪-♪-♪-♪-♪')
print()
print(' ' * 12, 'Olá. Bem Vindo a MUSIC ‼ \n')
cadastro = str(input('Deseja fazer um cadastro na music ? (sim/não)\n'))
if cadastro.lower() == 'sim':
    print('_' * 80)
    print()
    nome = str(input('Digite seu nome: '))
    print('_' * 80)
    print()
    print(' ' * 5, 'Então vamos lá {}, crie seu nome de usuário e uma senha numérica.'.format(nome))
    print('_' * 80)
    print()
    usuario = str(input('Usuário: '))
    while True:
        try:
            senha = int(input('Senha: '))
            break
        except ValueError:
            print('Apenas números!')
    print('_' * 80)
    print()
    print(' ' * 5, 'Perfeito.Você está cadastrado.'.center(65))
    print('_'*80)
    print()
    print(' ' * 2, 'Vamos acessar sua conta.')
    while True:
        usuCadastrado = str(input('Digite o usuário cadastrado: '))
        senhaCadastrada = int(getpass.getpass('Digite sua senha cadastrada:'))
        # senhaCadastrada = int(input('Digite sua senha cadastrada: '))
        if usuario.lower() == usuCadastrado.lower():
            if senha == senhaCadastrada:
                print('_'*80)
                print()
                print('Acesso liberado.'.center(75))
                break
        elif usuario != usuCadastrado:
            if senha != senhaCadastrada:
                print()
                print('Senha ou usuário inválidos!\n')
    print('_'*80)
    print()
    animacao = input(
        'Precione a tecla enter para ver alguns gêneros musicais.')
    print()
    sleep(0.1)
    print(' '*1, '♫')
    sleep(0.1)
    print(' '*2, '♪')
    sleep(0.1)
    print(' '*3, '♫')
    sleep(0.1)
    print(' '*4, '♪')
    sleep(0.1)
    print(' '*5, '♫')
    sleep(1)
    listaGeneros = ['Jazz', 'Axé', 'Blues', 'Country', 'Eletrônica', 'Forró', 'Funk', 'Gospel',
                    'Hip Hop', 'MPB', 'Música clássica', 'Pagode', 'Pop', 'Rap', 'Reggae', 'Rock', 'Samba', 'Sertanejo']
    for ls in (listaGeneros):
        print(' ' * 5, ls)

    def curio(cur):
        tam = len(cur)
        print()
        print(cur)
        print('_' * tam)

    curio('Agora que viu alguns dos gêneros. Queremos te conhecer melhor e mostrar à você algumas curiosidades.')

    print()
    while True:
        try:
            nascimento = int(input('Digite o ano do seu nascimento: '))
            print('_'*140)
            break
        except ValueError:
            print('Cuidado, não coloque qualquer outro tipo de caractere à não ser número.')
    
    if nascimento >= 2010:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu a eletrônica.')
    elif nascimento >= 2000:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o raggae.')
    elif nascimento >= 1995:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o rap.')
    elif nascimento >= 1985:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o funk.')
    elif nascimento >= 1975:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o axé.')
    elif nascimento >= 1965:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o hip hop.')  
    elif nascimento >= 1955:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o sertanejo.')  
    elif nascimento >= 1945:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o pagode.')  
    elif nascimento >= 1935:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o rock.')  
    elif nascimento >= 1925:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o samba.')  
    elif nascimento >= 1915:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o gospel.')
    elif nascimento >= 1900:
        print()
        print('Que bacana! Você nasceu aproximadamente na época em que surgiu o forró.')

    def mensagem(msg):
        tam = len(msg)
        print(msg)
        print('_' * tam)
    resoluNascimento = (2019 - nascimento)
    mensagem('Hoje com os seus {} anos, os genêros mais populares atualmente no Brasil, segundo as pesquisas são: Funk, Forró, Gospel e Sertanejo.'.format(resoluNascimento))
    
    music = str(input('Deseja ouvir uma musica? Sim/Não '))
    print('')
    if music.lower() == 'sim':
        while True:
            listaGeneros = ['Jazz', 'Axé', 'Blues', 'Country', 'Eletrônica', 'Forró', 'Funk', 'Gospel',
                            'Hip Hop', 'MPB', 'Música clássica', 'Pagode', 'Pop', 'Rap', 'Reggae', 'Rock', 'Samba', 'Sertanejo']
            for xs, ls in enumerate(listaGeneros):
                print(f'({xs + 1})', ls)
            ouvir = int(input('Selecione o numero da opção que deseja: '))
            print('')
            ouvir -= 1
            refer = listaGeneros[ouvir]
            print(f'Opção escolhida: {refer}')
            print('')

            musica = {
                'Jazz': [
                    'So What - Miles Davis',
                    'Frank Sinatra Fly Me To The Moon - Frank Sinatra'
                ],
                'Axé': [
                    'SWING DA COR - DANIELA MERCURY',
                    'MARGARETH MENEZES DANDALUNDA'
                ],
                'Blues': [
                    'Hellhound On My Trail - Robert Johnson',
                    'Mannish Boy - Muddy Waters'
                ],
                'Country': [
                    'There You’ll Be da - Faith Hill ',
                    'Indian Outlaw do - Tim McGraw'
                ],
                'Eletrônica': [
                    'JetLag, Anitta - Zé do Caroço',
                    'Alok, Bruno Martini, Zeeba - Never Let Me Go'
                ],
                'Forró': [
                    'Wesley Safadão - Só Pra Castigar',
                    'Gabriel Diniz - Acabou Acabou'
                ],
                'Funk': [
                    'Só depois do carnaval - lexa',
                    'Só você - Dennis Dj'
                ],
                'Gospel': [
                    'Lugar secreto - Gabriela Rocha',
                    'Ninguém explica Deus - Preto no Branco'
                ],
                'Hip Hop': [
                    'Old Town Road - Lil Nas X ft. Billy Ray Cyrus',
                    'Sally Walker - Iggy Azalea'
                ],
                'MPB': [
                    'Águas de Março - Elis Regina e Tom Jobim',
                    'Chega de Saudade - João Gilberto'
                ],
                'Música clássica': [
                    'Lustiges Zusammensein der Landleute - Beethoven',
                    'Gewitter, Sturm - Beethoven'
                ],
                'Pagode': [
                    'Péssimo negócio - Dilsinho',
                    'Chopp garotinho - Ferrugem'
                ],
                'Pop': [
                    ' SHALLOW (A STAR IS BORN) FT BRADLEY COOPER - Lady Gaga',
                    'PROMISES FT SAM SMITH - Calvin Harris'
                ],
                'Rap': [
                    'Balão - Orochi',
                    'Beijo com Trap - Hungria'
                ],
                'Reggae': [
                    'Exodus - Bob Marley & The Wailers',
                    'Black Woman - Judy Mowatt'
                ],
                'Rock': [
                    'Aerosmith - Sweet Emotion',
                    'AC/DC - Back in Black'
                ],
                'Samba': [
                    'Dona Duda Ribeiro - Não Deixe o Samba Morrer',
                    'Exaltasamba - Acaba Tudo Bem'
                ],
                'Sertanejo': [
                    'Marilia Mendonça - Todo mundo vai sofrer',
                    'Gusttavo lima - Cem mil'
                ]
            }

            for sx, sl in enumerate(musica[refer]):
                print(f'({sx + 1})', sl)
            print('')

            def pesquisa(url):
                webbrowser.open(url, new=1, autoraise=True)
            
            escolha = str(input('Escolha o número da musica que deseja ouvir: '))
            print('')
            if refer == 'Jazz' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=zqNTltOGh5c'
                pesquisa(url)
            elif refer == 'Jazz' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=mQR0bXO_yI8'
                pesquisa(url)
            elif refer == 'Axé' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=z1WRZDOGHlY'
                pesquisa(url)
            elif refer == 'Axé' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=Rd4OXsjJXFI'
                pesquisa(url)
            elif refer == 'Blues' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=hJqv--Ya7hk'
                pesquisa(url)
            elif refer == 'Blues' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=bSfqNEvykv0'
                pesquisa(url)
            elif refer == 'Country' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=BwyWmqV_RJc'
                pesquisa(url)
            elif refer == 'Country' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=kqlR4IEl_04'
                pesquisa(url)
            elif refer == 'Eletrônica' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=3Jo9RKmumGE'
                pesquisa(url)
            elif refer == 'Eletrônica' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=ri-fIya76ac'
                pesquisa(url)
            elif refer == 'Forró' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=V_w_KA1VKoQ'
                pesquisa(url)
            elif refer == 'Forró' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=FJOoPAEvIdM'
                pesquisa(url)
            elif refer == 'Funk' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=b78_dITFwy8'
                pesquisa(url)
            elif refer == 'Funk' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=um6fQzRg4hE'
                pesquisa(url)
            elif refer == 'Gospel' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=YnrN0o0lubM'
                pesquisa(url)
            elif refer == 'Gospel' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=LYsaKn8FRhc'
                pesquisa(url)
            elif refer == 'Hip Hop' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=gUcisIlT7sM'
                pesquisa(url)
            elif refer == 'Hip Hop' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=2Gy8eGr7AfM'
                pesquisa(url)
            elif refer == 'MPB' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=E1tOV7y94DY'
                pesquisa(url)
            elif refer == 'MPB' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=yUuJrpP0Mak'
                pesquisa(url)
            elif refer == 'Música clássica' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=ln8baOpLmaE'
                pesquisa(url)
            elif refer == 'Música clássica' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=VVSMNtTzy4U'
                pesquisa(url)
            elif refer == 'Pagode' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=4uQi5XvGI1M'
                pesquisa(url)
            elif refer == 'Pagode' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=ujHm8Rx5Vh4'
                pesquisa(url)
            elif refer == 'Pop' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=bo_efYhYU2A'
                pesquisa(url)
            elif refer == 'Pop' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=kkLk2XWMBf8'
                pesquisa(url)
            elif refer == 'Rap' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=L8_116bLouo'
                pesquisa(url)
            elif refer == 'Rap' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=63XyWeKWI0M'
                pesquisa(url)
            elif refer == 'Reggae' and escolha == '1':
                url = 'hhttps://www.youtube.com/watch?v=nv584jRwh0s'
                pesquisa(url)
            elif refer == 'Reggae' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=jHUQg5rvBEg'
                pesquisa(url)
            elif refer == 'Rock' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=D0EpGrvDXDM'
                pesquisa(url)
            elif refer == 'Rock' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=pAgnJDJN4VA'
                pesquisa(url)
            elif refer == 'Samba' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=N0yqCO7kWUU'
                pesquisa(url)
            elif refer == 'Samba' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=yID2bKez9M8'
                pesquisa(url)
            elif refer == 'Sertanejo' and escolha == '1':
                url = 'https://www.youtube.com/watch?v=ILADw1aretk'
                pesquisa(url)
            elif refer == 'Sertanejo' and escolha == '2':
                url = 'https://www.youtube.com/watch?v=5YIK4b7fNeo'
                pesquisa(url)
            else:
                print('Opção Invalida, vamos tentar novamente...')
                print(' ')
            choice = str(input('Deseja fazer uma nova busca de musica? Sim/Não '))
            if choice.lower() == 'não' or choice.lower() == 'nao':
                print('')
                print('Saindo do login, bj.')
                break 
            elif choice.lower() == 'sim':
                continue
            else:
                print('Opção invalida, finalizando programa')
                break

    elif music.lower() == 'nao' or music.lower() == 'não':
        print('Ta ok')


elif cadastro.lower() == 'nao' or cadastro.lower() == 'não':
    print('OK, Até a proxima!')
