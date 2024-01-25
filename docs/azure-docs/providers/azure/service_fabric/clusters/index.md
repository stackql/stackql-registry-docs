---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - service_fabric
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `etag` | `string` | Azure resource etag. |
| `location` | `string` | Azure resource location. |
| `properties` | `object` | Describes the cluster resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric cluster resource created or in the process of being created in the specified resource group. |
| `list` | `SELECT` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `create_or_update` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric cluster resource with the specified name. |
| `delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric cluster resource with the specified name. |
| `_list` | `EXEC` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Update the configuration of a Service Fabric cluster resource with the specified name. |
