---
title: scope_access_review_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instance
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
<tr><td><b>Name</b></td><td><code>scope_access_review_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_instance" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apply_decisions" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to apply all decisions for an access review instance. |
| <CopyableCode code="record_all_decisions" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to approve/deny all decisions for a review with certain filters. |
| <CopyableCode code="reset_decisions" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to reset all decisions for an access review instance. |
| <CopyableCode code="send_reminders" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to send reminders for an access review instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> | An action to stop an access review instance. |
