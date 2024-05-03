---
title: workspace_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_settings
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
<tr><td><b>Name</b></td><td><code>workspace_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.workspace_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Workspace setting data |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId, workspaceSettingName" /> | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, subscriptionId, workspaceSettingName" /> | creating settings about where we should store your security data and logs |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, subscriptionId, workspaceSettingName" /> | Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId, workspaceSettingName" /> | Settings about where we should store your security data and logs |
