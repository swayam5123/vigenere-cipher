{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "762d3cf5-4fdc-4ae8-bc06-cf20797405c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Encrypted text: mrttaqrhknsw ih puggrur\n",
      "Key: python\n",
      "\n",
      "Decrypted text: xtammdcjrgej tj wnstcwy\n",
      "\n"
     ]
    }
   ],
   "source": [
    "text = 'mrttaqrhknsw ih puggrur'\n",
    "custom_key = 'python'\n",
    "\n",
    "def vigenere(message, key, direction=1):\n",
    "    key_index = 0\n",
    "    alphabet = 'abcdefghijklmnopqrstuvwxyz'\n",
    "    final_message = ''\n",
    "\n",
    "    for char in message.lower():\n",
    "\n",
    "        # Append any non-letter character to the message\n",
    "        if not char.isalpha():\n",
    "            final_message += char\n",
    "        else:        \n",
    "            # Find the right key character to encode/decode\n",
    "            key_char = key[key_index % len(key)]\n",
    "            key_index += 1\n",
    "\n",
    "            # Define the offset and the encrypted/decrypted letter\n",
    "            offset = alphabet.index(key_char)\n",
    "            index = alphabet.find(char)\n",
    "            new_index = (index + offset*direction) % len(alphabet)\n",
    "            final_message += alphabet[new_index]\n",
    "    \n",
    "    return final_message\n",
    "\n",
    "def encrypt(message, key):\n",
    "    return vigenere(message, key)\n",
    "    \n",
    "def decrypt(message, key):\n",
    "    return vigenere(message, key, -1)\n",
    "\n",
    "print(f'\\nEncrypted text: {text}')\n",
    "print(f'Key: {custom_key}')\n",
    "decryption = decrypt(text, custom_key)\n",
    "print(f'\\nDecrypted text: {decryption}\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb8eca26-3270-40d0-8367-10a43bc1ae21",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
