---
title: commands
hide_title: false
hide_table_of_contents: false
keywords:
  - commands
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.commands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `issueTime` | `string` | The timestamp when the command was issued by the admin. |
| `payload` | `string` | The payload that the command specified, if any. |
| `state` | `string` | Indicates the command state. |
| `type` | `string` | The type of the command. |
| `commandExpireTime` | `string` | The time at which the command will expire. If the device doesn't execute the command within this time the command will become expired. |
| `commandId` | `string` | Unique ID of a device command. |
| `commandResult` | `object` | The result of executing a command. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `commandId, customerId, deviceId` |
