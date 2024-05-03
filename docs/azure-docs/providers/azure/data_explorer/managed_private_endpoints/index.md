---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - data_explorer
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.managed_private_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing the properties of a managed private endpoint object. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Gets a managed private endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of managed private endpoints. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Creates a managed private endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Deletes a managed private endpoint. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of managed private endpoints. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the managed private endpoints resource name is valid and is not already in use. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Updates a managed private endpoint. |
