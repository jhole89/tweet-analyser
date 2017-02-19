# -*- coding: utf-8 -*-

from configparser import RawConfigParser

from src.authenticate import Authorise
from src.data_sourcing import analysis_decider, data_router
from src.data_wrangling import document_processing

if __name__ == '__main__':
    api_connection = Authorise

    api_keys = RawConfigParser()
    api_keys.read('resources/credentials.properties')
    c_key = api_keys.get('apiKeys', 'consumer.key')
    c_secret = api_keys.get('apiKeys', 'consumer.secret')
    t_key = api_keys.get('apiKeys', 'accessToken.key')
    t_secret = api_keys.get('apiKeys', 'accessToken.secret')

    twitter_connection = api_connection(c_key, c_secret, t_key, t_secret).request_auth().make_connection()

    source_choice = analysis_decider()
    all_tweets = data_router(source_choice, twitter_connection)

    word_counters, co_occ_matrix = document_processing(all_tweets)
