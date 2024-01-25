---
title: bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - bindings
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
<tr><td><b>Name</b></td><td><code>bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.bindings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Get a Binding and its properties. |
| `list` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in an App. |
| `create_or_update` | `INSERT` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Create a new Binding or update an exiting Binding. |
| `delete` | `DELETE` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Operation to delete a Binding. |
| `_list` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in an App. |
| `update` | `EXEC` | `appName, bindingName, resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting Binding. |
