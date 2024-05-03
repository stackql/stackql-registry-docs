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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>governance_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.governance_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Describes properties of an governance assignment |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, assessmentName, assignmentKey, scope" /> | Get a specific governanceAssignment for the requested scope by AssignmentKey |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, assessmentName, scope" /> | Get governance assignments on all of your resources inside a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, assessmentName, assignmentKey, scope" /> | Creates or updates a governance assignment on the given subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, assessmentName, assignmentKey, scope" /> | Delete a GovernanceAssignment over a given scope |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, assessmentName, scope" /> | Get governance assignments on all of your resources inside a scope |
