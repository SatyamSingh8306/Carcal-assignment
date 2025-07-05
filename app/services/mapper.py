from typing import Optional, Dict, Any
from app.services.agent import agent, _llm
from app.services.promtps import format_prompt, prompt
from app.types.response import WimbledonResult

_agent_chain = prompt | agent
_llm = format_prompt |  _llm.with_structured_output(WimbledonResult)

"""Connection for Databse"""
class WimbledonDataSource:
    """Agents are checking online and formating the result"""
    def get_final(self, year: int) -> Optional[Dict[str, Any]]:
        # Searching and creating the required format

        result = _agent_chain.invoke({"years" : year})
        ans = _llm.invoke({"raw_data" : result})
        
        return ans

# Singleton instance for use in routes
wimbledon_data_source = WimbledonDataSource()