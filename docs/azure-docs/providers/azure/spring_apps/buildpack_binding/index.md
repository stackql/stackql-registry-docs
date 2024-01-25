---
title: buildpack_binding
hide_title: false
hide_table_of_contents: false
keywords:
  - buildpack_binding
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
<tr><td><b>Name</b></td><td><code>buildpack_binding</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.buildpack_binding</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId` | Get a buildpack binding by name. |
| `list` | `SELECT` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all buildpack bindings in a builder. |
| `create_or_update` | `INSERT` | `buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId` | Create or update a buildpack binding. |
| `delete` | `DELETE` | `buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId` | Operation to delete a Buildpack Binding |
| `_list` | `EXEC` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all buildpack bindings in a builder. |
