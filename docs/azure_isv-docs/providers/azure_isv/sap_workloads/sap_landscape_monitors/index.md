---
title: sap_landscape_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_landscape_monitors
  - sap_workloads
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>sap_landscape_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.sap_workloads.sap_landscape_monitors</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` | Gets configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name. |
| `create` | `INSERT` | `monitorName, resourceGroupName, subscriptionId` | Creates a SAP Landscape Monitor Dashboard for the specified subscription, resource group, and resource name. |
| `_list` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` | Gets configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name. |
