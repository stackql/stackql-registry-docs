---
title: provider_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_actions
  - app_compliance_automation
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>provider_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.provider_actions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_name_availability" /> | `EXEC` |  | Check if the given name is available for a report. |
| <CopyableCode code="list_in_use_storage_accounts" /> | `EXEC` |  | List the storage accounts which are in use by related reports |
| <CopyableCode code="onboard" /> | `EXEC` | <CopyableCode code="data__subscriptionIds" /> | Onboard given subscriptions to Microsoft.AppComplianceAutomation provider. |
| <CopyableCode code="trigger_evaluation" /> | `EXEC` | <CopyableCode code="data__resourceIds" /> | Trigger quick evaluation for the given subscriptions. |
