---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - connected_vsphere
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
<tr><td><b>Name</b></td><td><code>virtual_machine_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.connected_vsphere.virtual_machine_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The extended location. |
| `properties` | `object` | Describes the properties of a Virtual Machine Instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `api-version, resourceUri` | Lists all of the virtual machine instances within the specified parent resource. |
| `create_or_update` | `INSERT` | `api-version, resourceUri, data__properties` | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| `delete` | `DELETE` | `api-version, resourceUri` | The operation to delete a virtual machine instance. |
| `_list` | `EXEC` | `api-version, resourceUri` | Lists all of the virtual machine instances within the specified parent resource. |
| `restart` | `EXEC` | `api-version, resourceUri` | The operation to restart a virtual machine instance. |
| `start` | `EXEC` | `api-version, resourceUri` | The operation to start a virtual machine instance. |
| `stop` | `EXEC` | `api-version, resourceUri` | The operation to power off (stop) a virtual machine instance. |
| `update` | `EXEC` | `api-version, resourceUri` | The operation to update a virtual machine instance. |
