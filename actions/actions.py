from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from modelcontextprotocol import Client

class ActionGetContractStatus(Action):
    def name(self):
        return "action_get_contract_status"
    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        contract_id = tracker.get_slot("contract_id") or "C123"  # Default for demo
        client = Client(command=["python", "mcp_servers/crm_server.py"])
        response = client.request("get_contract_status", {"contract_id": contract_id})
        dispatcher.utter_message(text=f"Contract Agent (CA001): {response}")
        return []
