---
title: integration_runtime_stop
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_stop
  - synapse
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
<tr><td><b>Name</b></td><td><code>integration_runtime_stop</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtime_stop" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="error" /> | `string` | The operation error message. |
| <CopyableCode code="properties" /> | `object` | The operation properties. |
| <CopyableCode code="status" /> | `string` | status of Start Integrationruntimes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, integrationRuntimeOperationId, resourceGroupName, subscriptionId, workspaceName" /> |
