---
title: catalog_dev_box_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog_dev_box_definitions
  - dev_center
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
<tr><td><b>Name</b></td><td><code>catalog_dev_box_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.catalog_dev_box_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a Dev Box definition. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets a Dev Box definition from the catalog |
| `list_by_catalog` | `SELECT` |  | List Dev Box definitions in the catalog. |
| `_list_by_catalog` | `EXEC` |  | List Dev Box definitions in the catalog. |
