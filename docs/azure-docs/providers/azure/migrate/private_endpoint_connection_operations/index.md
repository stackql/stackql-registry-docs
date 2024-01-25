---
title: private_endpoint_connection_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_operations
  - migrate
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate.private_endpoint_connection_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the private endpoint connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId` | Get a PrivateEndpointConnection |
| `list_by_assessment_project` | `SELECT` | `projectName, resourceGroupName, subscriptionId` | List PrivateEndpointConnection resources by AssessmentProject |
| `delete` | `DELETE` | `privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId` | Delete a PrivateEndpointConnection |
| `_list_by_assessment_project` | `EXEC` | `projectName, resourceGroupName, subscriptionId` | List PrivateEndpointConnection resources by AssessmentProject |
| `update` | `EXEC` | `privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId` | Create a PrivateEndpointConnection |
