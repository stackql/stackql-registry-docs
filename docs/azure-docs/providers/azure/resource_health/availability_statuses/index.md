---
title: availability_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_statuses
  - resource_health
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
<tr><td><b>Name</b></td><td><code>availability_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_health.availability_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure Resource Manager Identity for the availabilityStatuses resource. |
| `name` | `string` | current. |
| `location` | `string` | Azure Resource Manager geo location of the resource. |
| `properties` | `object` | Properties of availability state. |
| `type` | `string` | Microsoft.ResourceHealth/AvailabilityStatuses. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AvailabilityStatuses_List` | `SELECT` | `resourceUri` | Lists all historical availability transitions and impacting events for a single resource. |
| `AvailabilityStatuses_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the current availability status for all the resources in the resource group. |
| `AvailabilityStatuses_ListBySubscriptionId` | `SELECT` | `subscriptionId` | Lists the current availability status for all the resources in the subscription. |
| `AvailabilityStatuses_GetByResource` | `EXEC` | `resourceUri` | Gets current availability status for a single resource |
