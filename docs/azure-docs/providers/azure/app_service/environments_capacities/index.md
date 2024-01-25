---
title: environments_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_capacities
  - app_service
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
<tr><td><b>Name</b></td><td><code>environments_capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.environments_capacities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the stamp. |
| `availableCapacity` | `integer` | Available capacity (# of machines, bytes of storage etc...). |
| `computeMode` | `string` | Shared/dedicated workers. |
| `excludeFromCapacityAllocation` | `boolean` | If &lt;code&gt;true&lt;/code&gt;, it includes basic apps.<br />Basic apps are not used for capacity allocation. |
| `isApplicableForAllComputeModes` | `boolean` | &lt;code&gt;true&lt;/code&gt; if capacity is applicable for all apps; otherwise, &lt;code&gt;false&lt;/code&gt;. |
| `isLinux` | `boolean` | Is this a linux stamp capacity |
| `siteMode` | `string` | Shared or Dedicated. |
| `totalCapacity` | `integer` | Total capacity (# of machines, bytes of storage etc...). |
| `unit` | `string` | Name of the unit. |
| `workerSize` | `string` | Size of the machines. |
| `workerSizeId` | `integer` | Size ID of machines: <br />0 - Small<br />1 - Medium<br />2 - Large |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId` |
