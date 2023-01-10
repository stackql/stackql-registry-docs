---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - intune
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.intune.operations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GetApps` | `EXEC` | `hostName` | Returns Intune Manageable apps. |
| `GetLocationByHostName` | `EXEC` |  | Returns location for given tenant. |
| `GetLocations` | `EXEC` |  | Returns location for user tenant. |
| `GetMAMFlaggedUserByName` | `EXEC` | `hostName, userName` | Returns Intune flagged user details |
| `GetMAMFlaggedUsers` | `EXEC` | `hostName` | Returns Intune flagged user collection |
| `GetMAMStatuses` | `EXEC` | `hostName` | Returns Intune Tenant level statuses. |
| `GetMAMUserDeviceByDeviceName` | `EXEC` | `deviceName, hostName, userName` | Get a unique device for a user. |
| `GetMAMUserDevices` | `EXEC` | `hostName, userName` | Get devices for a user. |
| `GetMAMUserFlaggedEnrolledApps` | `EXEC` | `hostName, userName` | Returns Intune flagged enrolled app collection for the User |
| `GetOperationResults` | `EXEC` | `hostName` | Returns operationResults. |
| `WipeMAMUserDevice` | `EXEC` | `deviceName, hostName, userName` | Wipe a device for a user. |
