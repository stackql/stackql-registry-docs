---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed identity properties retrieved from ARM request headers. |
| `location` | `string` | The GEO location of the application, always the same with its parent resource |
| `properties` | `object` | App resource properties payload |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | Get an App and its properties. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `create_or_update` | `INSERT` | `appName, resourceGroupName, serviceName, subscriptionId` | Create a new App or update an exiting App. |
| `delete` | `DELETE` | `appName, resourceGroupName, serviceName, subscriptionId` | Operation to delete an App. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `set_active_deployments` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Set existing Deployment under the app as active |
| `update` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting App. |
| `validate_domain` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId, data__name` | Check the resource name is valid as well as not in use. |
