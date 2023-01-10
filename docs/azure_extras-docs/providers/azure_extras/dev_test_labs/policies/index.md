---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a Policy. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Policies_Get` | `SELECT` | `api-version, labName, name, policySetName, resourceGroupName, subscriptionId` | Get policy. |
| `Policies_List` | `SELECT` | `api-version, labName, policySetName, resourceGroupName, subscriptionId` | List policies in a given policy set. |
| `Policies_CreateOrUpdate` | `INSERT` | `api-version, labName, name, policySetName, resourceGroupName, subscriptionId, data__properties` | Create or replace an existing policy. |
| `Policies_Delete` | `DELETE` | `api-version, labName, name, policySetName, resourceGroupName, subscriptionId` | Delete policy. |
| `Policies_Update` | `EXEC` | `api-version, labName, name, policySetName, resourceGroupName, subscriptionId` | Allows modifying tags of policies. All other properties will be ignored. |
