---
title: restorable_gremlin_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_gremlin_resources
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
<tr><td><b>Name</b></td><td><code>restorable_gremlin_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.restorable_gremlin_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `databaseName` | `string` | The name of the gremlin database available for restore. |
| `graphNames` | `array` | The names of the graphs available for restore. |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RestorableGremlinResources_List` | `SELECT` | `instanceId, location, subscriptionId` |
