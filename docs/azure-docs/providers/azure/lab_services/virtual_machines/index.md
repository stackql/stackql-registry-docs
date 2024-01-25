---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - lab_services
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.lab_services.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Virtual machine resource properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Returns the properties for a lab virtual machine. |
| `list_by_lab` | `SELECT` |  | Returns a list of all virtual machines for a lab. |
| `_list_by_lab` | `EXEC` |  | Returns a list of all virtual machines for a lab. |
| `redeploy` | `EXEC` |  | Action to redeploy a lab virtual machine to a different compute node. For troubleshooting connectivity. |
| `reimage` | `EXEC` |  | Re-image a lab virtual machine. The virtual machine will be deleted and recreated using the latest published snapshot of the reference environment of the lab. |
| `reset_password` | `EXEC` | `data__password, data__username` | Resets a lab virtual machine password. |
| `start` | `EXEC` |  | Action to start a lab virtual machine. |
| `stop` | `EXEC` |  | Action to stop a lab virtual machine. |
