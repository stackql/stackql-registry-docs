---
title: cloud_service_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_roles
  - compute
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
<tr><td><b>Name</b></td><td><code>cloud_service_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_service_roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | The cloud service role properties. |
| `sku` | `object` | Describes the cloud service role sku. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudServiceRoles_Get` | `SELECT` | `cloudServiceName, resourceGroupName, roleName, subscriptionId` | Gets a role from a cloud service. |
| `CloudServiceRoles_List` | `SELECT` | `cloudServiceName, resourceGroupName, subscriptionId` | Gets a list of all roles in a cloud service. Use nextLink property in the response to get the next page of roles. Do this till nextLink is null to fetch all the roles. |
