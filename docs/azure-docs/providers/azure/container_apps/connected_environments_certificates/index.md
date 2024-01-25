---
title: connected_environments_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_certificates
  - container_apps
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
<tr><td><b>Name</b></td><td><code>connected_environments_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.connected_environments_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Certificate resource specific properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `list` | `SELECT` | `connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `delete` | `DELETE` | `certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `_list` | `EXEC` | `connectedEnvironmentName, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId` | Patches a certificate. Currently only patching of tags is supported |
