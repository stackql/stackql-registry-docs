---
title: governance_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_assignments
  - security
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
<tr><td><b>Name</b></td><td><code>governance_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.governance_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes properties of an governance assignment |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, assessmentName, assignmentKey, scope` | Get a specific governanceAssignment for the requested scope by AssignmentKey |
| `list` | `SELECT` | `api-version, assessmentName, scope` | Get governance assignments on all of your resources inside a scope |
| `create_or_update` | `INSERT` | `api-version, assessmentName, assignmentKey, scope` | Creates or updates a governance assignment on the given subscription. |
| `delete` | `DELETE` | `api-version, assessmentName, assignmentKey, scope` | Delete a GovernanceAssignment over a given scope |
| `_list` | `EXEC` | `api-version, assessmentName, scope` | Get governance assignments on all of your resources inside a scope |
