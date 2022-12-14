---
title: available_service_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - available_service_tiers
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>available_service_tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.available_service_tiers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enabled` | `boolean` | True if the Service Tier is enabled for the workspace. |
| `lastSkuUpdate` | `string` | Time when the sku was last updated for the workspace. Returned for the Capacity Reservation Service Tier. |
| `maximumRetention` | `integer` | The maximum retention for the Service Tier, in days. |
| `minimumRetention` | `integer` | The minimum retention for the Service Tier, in days. |
| `serviceTier` | `string` | The name of the Service Tier. |
| `capacityReservationLevel` | `integer` | The capacity reservation level in GB per day. Returned for the Capacity Reservation Service Tier. |
| `defaultRetention` | `integer` | The default retention for the Service Tier, in days. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AvailableServiceTiers_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
