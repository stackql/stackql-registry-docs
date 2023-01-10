---
title: monitoring_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_settings
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
<tr><td><b>Name</b></td><td><code>monitoring_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.monitoring_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MonitoringSettings_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get the Monitoring Setting and its properties. |
| `MonitoringSettings_UpdatePatch` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Update the Monitoring Setting. |
| `MonitoringSettings_UpdatePut` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Update the Monitoring Setting. |
