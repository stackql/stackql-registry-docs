---
title: hyperv_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperv_collectors
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
<tr><td><b>Name</b></td><td><code>hyperv_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.hyperv_collectors</code></td></tr>
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
| `HyperVCollectors_Get` | `SELECT` | `api-version, hyperVCollectorName, projectName, resourceGroupName, subscriptionId` | Get a Hyper-V collector. |
| `HyperVCollectors_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get a list of Hyper-V collector. |
| `HyperVCollectors_Create` | `INSERT` | `api-version, hyperVCollectorName, projectName, resourceGroupName, subscriptionId` | Create or Update Hyper-V collector |
| `HyperVCollectors_Delete` | `DELETE` | `api-version, hyperVCollectorName, projectName, resourceGroupName, subscriptionId` | Delete a Hyper-V collector from the project. |
