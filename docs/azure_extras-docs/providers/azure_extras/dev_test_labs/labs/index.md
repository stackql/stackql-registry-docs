---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.labs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a lab. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Labs_Get` | `SELECT` | `api-version, name, resourceGroupName, subscriptionId` | Get lab. |
| `Labs_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List labs in a resource group. |
| `Labs_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List labs in a subscription. |
| `Labs_CreateOrUpdate` | `INSERT` | `api-version, name, resourceGroupName, subscriptionId` | Create or replace an existing lab. This operation can take a while to complete. |
| `Labs_Delete` | `DELETE` | `api-version, name, resourceGroupName, subscriptionId` | Delete lab. This operation can take a while to complete. |
| `Labs_ClaimAnyVm` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Claim a random claimable virtual machine in the lab. This operation can take a while to complete. |
| `Labs_CreateEnvironment` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Create virtual machines in a lab. This operation can take a while to complete. |
| `Labs_ExportResourceUsage` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Exports the lab resource usage into a storage account This operation can take a while to complete. |
| `Labs_GenerateUploadUri` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Generate a URI for uploading custom disk images to a Lab. |
| `Labs_ImportVirtualMachine` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Import a virtual machine into a different lab. This operation can take a while to complete. |
| `Labs_ListVhds` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | List disk images available for custom image creation. |
| `Labs_Update` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Allows modifying tags of labs. All other properties will be ignored. |
