---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sphere.products</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, productName, resourceGroupName, subscriptionId` | Get a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| `list_by_catalog` | `SELECT` | `catalogName, resourceGroupName, subscriptionId` | List Product resources by Catalog |
| `create_or_update` | `INSERT` | `catalogName, productName, resourceGroupName, subscriptionId` | Create a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| `delete` | `DELETE` | `catalogName, productName, resourceGroupName, subscriptionId` | Delete a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name' |
| `_list_by_catalog` | `EXEC` | `catalogName, resourceGroupName, subscriptionId` | List Product resources by Catalog |
| `count_devices` | `EXEC` | `catalogName, productName, resourceGroupName, subscriptionId` | Counts devices in product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| `generate_default_device_groups` | `EXEC` | `catalogName, productName, resourceGroupName, subscriptionId` | Generates default device groups for the product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| `update` | `EXEC` | `catalogName, productName, resourceGroupName, subscriptionId` | Update a Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
