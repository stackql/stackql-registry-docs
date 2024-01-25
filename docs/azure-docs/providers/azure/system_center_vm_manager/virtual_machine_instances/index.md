---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>virtual_machine_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.system_center_vm_manager.virtual_machine_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The extended location. |
| `properties` | `object` | Defines the resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceUri` | Retrieves information about a virtual machine instance. |
| `create_or_update` | `INSERT` | `resourceUri, data__extendedLocation, data__properties` | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| `delete` | `DELETE` | `resourceUri` | The operation to delete a virtual machine instance. |
| `restart` | `EXEC` | `resourceUri` | The operation to restart a virtual machine instance. |
| `restore_checkpoint` | `EXEC` | `resourceUri` | Restores to a checkpoint in virtual machine instance. |
| `start` | `EXEC` | `resourceUri` | The operation to start a virtual machine instance. |
| `stop` | `EXEC` | `resourceUri` | The operation to power off (stop) a virtual machine instance. |
| `update` | `EXEC` | `resourceUri` | The operation to update a virtual machine instance. |
