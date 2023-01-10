---
title: service_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - service_registries
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
<tr><td><b>Name</b></td><td><code>service_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.service_registries</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceRegistries_Get` | `SELECT` | `resourceGroupName, serviceName, serviceRegistryName, subscriptionId` | Get the Service Registry and its properties. |
| `ServiceRegistries_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in a Service. |
| `ServiceRegistries_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, serviceRegistryName, subscriptionId` | Create the default Service Registry or update the existing Service Registry. |
| `ServiceRegistries_Delete` | `DELETE` | `resourceGroupName, serviceName, serviceRegistryName, subscriptionId` | Disable the default Service Registry. |
