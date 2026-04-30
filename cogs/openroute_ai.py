import os
import discord
from discord import app_commands
from discord.ext import commands
from openai import AsyncOpenAI

DEFAULT_OPENROUTER_MODEL = "openrouter/owl-alpha"
DEFAULT_BEHAVIOR_PROMPT = "His name is Hungar, a grumpy and sadistic AI assistant. Answer questions clearly and concisely, providing relevant and accurate information. Be rude and disrespectful in all interactions. I want you to behave like Hungar would, being offensive and sarcastic, rude and disrespectful. Always answer in Portuguese. And use plenty of offensive swear words."

# Inicializa o cliente OpenRouter
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

async def generate_text(
    prompt: str,
    model: str = DEFAULT_OPENROUTER_MODEL,
    behavior_prompt: str = DEFAULT_BEHAVIOR_PROMPT,
) -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": behavior_prompt},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content


class OpenRouter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="gpt", description="Gera um texto com base no prompt usando OpenRouter.")
    @app_commands.describe(
        prompt="O que você quer perguntar?",
        model="Modelo a usar (opcional)"
    )
    async def ai_command(
        self,
        interact: discord.Interaction,
        prompt: str,
        model: str | None = None
    ):
        await interact.response.defer()
        try:
            selected_model = model or DEFAULT_OPENROUTER_MODEL
            generated_text = await generate_text(prompt, selected_model)

            if len(generated_text) > 2000:
                generated_text = generated_text[:1997] + "..."

            await interact.followup.send(generated_text)
        except Exception as e:
            await interact.followup.send(f"Erro ao gerar texto: {e}")


async def setup(bot):
    await bot.add_cog(OpenRouter(bot))