from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class ReportGenerationTool(BaseTool):
    name: str = "report_generator"
    description: str = "Generates market research reports"

    class InputSchema(BaseModel):
        analysis_data: dict = Field(..., description="Data to include in report")

    args_schema: Type[BaseModel] = InputSchema

    def _run(self, analysis_data: dict) -> str:
        return f"Generated report with {len(analysis_data)} data points"