from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from database.database import Trade
from models.models_main import InputQuery


def check_query_to_perform(query: InputQuery, session_maker: sessionmaker):
    match query.index:
        case 1:
            with session_maker() as session:
                trades = session.query(Trade).all()
                return queries_return(trades)
        case 2:
            with session_maker() as session:
                trades = session.query(Trade).filter(Trade.price > query.price)
                return queries_return(trades)
        case 3:
            with session_maker() as session:
                trades = (
                    session.query(Trade)
                    .filter(Trade.price > query.price)
                    .filter(Trade.active == query.active)
                )
                return queries_return(trades)
        case 4:
            with session_maker() as session:
                trades = session.query(Trade).filter(Trade.price < query.price)
                return queries_return(trades)
        case 5:
            with session_maker() as session:
                trades = (
                    session.query(Trade)
                    .filter(Trade.price < query.price)
                    .filter(Trade.active == query.active)
                )
                return queries_return(trades)
        case 6:
            with session_maker() as session:
                trades = (
                    session.query(Trade)
                    .order_by(Trade.datetime.desc())
                    .filter(Trade.active == query.active)
                    .first()
                )
                return queries_return(trades)

        case 7:
            with session_maker() as session:
                trades = session.query(Trade).order_by(Trade.datetime.desc()).first()
                return queries_return(trades)
        case 8:
            with session_maker() as session:
                trades = session.query(Trade.active, func.sum(Trade.price)).group_by(
                    Trade.active
                )
                return queries_return(trades)


def queries_return(trades):
    try:
        list_of_trade = []

        for iten in trades:
            dict_new = {
                "id": iten.id,
                "active": iten.active,
                "price": iten.price,
                "datetime": iten.datetime.strftime("%d/%m/%Y %H:%M"),
            }

            list_of_trade.append(dict_new)
        return list_of_trade
    except TypeError:
        return {
            "id": trades.id,
            "active": trades.active,
            "price": trades.price,
            "datetime": trades.datetime.strftime("%d/%m/%Y %H:%M"),
        }
    except AttributeError:
        list_of_trade = []

        for iten in trades:
            dict_new = {
                "active": iten.active,
                "price": round(iten[1], 2),
            }

            list_of_trade.append(dict_new)
        return list_of_trade
