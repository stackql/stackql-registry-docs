---
title: move_collections_move_collections_by_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections_move_collections_by_subscription
  - resource_mover
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
<tr><td><b>Name</b></td><td><code>move_collections_move_collections_by_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_mover.move_collections_move_collections_by_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource Id for the resource. |
| `name` | `string` | The name of the resource |
| `etag` | `string` | The etag of the resource. |
| `identity` | `object` | Defines the MSI properties of the Move Collection. |
| `location` | `string` | The geo-location where the resource lives. |
| `properties` | `object` | Defines the move collection properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, subscriptionId` |
| `_list` | `EXEC` | `api-version, subscriptionId` |
