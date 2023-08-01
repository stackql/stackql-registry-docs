---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - migrate
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this group. /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125;/groups/&#123;groupName&#125; |
| `name` | `string` | Name of the group. |
| `eTag` | `string` | For optimistic concurrency control. |
| `properties` | `object` | Properties of group resource. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects/groups]. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Groups_Get` | `SELECT` | `api-version, groupName, projectName, resourceGroupName, subscriptionId` | Get information related to a specific group in the project. Returns a json object of type 'group' as specified in the models section. |
| `Groups_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get all groups created in the project. Returns a json array of objects of type 'group' as specified in the Models section. |
| `Groups_Create` | `INSERT` | `api-version, groupName, projectName, resourceGroupName, subscriptionId, data__properties` | Create a new group by sending a json object of type 'group' as given in Models section as part of the Request Body. The group name in a project is unique.<br /><br />This operation is Idempotent.<br /> |
| `Groups_Delete` | `DELETE` | `api-version, groupName, projectName, resourceGroupName, subscriptionId` | Delete the group from the project. The machines remain in the project. Deleting a non-existent group results in a no-operation.<br /><br />A group is an aggregation mechanism for machines in a project. Therefore, deleting group does not delete machines in it.<br /> |
| `Groups_UpdateMachines` | `EXEC` | `api-version, groupName, projectName, resourceGroupName, subscriptionId` | Update machines in group by adding or removing machines. |
