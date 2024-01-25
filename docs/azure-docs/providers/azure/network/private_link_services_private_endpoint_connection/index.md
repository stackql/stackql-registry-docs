---
title: private_link_services_private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_private_endpoint_connection
  - network
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
<tr><td><b>Name</b></td><td><code>private_link_services_private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.private_link_services_private_endpoint_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `peConnectionName, resourceGroupName, serviceName, subscriptionId` | Get the specific private end point connection by specific private link service in the resource group. |
| `delete` | `DELETE` | `peConnectionName, resourceGroupName, serviceName, subscriptionId` | Delete private end point connection for a private link service in a subscription. |
| `update` | `EXEC` | `peConnectionName, resourceGroupName, serviceName, subscriptionId` | Approve or reject private end point connection for a private link service in a subscription. |
