from abc import ABCMeta, abstractmethod
from typing import List

class IPagamento(ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def pagar(self):
        pass

class CartaoCredito(IPagamento):

    def pagar(self):
        return "Pagamento realizado com cartão de crédito"
    
class Boleto(IPagamento):

    def pagar(self):
        return "Pagamento realizado com boleto bancário"

def formas_pagamentos(formas: List[IPagamento]):
    for forma in formas:
        print(forma.pagar())