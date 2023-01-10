---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - app_platform
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | App resource properties payload |
| `identity` | `object` | Managed identity properties retrieved from ARM request headers. |
| `location` | `string` | The GEO location of the application, always the same with its parent resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Apps_Get` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | Get an App and its properties. |
| `Apps_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `Apps_CreateOrUpdate` | `INSERT` | `appName, resourceGroupName, serviceName, subscriptionId` | Create a new App or update an exiting App. |
| `Apps_Delete` | `DELETE` | `appName, resourceGroupName, serviceName, subscriptionId` | Operation to delete an App. |
| `Apps_GetResourceUploadUrl` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Get an resource upload URL for an App, which may be artifacts or source archive. |
| `Apps_SetActiveDeployments` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Set existing Deployment under the app as active |
| `Apps_Update` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting App. |
| `Apps_ValidateDomain` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId, data__name` | Check the resource name is valid as well as not in use. |
