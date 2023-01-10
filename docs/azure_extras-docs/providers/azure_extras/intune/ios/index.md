---
title: ios
hide_title: false
hide_table_of_contents: false
keywords:
  - ios
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
<tr><td><b>Name</b></td><td><code>ios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.intune.ios</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Ios_AddAppForMAMPolicy` | `EXEC` | `appName, hostName, policyName` | Add app to an iOSMAMPolicy. |
| `Ios_AddGroupForMAMPolicy` | `EXEC` | `groupId, hostName, policyName` | Add group to an iOSMAMPolicy. |
| `Ios_CreateOrUpdateMAMPolicy` | `EXEC` | `hostName, policyName` | Creates or updates iOSMAMPolicy. |
| `Ios_DeleteAppForMAMPolicy` | `EXEC` | `appName, hostName, policyName` | Delete App for Ios Policy |
| `Ios_DeleteGroupForMAMPolicy` | `EXEC` | `groupId, hostName, policyName` | Delete Group for iOS Policy |
| `Ios_DeleteMAMPolicy` | `EXEC` | `hostName, policyName` | Delete Ios Policy |
| `Ios_GetAppForMAMPolicy` | `EXEC` | `hostName, policyName` | Get apps for an iOSMAMPolicy. |
| `Ios_GetGroupsForMAMPolicy` | `EXEC` | `hostName, policyName` | Returns groups for a given iOSMAMPolicy. |
| `Ios_GetMAMPolicies` | `EXEC` | `hostName` | Returns Intune iOSPolicies. |
| `Ios_GetMAMPolicyByName` | `EXEC` | `hostName, policyName` | Returns Intune iOS policies. |
| `Ios_PatchMAMPolicy` | `EXEC` | `hostName, policyName` |  patch an iOSMAMPolicy. |
