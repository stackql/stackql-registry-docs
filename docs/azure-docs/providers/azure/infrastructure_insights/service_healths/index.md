---
title: service_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - service_healths
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
<tr><td><b>Name</b></td><td><code>service_healths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.infrastructure_insights.service_healths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | Holds information about the health of a service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceHealths_Get` | `SELECT` | `location, resourceGroupName, serviceHealth, subscriptionId` | Returns the requested service health object. |
| `ServiceHealths_List` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns the list of all resource provider health states. |
