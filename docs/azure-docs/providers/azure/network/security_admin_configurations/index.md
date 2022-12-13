---
title: security_admin_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - security_admin_configurations
  - network
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
<tr><td><b>Name</b></td><td><code>security_admin_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_admin_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Defines the security admin configuration properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityAdminConfigurations_Get` | `SELECT` |  | Retrieves a network manager security admin configuration. |
| `SecurityAdminConfigurations_List` | `SELECT` | `networkManagerName, resourceGroupName, subscriptionId` | Lists all the network manager security admin configurations in a network manager, in a paginated format. |
| `SecurityAdminConfigurations_CreateOrUpdate` | `INSERT` |  | Creates or updates a network manager security admin configuration. |
| `SecurityAdminConfigurations_Delete` | `DELETE` |  | Deletes a network manager security admin configuration. |
