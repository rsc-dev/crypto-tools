#!/usr/bin/env python

"""Discrete logarithm helper"""

__author__ = 'Radoslaw Matusiak'
__copyright__ = 'Copyright (c) 2019 Radoslaw Matusiak'
__license__ = 'MIT'

import numbthy
from tqdm import tqdm


def dlog(p, g, h, B=2**20):
    """
    Calculate discrete logarithm.

    :param p: Prime p.
    :param g: Any element in Z_star_p => h=g^x for 0 <= x <= B.
    :param h: Value h=g^x for 0 <= x <= B.
    :param B: x value space; 0 <= x <= B.
    :return: x: discrete log modulo p if found, None otherwise.
    """
    l_hash = dict()
    print('[+] Calculating l-value table...')
    for x1 in tqdm(range(B)):
        g_pow_x1 = numbthy.power_mod(g, x1, p)
        inv_g_pow_x1 = numbthy.invmod(g_pow_x1, p)
        l_val = h * inv_g_pow_x1
        l_val = l_val % p
        l_hash[l_val] = x1

    print('[+] Looking up r-value in l-value table...')
    x0, x1 = 0, 0
    g_pow_B = numbthy.power_mod(g, B, p)
    for x0 in tqdm(range(B)):
        r_val = numbthy.power_mod(g_pow_B, x0, p)

        try:
            x1 = l_hash[r_val]
            print('[+] Found!!')
            break
        except KeyError:
            pass
    
    if x0 != 0 and x1 != 0:
        x = x0 * B + x1
    else:
        x = None
    return x


def run():
    print('Discrete logarithm helper')

    try:
        p = input('Enter p value:')
        p = int(p)

        g = input('Enter g value:')
        g = int(g)

        h = input('Enter h value:')
        h = int(h)
    except ValueError:
        exit(-1)

    dlog(p, g, h)


if __name__ == '__main__':
    # run()
    p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
    h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

    x = dlog(p, g, h)
    print(x)
