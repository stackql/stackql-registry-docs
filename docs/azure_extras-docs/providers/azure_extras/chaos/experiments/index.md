---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - chaos
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.chaos.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The identity of a resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Model that represents the Experiment properties model. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, experimentName, resourceGroupName, subscriptionId` | Get a Experiment resource. |
| `list` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get a list of Experiment resources in a resource group. |
| `create_or_update` | `INSERT` | `api-version, experimentName, resourceGroupName, subscriptionId, data__properties` | Create or update a Experiment resource. |
| `delete` | `DELETE` | `api-version, experimentName, resourceGroupName, subscriptionId` | Delete a Experiment resource. |
| `_list` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Get a list of Experiment resources in a resource group. |
| `cancel` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | Cancel a running Experiment resource. |
| `start` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | Start a Experiment resource. |
| `update` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` | The operation to update an experiment. |
