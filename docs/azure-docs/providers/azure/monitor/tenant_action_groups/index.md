---
title: tenant_action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_action_groups
  - monitor
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
<tr><td><b>Name</b></td><td><code>tenant_action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.tenant_action_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource Id. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. Since Azure Activity Log Alerts is a global service, the location of the rules should always be 'global'. |
| `properties` | `object` | A tenant  action group. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managementGroupId, tenantActionGroupName, x-ms-client-tenant-id` | Get a tenant action group. |
| `list_by_management_group_id` | `SELECT` | `managementGroupId, x-ms-client-tenant-id` | Get a list of all tenant action groups in a management group. |
| `create_or_update` | `INSERT` | `managementGroupId, tenantActionGroupName, x-ms-client-tenant-id` | Create a new tenant action group or update an existing one. |
| `delete` | `DELETE` | `managementGroupId, tenantActionGroupName, x-ms-client-tenant-id` | Delete a tenant action group. |
| `_list_by_management_group_id` | `EXEC` | `managementGroupId, x-ms-client-tenant-id` | Get a list of all tenant action groups in a management group. |
| `update` | `EXEC` | `managementGroupId, tenantActionGroupName, x-ms-client-tenant-id` | Updates an existing tenant action group's tags. To update other fields use the CreateOrUpdate method. |
