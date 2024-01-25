---
title: application_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - application_accelerators
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
<tr><td><b>Name</b></td><td><code>application_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.application_accelerators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Application accelerator properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Get the application accelerator. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handle requests to list all application accelerator. |
| `create_or_update` | `INSERT` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Create or update the application accelerator. |
| `delete` | `DELETE` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Delete the application accelerator. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Handle requests to list all application accelerator. |
