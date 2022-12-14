---
title: incident_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_comments
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
<tr><td><b>Name</b></td><td><code>incident_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.incident_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Incident comment property bag. |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IncidentComments_Get` | `SELECT` | `incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets an incident comment. |
| `IncidentComments_List` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all incident comments. |
| `IncidentComments_CreateOrUpdate` | `INSERT` | `incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName` | Creates or updates the incident comment. |
| `IncidentComments_Delete` | `DELETE` | `incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName` | Delete the incident comment. |
