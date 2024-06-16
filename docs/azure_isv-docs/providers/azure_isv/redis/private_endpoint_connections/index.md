---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - redis
  - azure_isv    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.private_endpoint_connections" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets the specified private endpoint connection associated with the redis cache. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | List all the private endpoint connections associated with the redis cache. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes the specified private endpoint connection associated with the redis cache. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="cacheName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Update the state of specified private endpoint connection associated with the redis cache. |
