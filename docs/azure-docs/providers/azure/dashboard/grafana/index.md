---
title: grafana
hide_title: false
hide_table_of_contents: false
keywords:
  - grafana
  - dashboard
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
<tr><td><b>Name</b></td><td><code>grafana</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dashboard.grafana</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the grafana resource |
| `name` | `string` | Name of the grafana resource. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the grafana resource lives |
| `properties` | `object` | Properties specific to the grafana resource. |
| `sku` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags for grafana resource. |
| `type` | `string` | The type of the grafana resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `list` | `SELECT` | `subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `create` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `check_enterprise_details` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `fetch_available_plugins` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
