---
title: restorable_gremlin_graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_gremlin_graphs
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>restorable_gremlin_graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.restorable_gremlin_graphs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource Identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `properties` | `object` | The properties of an Azure Cosmos DB Gremlin graph event |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `instanceId, location, subscriptionId` |
| `_list` | `EXEC` | `instanceId, location, subscriptionId` |
