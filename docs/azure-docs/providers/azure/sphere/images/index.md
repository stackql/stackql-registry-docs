---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - sphere
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sphere.images</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, imageName, resourceGroupName, subscriptionId` | Get a Image |
| `list_by_catalog` | `SELECT` | `catalogName, resourceGroupName, subscriptionId` | List Image resources by Catalog |
| `create_or_update` | `INSERT` | `catalogName, imageName, resourceGroupName, subscriptionId` | Create a Image |
| `delete` | `DELETE` | `catalogName, imageName, resourceGroupName, subscriptionId` | Delete a Image |
| `_list_by_catalog` | `EXEC` | `catalogName, resourceGroupName, subscriptionId` | List Image resources by Catalog |
