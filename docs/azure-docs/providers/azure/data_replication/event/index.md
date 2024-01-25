---
title: event
hide_title: false
hide_table_of_contents: false
keywords:
  - event
  - data_replication
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
<tr><td><b>Name</b></td><td><code>event</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.event</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id of the resource. |
| `name` | `string` | Gets or sets the name of the resource. |
| `properties` | `object` | Event model properties. |
| `systemData` | `object` | System data required to be defined for Azure resources. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `eventName, resourceGroupName, subscriptionId, vaultName` | Gets the details of the event. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of events in the given vault. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of events in the given vault. |
