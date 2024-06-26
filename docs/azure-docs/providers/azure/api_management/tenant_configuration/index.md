---
title: tenant_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configuration
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
<tr><td><b>Name</b></td><td><code>tenant_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_configuration" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete. |
| <CopyableCode code="save" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete. |
