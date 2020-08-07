PREDICTOR = {
    'iluminacao_column_names': [
        "Id",
        "Idra",
        "IdLogradouro",
        "IdPoste",
        'poste_numero',
        'coordenadaX',
        'coordenadaY',
        'vlsavis',
        'referencia',
        'poste_propriedade',
        'poste_status',
        'id_suporte',
        'IdLuminaria',
        'luminaria_numero',
        'altura_montagem',
        'IdLampada',
        'quantidade_lampada',
        'id_reator',
        'id_rele',
        'id_rede',
        'id_transformador',
        'id_medidor',
        'id_objecto_iluminado',
        'data_instalacao',
        'observacoes',
        'incluido_em',
        'id_usuario',
        'created_at',
        'update_at',
        'deleted_at'
    ],

    'solicitacao_column_names': [
        'id', 'idcidade', 'protocolo_sistema', 'protocolo_falasalvador', 'protocolo_consorcio', 'data_atendimento',
        'hora_atendimento', 'horaregistro', 'temporegistro', 'solicitante_nome', 'solicitante_telefone',
        'solicitante_email', 'poste_numero', 'luminaria_numero', 'idtiposolicitante', 'idtiposolicitacao',
        'idlogradouro_cadastro', 'idbairro_cadastro', 'visavis_cadastro', 'referencia_cadastro',
        'idlogradourotipo_informado', 'logradouro_descricao_informado', 'idbairro_informado', 'visavis_informado',
        'referencia_informado', 'dadoscomplementares', 'servicosolicitado', 'incluidoem', 'idusuario', 'idempresa',
        'enviado_impressao', 'enviado_mobile', 'enviado_mobile_idturma', 'data_execucao', 'hora_execucao', 'data_baixa',
        'hora_baixa', 'acao_adotada', 'servico_realizado', 'poste_numero_executado', 'luminaria_numero_executado',
        'iddefeitoencontrado', 'idcausadefeito', 'idturma', 'alterador_em', 'idusuarioalterou', 'sfs_informar_ciencia',
        'c_informar_ciencia', 'c_informar_concluida', 'sfs_informar_concluida', 'idfatura', 'tma_dias', 'tma_horas',
        'referencia_poste_executado', 'tipo_acao', 'motivo_acao', 'garantia', 'garantia_os_anterior', 'supervisor',
        'motivo_atraso', 'app_coordenada_x', 'app_coordenada_y', 'app_informacoes_gerais', 'controle_idturma',
        'controle_data_entrega', 'controle_data_recebido', 'controle_acao', 'controle_idmotivo', 'impressoem',
        'impressopor', 'os_separada_em', 'os_separada_por', 'os_separada_para', 'created_at', 'updated_at', 'deleted_at'
    ],
    'date_fields_solicitacao': [
        'data_atendimento', 'data_execucao', 'data_baixa'
    ]
}
