"""
A trivial compression example extracted from the book 'Classic
Computer Science Problems in Python'.

For manual testing:
python compressed_gene.py
"""


class CompressedGene:
    """Compressed gene saves the information of a received gene as a string compressed as a bit string."""

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """Convert the provided str of nucleotides into a bit string."""
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            # shift left two bits
            self.bit_string <<= 2

            if nucleotide == 'A':
                # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError(f'invalid nucleotide: {nucleotide}')

    def decompress(self) -> str:
        """Convert a bit string into an unicode str."""
        gene: str = ''

        # -1 to exclude sentinel
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # get just 2 relevant bits
            bits: int = self.bit_string >> i & 0b11

            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError(f'invalid bits: {bits}')

        # [::-1] reverses string by slicing backwards
        return gene[::-1]

    def __str__(self) -> str:
        """String representation for pretty printing."""
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof

    original: str = 'TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA' * 100
    print(f'original is {getsizeof(original)} bytes')

    compressed: CompressedGene = CompressedGene(original)
    print(f'compressed is {getsizeof(compressed.bit_string)} bytes')

    print(
        f'original and decompressed are the same: {original == compressed.decompress()}')
