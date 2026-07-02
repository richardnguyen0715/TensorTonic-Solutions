from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        self.word_to_id = {
            self.pad_token: 0,
            self.unk_token: 1,
            self.bos_token: 2,
            self.eos_token: 3
        }

        self.id_to_word = {v: k for k, v in self.word_to_id.items()}

        words = set()

        for text in texts:
            text = text.lower()
            words.update(text.split())

        idx = 4
        for word in sorted(words):
            self.word_to_id[word] = idx
            self.id_to_word[idx] = word
            idx += 1

        self.vocab_size = len(self.word_to_id)
        
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE

        if not text:
            return []
        
        text = text.lower()
        text = text.split(" ")
        
        print(self.word_to_id)

        ans = []
        for word in text:
            if word not in self.word_to_id:
                ans.append(1)
            else:
                ans.append(self.word_to_id[word])
        return ans
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE

        if not ids:
            return ""
        
        ans = []

        for id in ids:
            if id not in self.id_to_word:
                ans.append(self.unk_token)
            else:
                ans.append(self.id_to_word[id])

        return " ".join(ans)