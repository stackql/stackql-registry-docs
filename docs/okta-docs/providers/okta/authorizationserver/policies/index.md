---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.authorizationserver.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="conditions" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="priority" /> | `integer` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="system" /> | `boolean` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authServerId, policyId, subdomain" /> | Success |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authServerId, subdomain" /> | Success |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="authServerId, subdomain" /> | Success |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authServerId, policyId, subdomain" /> | Success |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="authServerId, policyId, subdomain" /> | Activate Authorization Server Policy |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="authServerId, policyId, subdomain" /> | Deactivate Authorization Server Policy |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="authServerId, policyId, subdomain" /> | Success |
