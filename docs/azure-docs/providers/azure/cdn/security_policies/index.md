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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityPolicies_Get` | `SELECT` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Gets an existing security policy within a profile. |
| `SecurityPolicies_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists security policies associated with the profile |
| `SecurityPolicies_Create` | `INSERT` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Creates a new security policy within the specified profile. |
| `SecurityPolicies_Delete` | `DELETE` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Deletes an existing security policy within profile. |
| `SecurityPolicies_Patch` | `EXEC` | `profileName, resourceGroupName, securityPolicyName, subscriptionId` | Updates an existing security policy within a profile. |
