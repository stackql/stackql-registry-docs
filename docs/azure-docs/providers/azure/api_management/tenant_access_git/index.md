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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_access_git</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_access_git" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate primary access key for GIT. |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> | Regenerate secondary access key for GIT. |
