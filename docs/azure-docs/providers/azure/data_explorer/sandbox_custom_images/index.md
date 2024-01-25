---
title: sandbox_custom_images
hide_title: false
hide_table_of_contents: false
keywords:
  - sandbox_custom_images
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>sandbox_custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.sandbox_custom_images</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId` | Returns a sandbox custom image |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of the existing sandbox custom images of the given Kusto cluster. |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId` | Creates or updates a sandbox custom image. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId` | Deletes a sandbox custom image. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of the existing sandbox custom images of the given Kusto cluster. |
| `check_name_availability` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the sandbox custom image resource name is valid and is not already in use. |
| `update` | `EXEC` | `clusterName, resourceGroupName, sandboxCustomImageName, subscriptionId` | Updates a sandbox custom image. |
