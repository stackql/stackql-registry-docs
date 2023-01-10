---
title: build_service_builder
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_builder
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
<tr><td><b>Name</b></td><td><code>build_service_builder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.build_service_builder</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BuildServiceBuilder_Get` | `SELECT` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Get a KPack builder. |
| `BuildServiceBuilder_List` | `SELECT` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List KPack builders result. |
| `BuildServiceBuilder_CreateOrUpdate` | `INSERT` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Create or update a KPack builder. |
| `BuildServiceBuilder_Delete` | `DELETE` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | Delete a KPack builder. |
| `BuildServiceBuilder_ListDeployments` | `EXEC` | `buildServiceName, builderName, resourceGroupName, serviceName, subscriptionId` | List deployments that are using the builder. |
