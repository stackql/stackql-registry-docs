---
title: serial_console
hide_title: false
hide_table_of_contents: false
keywords:
  - serial_console
  - serial_console
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
<tr><td><b>Name</b></td><td><code>serial_console</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.serial_console.serial_console</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DisableConsole` | `EXEC` | `default, subscriptionId` | Disables the Serial Console service for all VMs and VM scale sets in the provided subscription |
| `EnableConsole` | `EXEC` | `default, subscriptionId` | Enables the Serial Console service for all VMs and VM scale sets in the provided subscription |
| `GetConsoleStatus` | `EXEC` | `default, subscriptionId` | Gets whether or not Serial Console is disabled for a given subscription |
| `ListOperations` | `EXEC` |  | Gets a list of Serial Console API operations. |
