---
title: clientgrants
hide_title: false
hide_table_of_contents: false
keywords:
  - clientgrants
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
<tr><td><b>Name</b></td><td><code>clientgrants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.clientgrants" /></td></tr>
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
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clientId, userId, subdomain" /> | Lists all grants for a specified user and client |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clientId, userId, subdomain" /> | Revokes all grants for the specified user and client |
