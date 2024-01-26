---
title: vm_instance_guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_instance_guest_agents
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
<tr><td><b>Name</b></td><td><code>vm_instance_guest_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.connected_vsphere.vm_instance_guest_agents</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `api-version, resourceUri` | Returns the list of GuestAgent of the given vm. |
| `create` | `INSERT` | `api-version, resourceUri, data__properties` | Create Or Update GuestAgent. |
| `delete` | `DELETE` | `api-version, resourceUri` | Implements GuestAgent DELETE method. |
| `_list` | `EXEC` | `api-version, resourceUri` | Returns the list of GuestAgent of the given vm. |
