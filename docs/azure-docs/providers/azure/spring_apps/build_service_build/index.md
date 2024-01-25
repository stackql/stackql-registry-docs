---
title: build_service_build
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_build
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
<tr><td><b>Name</b></td><td><code>build_service_build</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.build_service_build</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get a KPack build. |
| `create_or_update` | `INSERT` | `buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Create or update a KPack build. |
| `delete` | `DELETE` | `buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | delete a KPack build. |
