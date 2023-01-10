---
title: bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - bindings
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
<tr><td><b>Name</b></td><td><code>bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.bindings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Bindings_Get` | `SELECT` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Get a Binding and its properties. |
| `Bindings_List` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in an App. |
| `Bindings_CreateOrUpdate` | `INSERT` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Create a new Binding or update an exiting Binding. |
| `Bindings_Delete` | `DELETE` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Operation to delete a Binding. |
| `Bindings_Update` | `EXEC` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting Binding. |
