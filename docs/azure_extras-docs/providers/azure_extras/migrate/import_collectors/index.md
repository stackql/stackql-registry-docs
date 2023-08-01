---
title: import_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - import_collectors
  - migrate
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
<tr><td><b>Name</b></td><td><code>import_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.import_collectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `properties` | `object` |
| `type` | `string` |
| `eTag` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ImportCollectors_Get` | `SELECT` | `api-version, importCollectorName, projectName, resourceGroupName, subscriptionId` | Get a Import collector. |
| `ImportCollectors_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get a list of Import collector. |
| `ImportCollectors_Create` | `INSERT` | `api-version, importCollectorName, projectName, resourceGroupName, subscriptionId` | Create or Update Import collector |
| `ImportCollectors_Delete` | `DELETE` | `api-version, importCollectorName, projectName, resourceGroupName, subscriptionId` | Delete a Import collector from the project. |
