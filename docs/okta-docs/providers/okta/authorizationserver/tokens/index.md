---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - authorizationserver
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.authorizationserver.tokens" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authServerId, clientId, tokenId, subdomain" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authServerId, clientId, subdomain" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authServerId, clientId, tokenId, subdomain" /> |
| <CopyableCode code="deleteall" /> | `EXEC` | <CopyableCode code="authServerId, clientId, subdomain" /> |
