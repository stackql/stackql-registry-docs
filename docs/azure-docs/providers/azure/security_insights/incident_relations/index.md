---
title: incident_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_relations
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
<tr><td><b>Name</b></td><td><code>incident_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.incident_relations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Relation property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IncidentRelations_Get` | `SELECT` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Gets an incident relation. |
| `IncidentRelations_List` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident relations. |
| `IncidentRelations_CreateOrUpdate` | `INSERT` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the incident relation. |
| `IncidentRelations_Delete` | `DELETE` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Delete the incident relation. |
