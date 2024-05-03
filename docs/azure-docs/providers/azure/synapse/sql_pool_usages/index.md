---
title: sql_pool_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_usages
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
<tr><td><b>Name</b></td><td><code>sql_pool_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the usage metric. |
| <CopyableCode code="currentValue" /> | `number` | The current value of the usage metric. |
| <CopyableCode code="displayName" /> | `string` | The usage metric display name. |
| <CopyableCode code="limit" /> | `number` | The current limit of the usage metric. |
| <CopyableCode code="nextResetTime" /> | `string` | The next reset time for the usage metric (ISO8601 format). |
| <CopyableCode code="resourceName" /> | `string` | The name of the resource. |
| <CopyableCode code="unit" /> | `string` | The units of the usage metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> |
