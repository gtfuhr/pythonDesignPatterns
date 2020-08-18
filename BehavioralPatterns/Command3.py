#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Command.

The command pattern has four main components: Command, ConcreteCommand,
Invoker and Receiver.
"""

from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    """Metaclass made to be inherited by the concrete Order(Command)."""

    @abstractmethod
    def execute(self):
        """Abstract execute method."""
        pass


class BuyStockOrder(Order):
    """Command class."""

    def __init__(self, stock):
        """Initialize the ConcreteCommand Class."""
        self.stock = stock

    def execute(self):
        """Execute buy."""
        self.stock.buy()


class SellStockOrder(Order):
    """Command class."""

    def __init__(self, stock):
        """Initialize the ConcreteCommand Class."""
        self.stock = stock

    def execute(self):
        """Execute buy."""
        self.stock.sell()


class StockTrade:
    """Receiver class."""

    def buy(self):
        """Buy stocks."""
        print("You will buy some stocks")

    def sell(self):
        """Sell stocks."""
        print("You will sell some stocks")


class Agent:
    """Invoker class."""

    def __init__(self):
        """Initialize the Invoker/Agent class."""
        self.__orderQueue = []

    def placeOrder(self, order):
        """Make some command."""
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':
    # Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # Chamador
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
