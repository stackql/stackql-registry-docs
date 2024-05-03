---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - container_registry
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.runs" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Gets the detailed information for a given run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Gets all the runs for a registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Gets all the runs for a registry. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Cancel an existing run. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Patch the run properties. |
