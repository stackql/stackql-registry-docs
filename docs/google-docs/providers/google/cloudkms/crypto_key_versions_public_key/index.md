---
title: crypto_key_versions_public_key
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_key_versions_public_key
  - cloudkms
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_key_versions_public_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.crypto_key_versions_public_key</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the CryptoKeyVersion public key. Provided here for verification. NOTE: This field is in Beta. |
| `pem` | `string` | The public key, encoded in PEM format. For more information, see the [RFC 7468](https://tools.ietf.org/html/rfc7468) sections for [General Considerations](https://tools.ietf.org/html/rfc7468#section-2) and [Textual Encoding of Subject Public Key Info] (https://tools.ietf.org/html/rfc7468#section-13). |
| `pemCrc32c` | `string` | Integrity verification field. A CRC32C checksum of the returned PublicKey.pem. An integrity check of PublicKey.pem can be performed by computing the CRC32C checksum of PublicKey.pem and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type. NOTE: This field is in Beta. |
| `protectionLevel` | `string` | The ProtectionLevel of the CryptoKeyVersion public key. |
| `algorithm` | `string` | The Algorithm associated with this key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_getPublicKey` | `SELECT` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` |
