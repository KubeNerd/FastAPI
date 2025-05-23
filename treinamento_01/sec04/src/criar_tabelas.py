# from core.configs import settings
# from core.database import engine

# async def create_tables() -> None:
#     import models.__all_models
#     print('Criando as tabelas no banco de dados....')

#     async with engine.begin() as conn:
#         await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
#         await conn.run_sync(settings.DBBaseModel.metadata.create_all)


# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(create_tables())


from core.configs import settings       # IMPORTAÇÃO DAS CONFIGURAÇÕES CRIADAS POR MIM - CLASSE DE CONFIGURAÇÕES GERAIS
from core.database import engine        # IMPORTAÇÃO DO MOTOR DE CONEXÃO COM O BANCO DE DADOS

async def criar_tabelas() -> None:                                         # Função para criar as tabelas
    import models.__all_models                                             # Importa todos os modelos
    print('Criando tabelas...')                                            # Imprime na tela

    async with engine.begin() as conn:                                          # Inicia a conexão com o banco de dados
                await conn.run_sync(settings.DBBaseModel.metadata.drop_all)     # Deleta todas as tabelas
                await conn.run_sync(settings.DBBaseModel.metadata.create_all)   # Cria todas as tabelas
                print('Tabela criada com sucesso!')                             # Imprime na tela

if __name__ == '__main__': # BLOCO DE EXECUÇÃO
    import asyncio               # Importa o módulo asyncio
    import platform              # Importa o módulo platform

    if platform.system() == 'Windows':  # Verifica se o sistema operacional é Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Define o loop de eventos do asyncio

    asyncio.run(criar_tabelas()) # Executa a função criar_tabelas