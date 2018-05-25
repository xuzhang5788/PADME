#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:07:10 2017

@author: zqwu
"""
import deepchem

hps = {}
hps['tf'] = {
    'layer_sizes': [1500],
    'weight_init_stddevs': [0.02],
    'bias_init_consts': [1.],
    'dropouts': [0.5],
    'penalty': 0.1,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.001,
    'num_dense_layer': 3,
    'dense_cmb_layer_size': 512
}

hps['tf_robust'] = {
    'layer_sizes': [1500],
    'weight_init_stddevs': [0.02],
    'bias_init_consts': [1.],
    'dropouts': [0.5],
    'bypass_layer_sizes': [200],
    'bypass_weight_init_stddevs': [0.02],
    'bypass_bias_init_consts': [1.],
    'bypass_dropouts': [0.5],
    'penalty': 0.1,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.0005
}
hps['logreg'] = {
    'penalty': 0.1,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.005
}
hps['irv'] = {
    'penalty': 0.,
    'penalty_type': 'l2',
    'batch_size': 50,
    'nb_epoch': 10,
    'learning_rate': 0.001,
    'n_K': 10
}
hps['graphconv'] = {
    'batch_size': 64,
    'nb_epoch': 40,
    'learning_rate': 0.0005,
    'n_filters': 64,
    'n_fully_connected_nodes': 128,
    'dropout_prob': 0.2,
    'num_dense_layer': 3,
    'dense_cmb_layer_size': 512,
    'seed': 123
}
hps['dag'] = {
    'batch_size': 64,
    'nb_epoch': 50,
    'learning_rate': 0.0005,
    'n_graph_feat': 30,
    'default_max_atoms': 60,
    'seed': 123
}

hps['weave'] = {
    #'batch_size': 105,
    #'batch_size': 168,
    'batch_size': 230,
    'nb_epoch': 66,
    'learning_rate': 3.385e-5,
    #'n_graph_feat': 450,
    #'n_graph_feat': 248,
    'n_graph_feat': 194,
    'n_pair_feat': 14,
    #'n_hidden': 210,
    #'n_hidden': 202,
    'n_hidden': 509,
    #'dropout_prob': 0.1,
    #'dropout_prob': 0.15,
    'dropout_prob': 0.10025,
    'num_dense_layer': 3,
    'dense_cmb_layer_size': 512,
    'seed': 123
}
hps['textcnn'] = {
    'batch_size': 64,
    'nb_epoch': 40,
    'learning_rate': 0.0005,
    'n_embedding': 75,
    'filter_sizes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20],
    'num_filters': [100, 200, 200, 200, 200, 100, 100, 100, 100, 100, 160, 160],
    'seed': 123
}
hps['rf'] = {'n_estimators': 500}
hps['kernelsvm'] = {'C': 1.0, 'gamma': 0.05}
hps['xgb'] = {
    'max_depth': 5,
    'learning_rate': 0.05,
    'n_estimators': 3000,
    'gamma': 0.,
    'min_child_weight': 5,
    'max_delta_step': 1,
    'subsample': 0.53,
    'colsample_bytree': 0.66,
    'colsample_bylevel': 1,
    'reg_alpha': 0,
    'reg_lambda': 1,
    'scale_pos_weight': 1,
    'base_score': 0.5,
    'seed': 2016,
    'early_stopping_rounds': 100
}

hps['tf_regression'] = {
    'layer_sizes': [1000, 1000],
    'weight_init_stddevs': [0.02, 0.02],
    'bias_init_consts': [1., 1.],
    'dropouts': [0.25, 0.25],
    #'dropout_prob': 0.105,
    'dropout_prob': 0.262,
    'penalty': 0.0005,
    'penalty_type': 'l2',
    #'batch_size': 128,
    'batch_size': 155,
    'nb_epoch': 100,
    #'nb_epoch': 66,
    #'nb_epoch': 3,
    #'learning_rate': 0.0008,
    'learning_rate': 0.000311,
    #'num_dense_layer': 3,
    'num_dense_layer': 2,
    #'dense_cmb_layer_size': 512
    'dense_cmb_layer_size': 1211
}

hps['tf_regression_ft'] = {
    'layer_sizes': [400, 100, 100],
    'weight_init_stddevs': [0.05, 0.1, 0.1],
    'bias_init_consts': [0., 0., 0.],
    'dropouts': [0.01, 0.01, 0.01],
    'penalty': 0.,
    'penalty_type': 'l2',
    'batch_size': 25,
    'nb_epoch': 50,
    'learning_rate': 0.001,
    'fit_transformers': deepchem.trans.CoulombFitTransformer
}
hps['rf_regression'] = {'n_estimators': 500}
hps['krr'] = {'alpha': 1e-3}
hps['krr_ft'] = {'alpha': 1e-3}
hps['graphconvreg'] = {
    'batch_size': 128,
    #'batch_size': 86, 
    'nb_epoch': 100,
    #'nb_epoch': 3,
    #'nb_epoch': 63,
    #'learning_rate': 0.0002,
    'learning_rate': 9.789365954742421e-05,
    'n_filters': 128,
    #'n_filters': 160,
    'n_fully_connected_nodes': 256,
    #'n_fully_connected_nodes': 492,
    'dropout_prob': 0.1,
    #'dropout_prob': 0.03567783932490167,
    'num_dense_layer': 3,
    #'num_dense_layer': 8,
    'dense_cmb_layer_size': 512,
    #'dense_cmb_layer_size': 1317,
    'seed': 123
}

hps['dtnn'] = {
    'batch_size': 64,
    'nb_epoch': 100,
    'learning_rate': 0.001,
    'n_embedding': 50,
    'n_distance': 170,
    'seed': 123
}
hps['dag_regression'] = {
    'batch_size': 64,
    'nb_epoch': 100,
    'learning_rate': 0.0005,
    'n_graph_feat': 30,
    'default_max_atoms': 60,
    'seed': 123
}
hps['weave_regression'] = {
    #'batch_size': 110,
    #'batch_size': 93,
    'batch_size': 168,
    'nb_epoch': 100,
    #'learning_rate': 6.3e-5,
    'learning_rate': 5.233e-5,
    #'n_graph_feat': 450,
    #'n_graph_feat': 223,
    'n_graph_feat': 150,
    'n_pair_feat': 14,
    'n_hidden': 110,
    #'n_hidden': 251,
    #'n_hidden': 693,
    #'dropout_prob': 0.1,
    #'dropout_prob': 0.082,
    'dropout_prob': 0.1052,
    'num_dense_layer': 3,
    'dense_cmb_layer_size': 512,
    'seed': 123
}
hps['textcnn_regression'] = {
    'batch_size': 64,
    'nb_epoch': 100,
    'learning_rate': 0.0005,
    'n_embedding': 75,
    'filter_sizes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20],
    'num_filters': [100, 200, 200, 200, 200, 100, 100, 100, 100, 100, 160, 160],
    'seed': 123
}
hps['ani'] = {
    'batch_size': 32,
    'nb_epoch': 100,
    'learning_rate': 0.00005,
    'layer_structures': [20, 10, 10],
    'seed': 123
}
hps['mpnn'] = {
    'batch_size': 16,
    'nb_epoch': 50,
    'learning_rate': 0.001,
    'T': 2,
    'M': 5,
    'dropout_prob': 0.105,
    'num_dense_layer': 3,
    'dense_cmb_layer_size': 512,
    'seed': 123
}

hps['xgb_regression'] = {
    'max_depth': 5,
    'learning_rate': 0.05,
    'n_estimators': 3000,
    'gamma': 0.,
    'min_child_weight': 5,
    'max_delta_step': 1,
    'subsample': 0.53,
    'colsample_bytree': 0.66,
    'colsample_bylevel': 1,
    'reg_alpha': 0,
    'reg_lambda': 1,
    'scale_pos_weight': 1,
    'base_score': 0.5,
    'seed': 2016,
    'early_stopping_rounds': 100
}

hps['siamese'] = {
    'n_pos': 1,
    'n_neg': 1,
    'test_batch_size': 128,
    'n_filters': [64, 128, 64],
    'n_fully_connected_nodes': [128],
    'nb_epochs': 1,
    'n_train_trials': 2000,
    'n_eval_trials': 20,
    'learning_rate': 1e-4
}
hps['res'] = {
    'n_pos': 1,
    'n_neg': 1,
    'test_batch_size': 128,
    'n_filters': [64, 128, 64],
    'n_fully_connected_nodes': [128],
    'max_depth': 3,
    'nb_epochs': 1,
    'n_train_trials': 2000,
    'n_eval_trials': 20,
    'learning_rate': 1e-4
}
hps['attn'] = {
    'n_pos': 1,
    'n_neg': 1,
    'test_batch_size': 128,
    'n_filters': [64, 128, 64],
    'n_fully_connected_nodes': [128],
    'max_depth': 3,
    'nb_epochs': 1,
    'n_train_trials': 2000,
    'n_eval_trials': 20,
    'learning_rate': 1e-4
}
