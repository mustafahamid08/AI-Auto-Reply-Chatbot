import time
import pyautogui
import pyperclip


def generate_reply(chat_history):
    text = chat_history.lower()

    # Greeting replies
    if "hello" in text or "hi" in text or "hey" in text:
        return "Hey! 👋 How are you doing?"

    # How are you
    elif "how are you" in text:
        return "I'm doing great! 😄 What about you?"

    # Thanks
    elif "thank" in text or "thanks" in text:
        return "You're welcome! 😊"

    # Goodbye
    elif "bye" in text or "goodbye" in text:
        return "Bye! 👋 Talk to you later."

    # Help
    elif "help" in text:
        return "Sure! Tell me what you need help with."

    # Project related
    elif "project" in text:
        return "That sounds interesting! Tell me more about your project."

    # Study related
    elif "study" in text or "exam" in text:
        return "Keep going! 📚 Consistency is the key to success."

    # Work related
    elif "work" in text or "job" in text:
        return "Sounds good! 💻 Keep working towards your goals."

    # Default smart reply
    else:
        return "That's interesting! 😄 Tell me more about it."


print("======================================")
print("      AI AUTO REPLY CHATBOT")
print("======================================")
print("Demo Mode: Offline")
print("Chatbot started successfully!")
print("Open your chat application.")
print("Press Ctrl+C to stop.")
print()

time.sleep(3)


while True:

    try:
        # Select chat history
        pyautogui.moveTo(700, 300, duration=0.2)
        pyautogui.dragTo(
            700,
            700,
            duration=0.5,
            button="left"
        )

        # Copy selected messages
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)

        # Read copied text
        chat_history = pyperclip.paste()

        if not chat_history.strip():
            print("No chat history found.")
            time.sleep(3)
            continue

        print("\nChat History:")
        print(chat_history)

        # Generate reply
        reply = generate_reply(chat_history)

        print("\nGenerated Reply:")
        print(reply)

        # Copy generated reply
        pyperclip.copy(reply)

        # Click message box
        pyautogui.click(700, 750)

        # Paste reply
        pyautogui.hotkey("ctrl", "v")

        # Send message
        pyautogui.press("enter")

        print("Reply sent successfully! ✅")

        # Wait before next message
        time.sleep(3)

    except KeyboardInterrupt:
        print("\nChatbot stopped.")
        break

    except Exception as e:
        print("\nError:", e)
        print("Retrying...")
        time.sleep(3)