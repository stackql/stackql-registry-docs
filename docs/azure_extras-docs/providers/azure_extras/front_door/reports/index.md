---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - front_door
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
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.front_door.reports</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Reports_GetLatencyScorecards` | `EXEC` | `aggregationInterval, experimentName, profileName, resourceGroupName, subscriptionId` |
| `Reports_GetTimeseries` | `EXEC` | `aggregationInterval, endDateTimeUTC, experimentName, profileName, resourceGroupName, startDateTimeUTC, subscriptionId, timeseriesType` |
