---
title: ssh_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_public_keys
  - oslogin
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
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.oslogin.ssh_public_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The canonical resource name. |
| `fingerprint` | `string` | Output only. The SHA-256 fingerprint of the SSH public key. |
| `key` | `string` | Public key text in SSH format, defined by RFC4253 section 6.6. |
| `expirationTimeUsec` | `string` | An expiration time in microseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_sshPublicKeys_get` | `SELECT` | `sshPublicKeysId, usersId` | Retrieves an SSH public key. |
| `users_sshPublicKeys_create` | `INSERT` | `usersId` | Create an SSH public key |
| `users_sshPublicKeys_delete` | `DELETE` | `sshPublicKeysId, usersId` | Deletes an SSH public key. |
| `users_sshPublicKeys_patch` | `EXEC` | `sshPublicKeysId, usersId` | Updates an SSH public key and returns the profile information. This method supports patch semantics. |
