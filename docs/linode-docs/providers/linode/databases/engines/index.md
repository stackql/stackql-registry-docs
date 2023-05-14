---
title: engines
hide_title: false
hide_table_of_contents: false
keywords:
  - engines
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
<tr><td><b>Name</b></td><td><code>engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.databases.engines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Managed Database engine ID in engine/version format. |
| `version` | `string` | The Managed Database engine version. |
| `engine` | `string` | The Managed Database engine type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDatabasesEngine` | `SELECT` | `engineId` | Display information for a single Managed Database engine type and version.<br /> |
| `getDatabasesEngines` | `SELECT` |  | Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases.<br /> |
| `_getDatabasesEngine` | `EXEC` | `engineId` | Display information for a single Managed Database engine type and version.<br /> |
| `_getDatabasesEngines` | `EXEC` |  | Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases.<br /> |
