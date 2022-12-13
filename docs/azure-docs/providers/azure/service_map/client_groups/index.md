---
title: client_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - client_groups
  - service_map
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
<tr><td><b>Name</b></td><td><code>client_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.client_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource ETAG. |
| `kind` | `string` | Additional resource type qualifier. |
| `properties` | `object` | Resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ClientGroups_Get` | `SELECT` | `clientGroupName, resourceGroupName, subscriptionId, workspaceName` | Retrieves the specified client group |
| `ClientGroups_GetMembersCount` | `EXEC` | `clientGroupName, resourceGroupName, subscriptionId, workspaceName` | Returns the approximate number of members in the client group. |
| `ClientGroups_ListMembers` | `EXEC` | `clientGroupName, resourceGroupName, subscriptionId, workspaceName` | Returns the members of the client group during the specified time interval. |
