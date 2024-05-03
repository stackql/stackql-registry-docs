---
title: clienttokens
hide_title: false
hide_table_of_contents: false
keywords:
  - clienttokens
  - user
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
<tr><td><b>Name</b></td><td><code>clienttokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.clienttokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="clientId" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="createdBy" /> | `object` |
| <CopyableCode code="expiresAt" /> | `string` |
| <CopyableCode code="issuer" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="scopes" /> | `array` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="userId" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clientId, tokenId, userId, subdomain" /> | Gets a refresh token issued for the specified User and Client. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clientId, userId, subdomain" /> | Lists all refresh tokens issued for the specified User and Client. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clientId, tokenId, userId, subdomain" /> | Revokes the specified refresh token. |
| <CopyableCode code="deleteAll" /> | `EXEC` | <CopyableCode code="clientId, userId, subdomain" /> | Revokes all refresh tokens issued for the specified User and Client. |
