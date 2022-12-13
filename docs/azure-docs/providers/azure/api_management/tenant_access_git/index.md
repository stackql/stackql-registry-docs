---
title: tenant_access_git
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access_git
  - api_management
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
<tr><td><b>Name</b></td><td><code>tenant_access_git</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tenant_access_git</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TenantAccessGit_RegeneratePrimaryKey` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Regenerate primary access key for GIT. |
| `TenantAccessGit_RegenerateSecondaryKey` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Regenerate secondary access key for GIT. |
