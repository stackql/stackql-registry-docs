---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - search
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.search.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID of the quota usage SKU endpoint for Microsoft.Search provider. |
| `name` | `object` | The name of the SKU supported by Azure AI Search. |
| `currentValue` | `integer` | The currently used up value for the particular search SKU. |
| `limit` | `integer` | The quota limit for the particular search SKU. |
| `unit` | `string` | The unit of measurement for the search SKU. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_subscription` | `SELECT` | `location, subscriptionId` | Gets a list of all Search quota usages in the given subscription. |
| `_list_by_subscription` | `EXEC` | `location, subscriptionId` | Gets a list of all Search quota usages in the given subscription. |
| `usages` | `EXEC` | `location, skuName, subscriptionId` | Gets the quota usage for a search SKU in the given subscription. |
