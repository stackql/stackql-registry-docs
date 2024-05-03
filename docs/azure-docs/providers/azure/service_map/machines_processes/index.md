---
title: machines_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_processes
  - service_map
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
<tr><td><b>Name</b></td><td><code>machines_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_map.machines_processes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource ETAG. |
| <CopyableCode code="kind" /> | `string` | Additional resource type qualifier. |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId, workspaceName" /> |
