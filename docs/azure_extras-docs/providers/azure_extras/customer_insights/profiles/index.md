---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The profile type definition. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Profiles_Get` | `SELECT` | `hubName, profileName, resourceGroupName, subscriptionId` | Gets information about the specified profile. |
| `Profiles_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all profile in the hub. |
| `Profiles_CreateOrUpdate` | `INSERT` | `hubName, profileName, resourceGroupName, subscriptionId` | Creates a profile within a Hub, or updates an existing profile. |
| `Profiles_Delete` | `DELETE` | `hubName, profileName, resourceGroupName, subscriptionId` | Deletes a profile within a hub |
| `Profiles_GetEnrichingKpis` | `EXEC` | `hubName, profileName, resourceGroupName, subscriptionId` | Gets the KPIs that enrich the profile Type identified by the supplied name. Enrichment happens through participants of the Interaction on an Interaction KPI and through Relationships for Profile KPIs. |
