---
title: tenant_access
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access
  - api_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_access" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Get tenant access information details without secrets. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Returns list of access infos - for Git and Management endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="If-Match, accessName, resourceGroupName, serviceName, subscriptionId" /> | Update tenant access information details. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Returns list of access infos - for Git and Management endpoints. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate primary access key |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate secondary access key |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, accessName, resourceGroupName, serviceName, subscriptionId" /> | Update tenant access information details. |
