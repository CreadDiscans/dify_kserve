from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class KserveTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        
        endpoint = tool_parameters.get("endpoint")
        params = tool_parameters.get('params')

        try:
            res = requests.post(endpoint, json=params)
            body = res.json()
            if 'error' in body.keys():
                raise Exception(f'erro occured: {body['error']}')
            else:
                yield body['result']
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")