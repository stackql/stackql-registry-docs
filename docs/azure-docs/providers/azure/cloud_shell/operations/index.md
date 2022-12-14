---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - cloud_shell
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cloud_shell.operations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeleteConsole` | `EXEC` | `consoleName` | Deletes the console |
| `DeleteUserSettings` | `EXEC` | `userSettingsName` | Delete cloud shell settings for current signed in user |
| `GetConsole` | `EXEC` | `consoleName` | Gets the console for the user. |
| `GetUserSettings` | `EXEC` | `userSettingsName` | Get current user settings for current signed in user. This operation returns settings for the user's cloud shell preferences including preferred location, storage profile, shell type, font and size settings. |
| `KeepAlive` | `EXEC` | `consoleName` | Keep console alive |
| `PatchUserSettings` | `EXEC` | `userSettingsName` | Patch cloud shell settings for current signed in user |
| `PutConsole` | `EXEC` | `consoleName, data__properties` | Puts a request for a console |
| `PutUserSettings` | `EXEC` | `userSettingsName, data__properties` | Create or update cloud shell settings for current signed in user |
| `deleteConsoleWithLocation` | `EXEC` | `consoleName, location` | Deletes the console |
| `deleteUserSettingsWithLocation` | `EXEC` | `location, userSettingsName` | Delete cloud shell settings for current signed in user |
| `getConsoleWithLocation` | `EXEC` | `consoleName, location` | Gets the console for the user. |
| `getUserSettingsWithLocation` | `EXEC` | `location, userSettingsName` | Get current user settings for current signed in user. This operation returns settings for the user's cloud shell preferences including preferred location, storage profile, shell type, font and size settings. |
| `keepAliveWithLocation` | `EXEC` | `consoleName, location` | Keep console alive |
| `patchUserSettingsWithLocation` | `EXEC` | `location, userSettingsName` | Patch cloud shell settings for current signed in user |
| `putConsoleWithLocation` | `EXEC` | `consoleName, location` | Puts a request for a console |
| `putUserSettingsWithLocation` | `EXEC` | `location, userSettingsName, data__properties` | Create or update cloud shell settings for current signed in user |
