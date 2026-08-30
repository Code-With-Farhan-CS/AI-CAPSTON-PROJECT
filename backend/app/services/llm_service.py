# import os
# from pathlib import Path
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# load_dotenv(dotenv_path=BASE_DIR / ".env")
# load_dotenv()

# class LLMService:
#     def __init__(self):
#         # 🔑 Groq API Key (Replace with your actual 'gsk_...' key)
#         self.api_key = os.getenv("GROQ_API_KEY") or "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"
        
#         if not self.api_key or self.api_key == "gsk_YOUR_GROQ_API_KEY_HERE":
#             raise ValueError("GROQ_API_KEY is not configured properly.")
        
#         # Initialize Groq Client
#         self.client = Groq(api_key=self.api_key)
#         # Ultra fast & powerful model (falls back to groq/compound)
#         self.model_name = os.getenv("GROQ_MODEL_NAME") or "groq/compound"

#     async def generate_response(self, prompt: str, system_instruction: str = None) -> str:
#         try:
#             messages = []
#             if system_instruction:
#                 messages.append({"role": "system", "content": system_instruction})
            
#             messages.append({"role": "user", "content": prompt})

#             response = self.client.chat.completions.create(
#                 model=self.model_name,
#                 messages=messages,
#                 temperature=0.7,
#                 max_tokens=1024,
#             )
#             return response.choices[0].message.content
#         except Exception as e:
#             print("\n[ERROR] GROQ API ERROR:", str(e), "\n")
#             raise Exception(f"Groq AI Generation Error: {str(e)}")

#     async def generate_with_context(self, prompt: str, context: str) -> str:
#         full_prompt = f"Context:\n{context}\n\nUser Prompt:\n{prompt}"
#         return await self.generate_response(full_prompt)

#     async def refine_text(self, text: str, instruction: str) -> str:
#         refine_prompt = f"Original Text:\n{text}\n\nInstruction for Refinement:\n{instruction}"
#         return await self.generate_response(refine_prompt)

# llm_service = LLMService()

import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")
load_dotenv()


class LLMService:
    def __init__(self):
        # Read API key strictly from environment variables
        self.api_key = os.getenv("GROQ_API_KEY")

        if not self.api_key or self.api_key == "gsk_YOUR_GROQ_API_KEY_HERE":
            raise ValueError(
                "GROQ_API_KEY is not configured properly in your .env file."
            )

        # Initialize Groq Client
        self.client = Groq(api_key=self.api_key)
        self.model_name = os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-versatile")

    async def generate_response(
        self, prompt: str, system_instruction: str = None
    ) -> str:
        try:
            messages = []
            if system_instruction:
                messages.append(
                    {"role": "system", "content": system_instruction}
                )

            messages.append({"role": "user", "content": prompt})

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7,
                max_tokens=1024,
            )
            return response.choices[0].message.content
        except Exception as e:
            print("\n[ERROR] GROQ API ERROR:", str(e), "\n")
            raise Exception(f"Groq AI Generation Error: {str(e)}")

    async def generate_with_context(self, prompt: str, context: str) -> str:
        full_prompt = f"Context:\n{context}\n\nUser Prompt:\n{prompt}"
        return await self.generate_response(full_prompt)

    async def refine_text(self, text: str, instruction: str) -> str:
        refine_prompt = (
            f"Original Text:\n{text}\n\nInstruction for Refinement:\n{instruction}"
        )
        return await self.generate_response(refine_prompt)


llm_service = LLMService()