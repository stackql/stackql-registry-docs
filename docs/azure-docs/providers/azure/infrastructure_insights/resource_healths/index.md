---
title: resource_healths
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_healths
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
<tr><td><b>Name</b></td><td><code>resource_healths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.infrastructure_insights.resource_healths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | Health information related to a resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourceHealths_Get` | `SELECT` | `location, resourceGroupName, resourceRegistrationId, serviceRegistrationId, subscriptionId` | Returns the requested health information about a resource. |
| `ResourceHealths_List` | `SELECT` | `location, resourceGroupName, serviceRegistrationId, subscriptionId` | Returns a list of each resource's health under a service. |
