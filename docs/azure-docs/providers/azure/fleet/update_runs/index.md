---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
  - fleet
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
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.fleet.update_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| `properties` | `object` | The properties of the UpdateRun. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fleetName, resourceGroupName, subscriptionId, updateRunName` | Get a UpdateRun |
| `list_by_fleet` | `SELECT` | `fleetName, resourceGroupName, subscriptionId` | List UpdateRun resources by Fleet |
| `create_or_update` | `INSERT` | `fleetName, resourceGroupName, subscriptionId, updateRunName` | Create a UpdateRun |
| `delete` | `DELETE` | `fleetName, resourceGroupName, subscriptionId, updateRunName` | Delete a UpdateRun |
| `_list_by_fleet` | `EXEC` | `fleetName, resourceGroupName, subscriptionId` | List UpdateRun resources by Fleet |
| `start` | `EXEC` | `fleetName, resourceGroupName, subscriptionId, updateRunName` | Starts an UpdateRun. |
| `stop` | `EXEC` | `fleetName, resourceGroupName, subscriptionId, updateRunName` | Stops an UpdateRun. |
