---
title: admin_rule_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_rule_collections
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
<tr><td><b>Name</b></td><td><code>admin_rule_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.admin_rule_collections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Defines the admin rule collection properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AdminRuleCollections_Get` | `SELECT` |  | Gets a network manager security admin configuration rule collection. |
| `AdminRuleCollections_List` | `SELECT` | `configurationName, networkManagerName, resourceGroupName, subscriptionId` | Lists all the rule collections in a security admin configuration, in a paginated format. |
| `AdminRuleCollections_CreateOrUpdate` | `INSERT` |  | Creates or updates an admin rule collection. |
| `AdminRuleCollections_Delete` | `DELETE` |  | Deletes an admin rule collection. |
