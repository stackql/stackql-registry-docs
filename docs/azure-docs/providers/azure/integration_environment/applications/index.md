---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of application. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationName, resourceGroupName, spaceName, subscriptionId` | Get a Application |
| `list_by_space` | `SELECT` | `resourceGroupName, spaceName, subscriptionId` | List Application resources by Space |
| `create_or_update` | `INSERT` | `applicationName, resourceGroupName, spaceName, subscriptionId` | Create a Application |
| `delete` | `DELETE` | `applicationName, resourceGroupName, spaceName, subscriptionId` | Delete a Application |
| `_list_by_space` | `EXEC` | `resourceGroupName, spaceName, subscriptionId` | List Application resources by Space |
| `patch` | `EXEC` | `applicationName, resourceGroupName, spaceName, subscriptionId` | Update a Application |
| `save_business_process_development_artifact` | `EXEC` | `applicationName, resourceGroupName, spaceName, subscriptionId, data__name` | The save business process development artifact action. |
| `validate_business_process_development_artifact` | `EXEC` | `applicationName, resourceGroupName, spaceName, subscriptionId, data__name` | The validate business process development artifact action. |
