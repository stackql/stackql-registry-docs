---
title: android
hide_title: false
hide_table_of_contents: false
keywords:
  - android
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
<tr><td><b>Name</b></td><td><code>android</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.intune.android</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Android_AddAppForMAMPolicy` | `EXEC` | `appName, hostName, policyName` | Add app to an AndroidMAMPolicy. |
| `Android_AddGroupForMAMPolicy` | `EXEC` | `groupId, hostName, policyName` | Add group to an AndroidMAMPolicy. |
| `Android_CreateOrUpdateMAMPolicy` | `EXEC` | `hostName, policyName` | Creates or updates AndroidMAMPolicy. |
| `Android_DeleteAppForMAMPolicy` | `EXEC` | `appName, hostName, policyName` | Delete App for Android Policy |
| `Android_DeleteGroupForMAMPolicy` | `EXEC` | `groupId, hostName, policyName` | Delete Group for Android Policy |
| `Android_DeleteMAMPolicy` | `EXEC` | `hostName, policyName` | Delete Android Policy |
| `Android_GetAppForMAMPolicy` | `EXEC` | `hostName, policyName` | Get apps for an AndroidMAMPolicy. |
| `Android_GetGroupsForMAMPolicy` | `EXEC` | `hostName, policyName` | Returns groups for a given AndroidMAMPolicy. |
| `Android_GetMAMPolicies` | `EXEC` | `hostName` | Returns Intune Android policies. |
| `Android_GetMAMPolicyByName` | `EXEC` | `hostName, policyName` | Returns AndroidMAMPolicy with given name. |
| `Android_PatchMAMPolicy` | `EXEC` | `hostName, policyName` | Patch AndroidMAMPolicy. |
