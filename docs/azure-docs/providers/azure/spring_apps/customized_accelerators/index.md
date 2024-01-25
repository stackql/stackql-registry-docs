---
title: customized_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - customized_accelerators
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
<tr><td><b>Name</b></td><td><code>customized_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.customized_accelerators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Customized accelerator properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Get the customized accelerator. |
| `list` | `SELECT` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all customized accelerators. |
| `create_or_update` | `INSERT` | `applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Create or update the customized accelerator. |
| `delete` | `DELETE` | `applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Delete the customized accelerator. |
| `_list` | `EXEC` | `applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all customized accelerators. |
| `validate` | `EXEC` | `applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId, data__gitRepository` | Check the customized accelerator are valid. |
