from typing import Any, Dict
import flask



db_module_path = "skip_db_lib.database.customers.CustomerDatabase"


def test_get_customer_by_id(app: flask.Flask , test_id: str, test_customer: Dict[str, Any], mocker):

    with app.app_context():
        from skip_db_lib.database.customers import CustomerDatabase
        
        mocker.patch(
            f"{db_module_path}.get_customer_by_id._get_coll", return_value=
        )

        mocker.patch(
            f"{db_module_path}.get_customer_by_id._get_coll.find_one", return_value=test_customer
        )


        customer = CustomerDatabase.get_customer_by_id(test_id)
        assert customer.get("_id") == test_id