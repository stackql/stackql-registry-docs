---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - lab_services
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.lab_services.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Virtual machine resource properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_Get` | `SELECT` |  | Returns the properties for a lab virtual machine. |
| `VirtualMachines_ListByLab` | `SELECT` |  | Returns a list of all virtual machines for a lab. |
| `VirtualMachines_Redeploy` | `EXEC` |  | Action to redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity. |
| `VirtualMachines_Reimage` | `EXEC` |  | Re-image a lab virtual machine. The virtual machine will be deleted and recreated using the latest published snapshot of the reference environment of the lab. |
| `VirtualMachines_ResetPassword` | `EXEC` | `data__password, data__username` | Resets a lab virtual machine password. |
| `VirtualMachines_Start` | `EXEC` |  | Action to start a lab virtual machine. |
| `VirtualMachines_Stop` | `EXEC` |  | Action to stop a lab virtual machine. |
