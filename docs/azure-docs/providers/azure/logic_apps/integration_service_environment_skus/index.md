---
title: integration_service_environment_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_skus
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_service_environment_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_service_environment_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | The integration service environment sku capacity. |
| `resourceType` | `string` | The resource type. |
| `sku` | `object` | The sku. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `IntegrationServiceEnvironmentSkus_List` | `SELECT` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` |
