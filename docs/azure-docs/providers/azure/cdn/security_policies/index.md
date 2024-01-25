---
title: security_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies
  - cdn
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
<tr><td><b>Name</b></td><td><code>security_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.security_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Gets an existing security policy within a profile. |
| `list_by_profile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists security policies associated with the profile |
| `create` | `INSERT` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Creates a new security policy within the specified profile. |
| `delete` | `DELETE` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Deletes an existing security policy within profile. |
| `_list_by_profile` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Lists security policies associated with the profile |
| `patch` | `EXEC` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Updates an existing security policy within a profile. |
