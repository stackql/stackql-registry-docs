---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Project properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Projects_Get` | `SELECT` | `projectName, resourceGroupName, storageMoverName, subscriptionId` | Gets a Project resource. |
| `Projects_List` | `SELECT` | `resourceGroupName, storageMoverName, subscriptionId` | Lists all Projects in a Storage Mover. |
| `Projects_CreateOrUpdate` | `INSERT` | `projectName, resourceGroupName, storageMoverName, subscriptionId` | Creates or updates a Project resource, which is a logical grouping of related jobs. |
| `Projects_Delete` | `DELETE` | `projectName, resourceGroupName, storageMoverName, subscriptionId` | Deletes a Project resource. |
| `Projects_Update` | `EXEC` | `projectName, resourceGroupName, storageMoverName, subscriptionId` | Updates properties for a Project resource. Properties not specified in the request body will be unchanged. |
