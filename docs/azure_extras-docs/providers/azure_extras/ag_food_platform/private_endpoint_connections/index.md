---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - ag_food_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Get Private endpoint connection object. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get list of Private endpoint connections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerForAgricultureResourceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Approves or Rejects a Private endpoint connection request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerForAgricultureResourceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Delete Private endpoint connection request. |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get list of Private endpoint connections. |
