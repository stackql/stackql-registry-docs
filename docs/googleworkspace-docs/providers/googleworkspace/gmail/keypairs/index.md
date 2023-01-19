---
title: keypairs
hide_title: false
hide_table_of_contents: false
keywords:
  - keypairs
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
<tr><td><b>Name</b></td><td><code>keypairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.keypairs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `disableTime` | `string` | Output only. If a key pair is set to `DISABLED`, the time that the key pair's state changed from `ENABLED` to `DISABLED`. This field is present only when the key pair is in state `DISABLED`. |
| `enablementState` | `string` | Output only. The current state of the key pair. |
| `keyPairId` | `string` | Output only. The immutable ID for the client-side encryption S/MIME key pair. |
| `pem` | `string` | Output only. The public key and its certificate chain, in [PEM](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) format. |
| `pkcs7` | `string` | Input only. The public key and its certificate chain. The chain must be in [PKCS#7](https://en.wikipedia.org/wiki/PKCS_7) format and use PEM encoding and ASCII armor. |
| `privateKeyMetadata` | `array` | Metadata for instances of this key pair's private key. |
| `subjectEmailAddresses` | `array` | Output only. The email address identities that are specified on the leaf certificate. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_settings_cse_keypairs_get` | `SELECT` | `keyPairId, userId` | Retrieves an existing client-side encryption key pair. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_keypairs_list` | `SELECT` | `userId` | Lists client-side encryption key pairs for an authenticated user. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_keypairs_create` | `INSERT` | `userId` | Creates and uploads a client-side encryption S/MIME public key certificate chain and private key metadata for the authenticated user. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_keypairs_disable` | `EXEC` | `keyPairId, userId` | Turns off a client-side encryption key pair. The authenticated user can no longer use the key pair to decrypt incoming CSE message texts or sign outgoing CSE mail. To regain access, use the EnableCseKeyPair to turn on the key pair. After 30 days, you can permanently delete the key pair by using the ObliterateCseKeyPair method. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_keypairs_enable` | `EXEC` | `keyPairId, userId` | Turns on a client-side encryption key pair that was turned off. The key pair becomes active again for any associated client-side encryption identities. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_keypairs_obliterate` | `EXEC` | `keyPairId, userId` | Deletes a client-side encryption key pair permanently and immediately. You can only permanently delete key pairs that have been turned off for more than 30 days. To turn off a key pair, use the DisableCseKeyPair method. Gmail can't restore or decrypt any messages that were encrypted by an obliterated key. Authenticated users and Google Workspace administrators lose access to reading the encrypted messages. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
