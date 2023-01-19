---
title: smime_info
hide_title: false
hide_table_of_contents: false
keywords:
  - smime_info
  - gmail
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>smime_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.smime_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The immutable ID for the SmimeInfo. |
| `isDefault` | `boolean` | Whether this SmimeInfo is the default one for this user's send-as address. |
| `issuerCn` | `string` | The S/MIME certificate issuer's common name. |
| `pem` | `string` | PEM formatted X509 concatenated certificate string (standard base64 encoding). Format used for returning key, which includes public key as well as certificate chain (not private key). |
| `pkcs12` | `string` | PKCS#12 format containing a single private/public key pair and certificate chain. This format is only accepted from client for creating a new SmimeInfo and is never returned, because the private key is not intended to be exported. PKCS#12 may be encrypted, in which case encryptedKeyPassword should be set appropriately. |
| `encryptedKeyPassword` | `string` | Encrypted key password, when key is encrypted. |
| `expiration` | `string` | When the certificate expires (in milliseconds since epoch). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_settings_sendAs_smimeInfo_get` | `SELECT` | `id, sendAsEmail, userId` | Gets the specified S/MIME config for the specified send-as alias. |
| `users_settings_sendAs_smimeInfo_list` | `SELECT` | `sendAsEmail, userId` | Lists S/MIME configs for the specified send-as alias. |
| `users_settings_sendAs_smimeInfo_delete` | `DELETE` | `id, sendAsEmail, userId` | Deletes the specified S/MIME config for the specified send-as alias. |
| `users_settings_sendAs_smimeInfo_insert` | `EXEC` | `sendAsEmail, userId` | Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key. |
| `users_settings_sendAs_smimeInfo_setDefault` | `EXEC` | `id, sendAsEmail, userId` | Sets the default S/MIME config for the specified send-as alias. |
