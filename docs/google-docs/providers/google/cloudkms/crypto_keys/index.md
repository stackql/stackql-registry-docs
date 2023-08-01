---
title: crypto_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_keys
  - cloudkms
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.crypto_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cryptoKeys` | `array` | The list of CryptoKeys. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCryptoKeysRequest.page_token to retrieve the next page of results. |
| `totalSize` | `integer` | The total number of CryptoKeys that matched the query. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns metadata for a given CryptoKey, as well as its primary CryptoKeyVersion. |
| `list` | `SELECT` | `keyRingsId, locationsId, projectsId` | Lists CryptoKeys. |
| `create` | `INSERT` | `keyRingsId, locationsId, projectsId` | Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required. |
| `decrypt` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Decrypts data that was protected by Encrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| `encrypt` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Encrypts data, so that it can only be recovered by a call to Decrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| `patch` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Update a CryptoKey. |
