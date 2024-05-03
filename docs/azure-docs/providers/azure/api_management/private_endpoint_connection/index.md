---
title: private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.private_endpoint_connection" /></td></tr>
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
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all private endpoint connections of the API Management service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Private Endpoint Connection or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Private Endpoint Connection. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all private endpoint connections of the API Management service instance. |
| <CopyableCode code="get_by_name" /> | `EXEC` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Private Endpoint Connection specified by its identifier. |
