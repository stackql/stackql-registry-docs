---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - nginx
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.nginx.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `location` | `string` |  |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `certificateName, deploymentName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `certificateName, deploymentName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `certificateName, deploymentName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` |
