---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - nginx
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.nginx.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `location` | `string` |  |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Configurations_Get` | `SELECT` | `configurationName, deploymentName, resourceGroupName, subscriptionId` |
| `Configurations_List` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` |
| `Configurations_CreateOrUpdate` | `INSERT` | `configurationName, deploymentName, resourceGroupName, subscriptionId` |
| `Configurations_Delete` | `DELETE` | `configurationName, deploymentName, resourceGroupName, subscriptionId` |
