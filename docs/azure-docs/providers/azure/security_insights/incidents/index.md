---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
  - security_insights
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes incident properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Incidents_Get` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets an incident. |
| `Incidents_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all incidents. |
| `Incidents_CreateOrUpdate` | `INSERT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the incident. |
| `Incidents_Delete` | `DELETE` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Delete the incident. |
| `Incidents_CreateTeam` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName, data__teamName` | Creates a Microsoft team to investigate the incident by sharing information and insights between participants. |
| `Incidents_ListAlerts` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident alerts. |
| `Incidents_ListBookmarks` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident bookmarks. |
| `Incidents_ListEntities` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident related entities. |
| `Incidents_RunPlaybook` | `EXEC` | `incidentIdentifier, resourceGroupName, subscriptionId, workspaceName, data__logicAppsResourceId` | Triggers playbook on a specific incident |
