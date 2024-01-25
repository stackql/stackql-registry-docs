---
title: data_products_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products_catalogs
  - network_analytics
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
<tr><td><b>Name</b></td><td><code>data_products_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_analytics.data_products_catalogs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List data catalog by resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List data catalog by subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List data catalog by resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List data catalog by subscription. |
