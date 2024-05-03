---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - dashboard
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
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dashboard.managed_private_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the managed private endpoint. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |
