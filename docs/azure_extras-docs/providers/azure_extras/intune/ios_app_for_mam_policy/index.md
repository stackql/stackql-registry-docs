---
title: ios_app_for_mam_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - ios_app_for_mam_policy
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
<tr><td><b>Name</b></td><td><code>ios_app_for_mam_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.intune.ios_app_for_mam_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource Location |
| `properties` | `object` |  |
| `tags` | `object` | Resource Tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hostName, policyName` | Get apps for an iOSMAMPolicy. |
| `delete` | `DELETE` | `appName, hostName, policyName` | Delete App for Ios Policy |
| `_get` | `EXEC` | `hostName, policyName` | Get apps for an iOSMAMPolicy. |
