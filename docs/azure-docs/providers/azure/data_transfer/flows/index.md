---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
  - data_transfer
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
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.flows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of flow |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Gets flow resource. |
| <CopyableCode code="list_by_connection" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Gets flows in a connection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates the flow resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Deletes the flow resource. |
| <CopyableCode code="_list_by_connection" /> | `EXEC` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Gets flows in a connection. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Disables the specified flow |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Enables the specified flow. |
| <CopyableCode code="link" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId, data__id" /> | Links the specified flow. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Updates the flow resource. |
