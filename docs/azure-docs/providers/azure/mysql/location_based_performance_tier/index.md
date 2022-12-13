---
title: location_based_performance_tier
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_performance_tier
  - mysql
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
<tr><td><b>Name</b></td><td><code>location_based_performance_tier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.location_based_performance_tier</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the performance tier. |
| `minLargeStorageMB` | `integer` | Max storage allowed for a server. |
| `minStorageMB` | `integer` | Max storage allowed for a server. |
| `serviceLevelObjectives` | `array` | Service level objectives associated with the performance tier |
| `maxBackupRetentionDays` | `integer` | Maximum Backup retention in days for the performance tier edition |
| `maxLargeStorageMB` | `integer` | Max storage allowed for a server. |
| `maxStorageMB` | `integer` | Max storage allowed for a server. |
| `minBackupRetentionDays` | `integer` | Minimum Backup retention in days for the performance tier edition |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LocationBasedPerformanceTier_List` | `SELECT` | `locationName, subscriptionId` |
