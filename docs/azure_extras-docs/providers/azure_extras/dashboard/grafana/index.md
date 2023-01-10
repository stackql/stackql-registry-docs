---
title: grafana
hide_title: false
hide_table_of_contents: false
keywords:
  - grafana
  - dashboard
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
<tr><td><b>Name</b></td><td><code>grafana</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dashboard.grafana</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the grafana resource |
| `name` | `string` | Name of the grafana resource. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `properties` | `object` | Properties specific to the grafana resource. |
| `tags` | `object` | The tags for grafana resource. |
| `location` | `string` | The geo-location where the grafana resource lives |
| `sku` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the grafana resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Grafana_Get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `Grafana_List` | `SELECT` | `subscriptionId` |
| `Grafana_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Grafana_Create` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` |
| `Grafana_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` |
| `Grafana_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
