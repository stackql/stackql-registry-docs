---
title: diagnostic_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>diagnostic_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.diagnostic_settings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiagnosticSettings_GetDiagnosticProactiveLogCollectionSettings` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Gets the proactive log collection settings of the specified Data Box Edge/Data Box Gateway device. |
| `DiagnosticSettings_GetDiagnosticRemoteSupportSettings` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Gets the diagnostic remote support settings of the specified Data Box Edge/Data Box Gateway device. |
| `DiagnosticSettings_UpdateDiagnosticProactiveLogCollectionSettings` | `EXEC` | `deviceName, resourceGroupName, subscriptionId, data__properties` | Updates the proactive log collection settings on a Data Box Edge/Data Box Gateway device. |
| `DiagnosticSettings_UpdateDiagnosticRemoteSupportSettings` | `EXEC` | `deviceName, resourceGroupName, subscriptionId, data__properties` | Updates the diagnostic remote support settings on a Data Box Edge/Data Box Gateway device. |
