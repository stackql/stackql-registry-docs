---
title: app_attach_package
hide_title: false
hide_table_of_contents: false
keywords:
  - app_attach_package
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>app_attach_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.app_attach_package</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Schema for App Attach Package properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appAttachPackageName, resourceGroupName, subscriptionId` | Get an app attach package. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List App Attach packages in resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List App Attach packages in subscription. |
| `create_or_update` | `INSERT` | `appAttachPackageName, resourceGroupName, subscriptionId, data__properties` | Create or update an App Attach package. |
| `delete` | `DELETE` | `appAttachPackageName, resourceGroupName, subscriptionId` | Remove an App Attach Package. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List App Attach packages in resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List App Attach packages in subscription. |
| `update` | `EXEC` | `appAttachPackageName, resourceGroupName, subscriptionId` | Update an App Attach Package |
