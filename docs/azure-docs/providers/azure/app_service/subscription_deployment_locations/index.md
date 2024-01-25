---
title: subscription_deployment_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_deployment_locations
  - app_service
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
<tr><td><b>Name</b></td><td><code>subscription_deployment_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.subscription_deployment_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hostingEnvironmentDeploymentInfos` | `array` | Available App Service Environments with basic information. |
| `hostingEnvironments` | `array` | Available App Service Environments with full descriptions of the environments. |
| `locations` | `array` | Available regions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `subscriptionId` |
