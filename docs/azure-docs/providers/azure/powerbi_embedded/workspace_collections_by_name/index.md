---
title: workspace_collections_by_name
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_collections_by_name
  - powerbi_embedded
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
<tr><td><b>Name</b></td><td><code>workspace_collections_by_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_embedded.workspace_collections_by_name</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource id |
| `name` | `string` | Workspace collection name |
| `location` | `string` | Azure location |
| `properties` | `object` | Properties |
| `sku` | `object` |  |
| `tags` | `object` |  |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceCollectionName` |
