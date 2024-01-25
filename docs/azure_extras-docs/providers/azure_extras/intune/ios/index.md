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
| `add_app_for_mam_policy` | `EXEC` | `appName, hostName, policyName` | Add app to an iOSMAMPolicy. |
| `add_group_for_mam_policy` | `EXEC` | `groupId, hostName, policyName` | Add group to an iOSMAMPolicy. |
| `patch_mam_policy` | `EXEC` | `hostName, policyName` |  patch an iOSMAMPolicy. |
