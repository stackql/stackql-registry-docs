---
title: service_runners
hide_title: false
hide_table_of_contents: false
keywords:
  - service_runners
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
<tr><td><b>Name</b></td><td><code>service_runners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.service_runners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `identity` | `object` | Properties of a managed identity |
| `location` | `string` | The location of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Get service runner. |
| `create_or_update` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Create or replace an existing service runner. |
| `delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId` | Delete service runner. |
