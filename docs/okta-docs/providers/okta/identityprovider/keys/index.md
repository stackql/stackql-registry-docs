---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - identityprovider
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.identityprovider.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="alg" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="e" /> | `string` |
| <CopyableCode code="expiresAt" /> | `string` |
| <CopyableCode code="false" /> | `string` |
| <CopyableCode code="key_ops" /> | `array` |
| <CopyableCode code="kid" /> | `string` |
| <CopyableCode code="kty" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="use" /> | `string` |
| <CopyableCode code="x5c" /> | `array` |
| <CopyableCode code="x5t" /> | `string` |
| <CopyableCode code="x5t#S256" /> | `string` |
| <CopyableCode code="x5u" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyId, subdomain" /> | Gets a specific IdP Key Credential by `kid` |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates IdP key credentials. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Adds a new X.509 certificate credential to the IdP key store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyId, subdomain" /> | Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP. |
