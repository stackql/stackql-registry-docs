---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - app_configuration
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a private endpoint connection. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets the specified private endpoint connection associated with the configuration store. |
| <CopyableCode code="list_by_configuration_store" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Lists all private endpoint connections for a configuration store. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Update the state of the specified private endpoint connection associated with the configuration store. This operation cannot be used to create a private endpoint connection. Private endpoint connections must be created with the Network resource provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes a private endpoint connection. |
| <CopyableCode code="_list_by_configuration_store" /> | `EXEC` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Lists all private endpoint connections for a configuration store. |
