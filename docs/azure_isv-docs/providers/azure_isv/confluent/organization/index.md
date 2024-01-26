---
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - confluent
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.confluent.organization</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM id of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | Location of Organization resource |
| `properties` | `object` | Organization resource property |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Organization resource tags |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `organizationName, resourceGroupName, subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `list_by_subscription` | `SELECT` | `subscriptionId` |
| `create` | `INSERT` | `organizationName, resourceGroupName, subscriptionId, data__properties` |
| `delete` | `DELETE` | `organizationName, resourceGroupName, subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |
| `update` | `EXEC` | `organizationName, resourceGroupName, subscriptionId` |
| `validate_organization` | `EXEC` | `organizationName, resourceGroupName, subscriptionId, data__properties` |
| `validate_organization_v2` | `EXEC` | `organizationName, resourceGroupName, subscriptionId, data__properties` |
