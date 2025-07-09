import asyncio
import logging
from pipecat.frames.frames import App
from src.services.twilio_service import TwilioService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoiceAgent:
    def __init__(self):
        self.twilio_service = TwilioService()

    async def handle_incoming_call(self, call_sid, from_number, to_number):
        logger.info(f"Handling incoming call: {call_sid} from {from_number} to {to_number}")
        # Placeholder for call routing logic
        # Example: transfer call to another number
        # self.twilio_service.make_call(to_number="<TRANSFER_NUMBER>", from_number=to_number, twiml_url="<TWIML_URL>")
        pass

    async def main(self):
        app = App()
        # Add your agent logic here
        try:
            await app.run()
        except Exception as e:
            logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    agent = VoiceAgent()
    asyncio.run(agent.main())
