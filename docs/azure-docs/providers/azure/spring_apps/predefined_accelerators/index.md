---
title: predefined_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - predefined_accelerators
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
<tr><td><b>Name</b></td><td><code>predefined_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.predefined_accelerators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Predefined accelerator properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Get the predefined accelerator. |
| `list` | `SELECT` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all predefined accelerators. |
| `_list` | `EXEC` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all predefined accelerators. |
| `disable` | `EXEC` | `applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Disable predefined accelerator. |
| `enable` | `EXEC` | `applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Enable predefined accelerator. |
