---
title: session_host_managements
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_managements
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>session_host_managements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.session_host_managements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Session host Managements of HostPool. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hostPoolName, resourceGroupName, subscriptionId` | Get a SessionHostManagement. |
| `create_or_update` | `INSERT` | `hostPoolName, resourceGroupName, subscriptionId, data__properties` | Create or update a SessionHostManagement. |
| `update` | `EXEC` | `hostPoolName, resourceGroupName, subscriptionId` | Update a SessionHostManagement. |
