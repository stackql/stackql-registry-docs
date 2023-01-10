---
title: buildpack_binding
hide_title: false
hide_table_of_contents: false
keywords:
  - buildpack_binding
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
<tr><td><b>Name</b></td><td><code>buildpack_binding</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.buildpack_binding</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BuildpackBinding_Get` | `SELECT` | `buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId` | Get a buildpack binding by name. |
| `BuildpackBinding_List` | `SELECT` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all buildpack bindings in a builder. |
| `BuildpackBinding_CreateOrUpdate` | `INSERT` | `buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId` | Create or update a buildpack binding. |
| `BuildpackBinding_Delete` | `DELETE` | `buildServiceName, builderName, buildpackBindingName, resourceGroupName, serviceName, subscriptionId` | Operation to delete a Buildpack Binding |
