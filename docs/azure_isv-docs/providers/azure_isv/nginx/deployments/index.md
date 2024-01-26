---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - nginx
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.nginx.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `identity` | `object` |  |
| `location` | `string` |  |
| `properties` | `object` |  |
| `sku` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `deploymentName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `deploymentName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` |
