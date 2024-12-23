import { map, max, sum } from "@/lib/arrays";
import { pipe } from "@/lib/utils.js";

const parse = input => input.split("\n").map(Number);

const prng = secret => {
  const secrets = [secret];
  let run = 2000;
  while (run--) {
    secret = ((secret << 6) ^ secret) & 0xffffff;
    secret = ((secret >> 5) ^ secret) & 0xffffff;
    secret = ((secret << 11) ^ secret) & 0xffffff;
    secrets.push(secret);
  }
  return secrets;
};

export const part1 = pipe(
  parse,
  map(prng),
  map(secrets => secrets.at(-1)),
  sum
);

const diff = prices =>
  [prices, prices.map((p, i) => p - prices[i - 1])].map(v =>
    v.slice(1)
  );

const seqPriceMap = data => {
  const sequenceKeys = new Set();
  return [
    sequenceKeys,
    data.map(
      ([prices, diffs]) =>
        new Map(
          diffs
            .map((_, i) => {
              const key = diffs
                .slice(i, i + 4)
                .reduce(
                  (acc, i) => acc * 100 + (i + 10),
                  0
                );
              sequenceKeys.add(key);
              return [key, prices[i + 3]];
            })
            .reverse()
        )
    ),
  ];
};

const sums = ([keys, maps]) =>
  [...keys].map(seq =>
    maps.reduce((sum, map) => sum + (map.get(seq) ?? 0), 0)
  );

export const part2 = pipe(
  parse,
  map(prng),
  map(secrets => secrets.map(v => v % 10)),
  map(diff),
  seqPriceMap,
  sums,
  max
);