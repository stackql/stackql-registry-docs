---
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
  - databases
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.databases.types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID representing the Managed Database node plan type. |
| `memory` | `integer` | The amount of RAM allocated to Database created of this plan type. The value is represented in megabytes. |
| `vcpus` | `integer` | The integer of number CPUs allocated to databases of this plan type. |
| `class` | `string` | The compute class category. |
| `deprecated` | `boolean` | Whether this Database plan type has been deprecated and is no longer available. |
| `disk` | `integer` | The amount of disk space set aside for Databases of this plan type. The value is represented in megabytes. |
| `engines` | `object` |  |
| `label` | `string` | A human-readable string that describes each plan type. For display purposes only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDatabasesType` | `SELECT` | `typeId` | Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance.<br /> |
| `getDatabasesTypes` | `SELECT` |  | Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.<br /><br />Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type.<br /> |
| `_getDatabasesType` | `EXEC` | `typeId` | Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance.<br /> |
| `_getDatabasesTypes` | `EXEC` |  | Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.<br /><br />Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type.<br /> |
