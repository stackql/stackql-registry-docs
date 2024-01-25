---
title: deployments_remote_debugging_config
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_remote_debugging_config
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
<tr><td><b>Name</b></td><td><code>deployments_remote_debugging_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.deployments_remote_debugging_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enabled` | `boolean` | Indicate if remote debugging is enabled |
| `port` | `integer` | Application debugging port |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` |
