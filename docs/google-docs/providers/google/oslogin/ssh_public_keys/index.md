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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oslogin.ssh_public_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The canonical resource name. |
| <CopyableCode code="expirationTimeUsec" /> | `string` | An expiration time in microseconds since epoch. |
| <CopyableCode code="fingerprint" /> | `string` | Output only. The SHA-256 fingerprint of the SSH public key. |
| <CopyableCode code="key" /> | `string` | Public key text in SSH format, defined by RFC4253 section 6.6. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="sshPublicKeysId, usersId" /> | Retrieves an SSH public key. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="usersId" /> | Create an SSH public key |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="sshPublicKeysId, usersId" /> | Deletes an SSH public key. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="sshPublicKeysId, usersId" /> | Updates an SSH public key and returns the profile information. This method supports patch semantics. |
