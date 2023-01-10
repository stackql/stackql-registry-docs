---
title: products_and_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - products_and_configurations
  - edge_order
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>products_and_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_order.products_and_configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductsAndConfigurations_ListConfigurations` | `EXEC` | `subscriptionId` | List configurations for the given product family, product line and product for the given subscription. |
| `ProductsAndConfigurations_ListProductFamilies` | `EXEC` | `subscriptionId, data__filterableProperties` | List product families for the given subscription. |
| `ProductsAndConfigurations_ListProductFamiliesMetadata` | `EXEC` | `subscriptionId` | List product families metadata for the given subscription. |
