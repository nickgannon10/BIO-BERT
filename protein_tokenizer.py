from transformers import PreTrainedTokenizer
from typing import List, Dict

class ProteinTokenizer(PreTrainedTokenizer):
    def __init__(self):
        self.amino_acids = "ACDEFGHIKLMNPQRSTVWY"
        self.special_tokens = {"pad_token": "[PAD]", "mask_token": "[MASK]", "unk_token": "[UNK]", "cls_token": "[CLS]", "sep_token": "[SEP]"}
        self.all_tokens = list(self.amino_acids) + list(self.special_tokens.values())
        self.token_to_id = {token: i for i, token in enumerate(self.all_tokens)}
        self.id_to_token = {i: token for token, i in self.token_to_id.items()}

        super().__init__(pad_token=self.special_tokens["pad_token"],
                         mask_token=self.special_tokens["mask_token"],
                         unk_token=self.special_tokens["unk_token"],
                         cls_token=self.special_tokens["cls_token"],
                         sep_token=self.special_tokens["sep_token"])

    def _tokenize(self, sequence: str) -> List[str]:
        return [char.upper() if char.upper() in self.amino_acids else self.unk_token for char in sequence]

    def _convert_token_to_id(self, token: str) -> int:
        return self.token_to_id.get(token, self.token_to_id[self.unk_token])

    def _convert_id_to_token(self, index: int) -> str:
        return self.id_to_token.get(index, self.unk_token)

    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        return "".join(tokens)

    def get_vocab(self) -> Dict[str, int]:
        return self.token_to_id

    @property
    def vocab_size(self) -> int:
        return len(self.token_to_id)

    def save_vocabulary(self, save_directory: str, filename_prefix: str = None) -> List[str]:
        pass

# from transformers import PreTrainedTokenizer
# from typing import List, Dict
# import re

# class ProteinTokenizer(PreTrainedTokenizer):
#     def __init__(self):
#         self.amino_acids = "ACDEFGHIKLMNPQRSTVWY"
#         self.special_tokens = {"pad_token": "[PAD]", "mask_token": "[MASK]", "unk_token": "[UNK]"}
#         self.unk_token = self.special_tokens["unk_token"]
#         self.all_tokens = list(self.amino_acids) + list(self.special_tokens.values())
#         self.token_to_id = {token: i for i, token in enumerate(self.all_tokens)}
#         self.id_to_token = {i: token for token, i in self.token_to_id.items()}

#         super().__init__()

#     def _tokenize(self, sequence: str) -> List[str]:
#         # Regular expression to match special tokens
#         token_pattern = re.compile(r'\[PAD\]|\[MASK\]|\[UNK\]')
        
#         # Split the sequence based on the special tokens, while keeping them in the result
#         tokens = []
#         pos = 0
#         for match in token_pattern.finditer(sequence):
#             # Add the sequence before the special token
#             if match.start() > pos:
#                 tokens.extend(list(sequence[pos:match.start()].upper()))
#             # Add the special token itself
#             tokens.append(match.group())
#             pos = match.end()
        
#         # Add any remaining part of the sequence after the last special token
#         if pos < len(sequence):
#             tokens.extend(list(sequence[pos:].upper()))
        
#         return tokens

#     def _convert_token_to_id(self, token: str) -> int:
#         return self.token_to_id.get(token, self.token_to_id.get(self.unk_token))

#     def _convert_id_to_token(self, index: int) -> str:
#         return self.id_to_token.get(index, self.unk_token)

#     def convert_tokens_to_string(self, tokens: List[str]) -> str:
#         return "".join(tokens)

#     def get_vocab(self) -> Dict[str, int]:
#         return self.token_to_id

#     @property
#     def vocab_size(self) -> int:
#         return len(self.token_to_id)

#     def save_vocabulary(self, save_directory: str, filename_prefix: str = None) -> List[str]:
#         pass
