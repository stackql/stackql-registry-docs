---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets the details of the private endpoint connection of the environment in the given resource group. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Gets a list of all private endpoint connections in the given environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Updates a Private Endpoint connection of the environment in the given resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Disconnects the private endpoint connection and deletes it from the environment. |
| <CopyableCode code="_list_by_environment" /> | `EXEC` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Gets a list of all private endpoint connections in the given environment. |
