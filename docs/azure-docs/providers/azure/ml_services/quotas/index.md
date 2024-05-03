---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `object` | The Resource Name. |
| <CopyableCode code="amlWorkspaceLocation" /> | `string` | Region of the AML workspace in the id. |
| <CopyableCode code="limit" /> | `integer` | The maximum permitted quota of the resource. |
| <CopyableCode code="type" /> | `string` | Specifies the resource type. |
| <CopyableCode code="unit" /> | `string` | An enum describing the unit of quota measurement. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets the currently assigned Workspace Quotas based on VMFamily. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Gets the currently assigned Workspace Quotas based on VMFamily. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Update quota for each VM family in workspace. |
