---
title: build_service_builder
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_builder
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
<tr><td><b>Name</b></td><td><code>build_service_builder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.build_service_builder</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Get a KPack builder. |
| `list` | `SELECT` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List KPack builders result. |
| `create_or_update` | `INSERT` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Create or update a KPack builder. |
| `delete` | `DELETE` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Delete a KPack builder. |
| `_list` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List KPack builders result. |
