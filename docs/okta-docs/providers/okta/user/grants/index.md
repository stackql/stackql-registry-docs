---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.grants" /></td></tr>
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
| <CopyableCode code="issuer" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="scopeId" /> | `string` |
| <CopyableCode code="source" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="userId" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="grantId, userId, subdomain" /> | Gets a grant for the specified user |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="userId, subdomain" /> | Lists all grants for the specified user |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="grantId, userId, subdomain" /> | Revokes one grant for a specified user |
| <CopyableCode code="deleteAll" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Revokes all grants for a specified user |
