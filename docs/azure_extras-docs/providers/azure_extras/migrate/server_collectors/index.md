---
title: server_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - server_collectors
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
<tr><td><b>Name</b></td><td><code>server_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.server_collectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `eTag` | `string` |
| `properties` | `object` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerCollectors_Get` | `SELECT` | `api-version, projectName, resourceGroupName, serverCollectorName, subscriptionId` | Get a Server collector. |
| `ServerCollectors_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get a list of Server collector. |
| `ServerCollectors_Create` | `INSERT` | `api-version, projectName, resourceGroupName, serverCollectorName, subscriptionId` | Create or Update Server collector |
| `ServerCollectors_Delete` | `DELETE` | `api-version, projectName, resourceGroupName, serverCollectorName, subscriptionId` | Delete a Server collector from the project. |
