---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.labs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a lab. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, name, resourceGroupName, subscriptionId` | Get lab. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List labs in a resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List labs in a subscription. |
| `create_or_update` | `INSERT` | `api-version, name, resourceGroupName, subscriptionId` | Create or replace an existing lab. This operation can take a while to complete. |
| `delete` | `DELETE` | `api-version, name, resourceGroupName, subscriptionId` | Delete lab. This operation can take a while to complete. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List labs in a resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List labs in a subscription. |
| `claim_any_vm` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Claim a random claimable virtual machine in the lab. This operation can take a while to complete. |
| `export_resource_usage` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Exports the lab resource usage into a storage account This operation can take a while to complete. |
| `generate_upload_uri` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Generate a URI for uploading custom disk images to a Lab. |
| `import_virtual_machine` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Import a virtual machine into a different lab. This operation can take a while to complete. |
| `update` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Allows modifying tags of labs. All other properties will be ignored. |
