---
title: region_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - region_healths
  - infrastructure_insights
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
<tr><td><b>Name</b></td><td><code>region_healths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.infrastructure_insights.region_healths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Contains information related to the health of a region. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The Azure Region where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegionHealths_Get` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns the requested health status of a region. |
| `RegionHealths_List` | `SELECT` | `resourceGroupName, subscriptionId` | Returns the list of all health status for the region. |
