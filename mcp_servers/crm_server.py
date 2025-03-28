from modelcontextprotocol import Protocol, Tool
import json

protocol = Protocol()

def get_contract_status(params):
    contract_id = params.get("contract_id")
    with open("data/contracts.json", "r") as f:
        data = json.load(f)
    for contract in data["contracts"]:
        if contract["id"] == contract_id:
            return f"Status: {contract['status']}, Signed: {contract['signed_date']}"
    return "Contract not found."

contract_tool = Tool(
    name="get_contract_status",
    description="Fetch contract status by ID",
    parameters={"contract_id": "string"},
    handler=get_contract_status
)

protocol.set_request_handler("list_tools", lambda request: {"tools": [contract_tool.to_dict()]})
protocol.set_request_handler("get_contract_status", get_contract_status)

if __name__ == "__main__":
    protocol.run_stdio()
