---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - powerbi_privatelinks
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_privatelinks.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the id of the resource. |
| `name` | `string` | Specifies the name of the resource. |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureResourceName, privateEndpointName, resourceGroupName, subscriptionId` | Get a specific private endpoint connection for Power BI by private endpoint name. |
| `list_by_resource` | `SELECT` | `azureResourceName, resourceGroupName, subscriptionId` | Gets private endpoint connection for Power BI. |
| `create` | `INSERT` | `azureResourceName, privateEndpointName, resourceGroupName, subscriptionId` | Updates the status of Private Endpoint Connection object. Used to approve or reject a connection. |
| `delete` | `DELETE` | `azureResourceName, privateEndpointName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection for Power BI by private endpoint name. |
| `_list_by_resource` | `EXEC` | `azureResourceName, resourceGroupName, subscriptionId` | Gets private endpoint connection for Power BI. |
