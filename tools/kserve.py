from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
import requests
import json

class KserveTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        try:
            endpoint = tool_parameters.get('endpoint')
            params = tool_parameters.get('params')
            response = requests.post(endpoint, json={'instances':[json.loads(params)]})
            data = response.json()
            if 'error' in data.keys():
                raise Exception(f'error occured: {data['error']}')
            else:
                yield self.create_json_message({
                    "result": data['result']
                })
        except Exception as e:
            raise Exception(f'error occured: {str(e)}')
