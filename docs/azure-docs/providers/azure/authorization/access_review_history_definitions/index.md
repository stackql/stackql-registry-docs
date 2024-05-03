---
title: access_review_history_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definitions
  - authorization
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
<tr><td><b>Name</b></td><td><code>access_review_history_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_history_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review history definition id. |
| <CopyableCode code="name" /> | `string` | The access review history definition unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review History Instances. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the accessReviewHistoryDefinitions available from this provider, definition instances are only available for 30 days after creation. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists the accessReviewHistoryDefinitions available from this provider, definition instances are only available for 30 days after creation. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="historyDefinitionId, subscriptionId" /> | Get access review history definition by definition Id |
