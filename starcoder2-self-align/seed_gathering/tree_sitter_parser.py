# tree_sitter_parser.py

from tree_sitter_language_pack import get_parser, get_language

# Get the Language and Parser for Python:
LANGUAGE = get_language("python")   # tree_sitter.Language instance
_PARSER  = get_parser("python")     # tree_sitter.Parser instance

def make_parser():
    """
    Returns a Tree-Sitter Parser configured for Python.
    """
    return _PARSER

def node_to_string(node, source_bytes: bytes) -> str:
    """
    Given a Tree-Sitter AST node and the raw source bytes,
    return the substring corresponding to that node.
    """
    return source_bytes[node.start_byte:node.end_byte].decode("utf8", errors="replace")
