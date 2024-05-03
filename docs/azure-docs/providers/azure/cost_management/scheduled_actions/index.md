---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - cost_management
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
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.scheduled_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | Resource Etag. For update calls, eTag is optional and can be specified to achieve optimistic concurrency. Fetch the resource's eTag by doing a 'GET' call first and then including the latest eTag as part of the request body or 'If-Match' header while performing the update. For create calls, eTag is not required. |
| <CopyableCode code="kind" /> | `string` | Kind of the scheduled action. |
| <CopyableCode code="properties" /> | `object` | The properties of the scheduled action. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Get the private scheduled action by name. |
| <CopyableCode code="list" /> | `SELECT` |  | List all private scheduled actions. |
| <CopyableCode code="list_by_scope" /> | `SELECT` | <CopyableCode code="scope" /> | List all shared scheduled actions within the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name" /> | Create or update a private scheduled action. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name" /> | Delete a private scheduled action. |
| <CopyableCode code="delete_by_scope" /> | `DELETE` | <CopyableCode code="name, scope" /> | Delete a scheduled action within the given scope. |
| <CopyableCode code="_list" /> | `EXEC` |  | List all private scheduled actions. |
| <CopyableCode code="_list_by_scope" /> | `EXEC` | <CopyableCode code="scope" /> | List all shared scheduled actions within the given scope. |
| <CopyableCode code="check_name_availability" /> | `EXEC` |  | Checks availability and correctness of the name for a scheduled action. |
| <CopyableCode code="check_name_availability_by_scope" /> | `EXEC` | <CopyableCode code="scope" /> | Checks availability and correctness of the name for a scheduled action within the given scope. |
| <CopyableCode code="create_or_update_by_scope" /> | `EXEC` | <CopyableCode code="name, scope" /> | Create or update a shared scheduled action within the given scope. |
| <CopyableCode code="get_by_scope" /> | `EXEC` | <CopyableCode code="name, scope" /> | Get the shared scheduled action from the given scope by name. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="name" /> | Processes a private scheduled action. |
| <CopyableCode code="run_by_scope" /> | `EXEC` | <CopyableCode code="name, scope" /> | Runs a shared scheduled action within the given scope. |
