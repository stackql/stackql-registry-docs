---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - elastic_san
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  Response for PrivateEndpoint connection properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticSanName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets the specified private endpoint connection associated with the Elastic San |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="elasticSanName, resourceGroupName, subscriptionId" /> | List all Private Endpoint Connections associated with the Elastic San. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="elasticSanName, privateEndpointConnectionName, resourceGroupName, subscriptionId, data__properties" /> | Update the state of specified private endpoint connection associated with the Elastic San |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticSanName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes the specified private endpoint connection associated with the Elastic San |
