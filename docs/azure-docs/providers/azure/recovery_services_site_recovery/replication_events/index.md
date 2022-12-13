---
title: replication_events
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_events
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | The properties of a monitoring event. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationEvents_Get` | `SELECT` | `api-version, eventName, resourceGroupName, resourceName, subscriptionId` | The operation to get the details of an Azure Site recovery event. |
| `ReplicationEvents_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of Azure Site Recovery events for the vault. |
