---
title: dscp_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - dscp_configuration
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
<tr><td><b>Name</b></td><td><code>dscp_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.dscp_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Differentiated Services Code Point configuration properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DscpConfiguration_Get` | `SELECT` | `dscpConfigurationName, resourceGroupName, subscriptionId` | Gets a DSCP Configuration. |
| `DscpConfiguration_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a DSCP Configuration. |
| `DscpConfiguration_ListAll` | `SELECT` | `subscriptionId` | Gets all dscp configurations in a subscription. |
| `DscpConfiguration_CreateOrUpdate` | `INSERT` | `dscpConfigurationName, resourceGroupName, subscriptionId` | Creates or updates a DSCP Configuration. |
| `DscpConfiguration_Delete` | `DELETE` | `dscpConfigurationName, resourceGroupName, subscriptionId` | Deletes a DSCP Configuration. |
