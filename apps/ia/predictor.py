import pandas as pd
import numpy as np
import app_constants


class FailPredictor:

    def __init__(self, *args, **kwargs):
        self.iluminacao_path = 'data/' + kwargs.get('iluminacao_path')
        self.solicitacao_path = 'data/' + kwargs.get('solicitacao_path')
        self.df_iluminacao = None
        self.df_solicitacao = None

    def get_data(self, days_offset=2050):
        self.df_iluminacao = pd.read_csv(
            self.iluminacao_path,
            names=app_constants.PREDICTOR['iluminacao_column_names']
        )

        self.df_solicitacao = pd.read_csv(
            self.solicitacao_path,
            names=app_constants.PREDICTOR['solicitacao_column_names']
        )
        self.df_solicitacao['data_execucao'] = pd.to_datetime(self.df_solicitacao['data_execucao'], format='%Y-%m-%d',
                                                              errors='coerce')
        self.df_solicitacao['data_atendimento'] = pd.to_datetime(self.df_solicitacao['data_atendimento'],
                                                                 format='%Y-%m-%d',
                                                                 errors='coerce')
        df_sol = self.df_solicitacao[pd.DataFrame.notna(self.df_solicitacao['luminaria_numero'])]
        df_sol = df_sol[pd.DataFrame.notna(df_sol['data_execucao'])]

        df_sol = df_sol[df_sol['luminaria_numero'] != 0]
        df_sol = df_sol.sort_values(by=['data_execucao'])
        df_sol = df_sol[(pd.to_datetime('now') - df_sol['data_execucao']).dt.days > days_offset]

        luminaria_ids = df_sol['luminaria_numero'].to_list()
        luminaria_ids = (list(set(luminaria_ids)))

        mtbf = (self.lamp_mtbf(luminaria_ids, df_sol))
        mttr = self.lamp_mttf(luminaria_ids, df_sol)
        df_media_dias = pd.read_csv('data/out.csv')
        df_media_dias.dropna(inplace=True)
        return (mtbf / (mtbf + mttr)), mttr, mtbf, days_offset, df_sol.shape[0]

    def lamp_mtbf(self, luminaria_ids, df_solicitacoes):
        media_dias = []
        for i, luminaria in enumerate(luminaria_ids):
            df = pd.DataFrame()
            df['data_execucao'] = df_solicitacoes[df_solicitacoes['luminaria_numero'] == luminaria]['data_execucao']
            # min_date = df_solicitacoes[df_solicitacoes['luminaria_numero'] == luminaria]['data_execucao'].min()
            # max_date = df_solicitacoes[df_solicitacoes['luminaria_numero'] == luminaria]['data_execucao'].max()
            df['previous_date'] = df['data_execucao'].shift()
            df['days_between_execution'] = df['data_execucao'] - df['previous_date']
            df['days_between_execution'] = df['days_between_execution'].apply(lambda x: x.days)
            media_dias.append(df['days_between_execution'].agg('mean'))
        return pd.DataFrame(media_dias)[0].mean()

    def lamp_mttf(self, luminarias_ids, df_solicitacoes):
        media_dias = []
        for i, luminaria in enumerate(luminarias_ids):
            df = pd.DataFrame()
            df['data_execucao'] = df_solicitacoes[df_solicitacoes['luminaria_numero'] == luminaria]['data_execucao']
            df['data_atendimento'] = df_solicitacoes[df_solicitacoes['luminaria_numero'] == luminaria][
                'data_atendimento']

            df['difference'] = (df['data_execucao'] - df['data_atendimento'])

            if df[df['difference'].dt.days > 0]['difference'].mean().days is np.nan:
                media_dias.append(0)
            else:
                media_dias.append(df[df['difference'].dt.days > 0]['difference'].mean().days)
        return pd.DataFrame(media_dias)[0].mean()

    def transform_string_in_dates(self, df, label, format="%Y-%m-%d"):
        return pd.to_datetime(df[label], format, errors='coerce')


predictor = FailPredictor(
    iluminacao_path="iluminacao_publicas.csv",
    solicitacao_path="solicitacao_reclamacaos.csv"
)

disponibilidade_por_ano = []
years = []
for i in range(3, 7):
    years.append(i * 365)


def const_disponibilidade():
    for year in years:
        yield predictor.get_data(days_offset=year)

for disponibilidade in const_disponibilidade():
    print(disponibilidade)


