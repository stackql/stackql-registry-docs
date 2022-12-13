---
title: tenant_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configurations
  - portal
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
<tr><td><b>Name</b></td><td><code>tenant_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.portal.tenant_configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TenantConfigurations_Get` | `SELECT` | `configurationName` | Gets the tenant configuration. |
| `TenantConfigurations_List` | `SELECT` |  | Gets list of the tenant configurations. |
| `TenantConfigurations_Create` | `INSERT` | `configurationName` | Create the tenant configuration. If configuration already exists - update it. User has to be a Tenant Admin for this operation. |
| `TenantConfigurations_Delete` | `DELETE` | `configurationName` | Delete the tenant configuration. User has to be a Tenant Admin for this operation. |
