---
title: workspaces_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_keys
  - ml_services
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
<tr><td><b>Name</b></td><td><code>workspaces_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.workspaces_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appInsightsInstrumentationKey" /> | `string` | The access key of the workspace app insights |
| <CopyableCode code="containerRegistryCredentials" /> | `object` |  |
| <CopyableCode code="notebookAccessKeys" /> | `object` |  |
| <CopyableCode code="userStorageArmId" /> | `string` | The arm Id key of the workspace storage |
| <CopyableCode code="userStorageKey" /> | `string` | The access key of the workspace storage |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
