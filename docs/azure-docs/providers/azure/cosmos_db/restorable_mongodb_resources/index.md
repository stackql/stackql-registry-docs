---
title: restorable_mongodb_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_mongodb_resources
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
<tr><td><b>Name</b></td><td><code>restorable_mongodb_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.restorable_mongodb_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `type` | `string` | The type of Azure resource. |
| `collectionNames` | `array` | The names of the collections available for restore. |
| `databaseName` | `string` | The name of the database available for restore. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `RestorableMongodbResources_List` | `SELECT` | `instanceId, location, subscriptionId` |
