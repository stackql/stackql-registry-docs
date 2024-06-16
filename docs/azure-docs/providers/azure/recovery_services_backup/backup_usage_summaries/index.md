---
title: backup_usage_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_usage_summaries
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>backup_usage_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_usage_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The name of usage. |
| <CopyableCode code="currentValue" /> | `integer` | Current value of usage. |
| <CopyableCode code="limit" /> | `integer` | Limit of usage. |
| <CopyableCode code="nextResetTime" /> | `string` | Next reset time of usage. |
| <CopyableCode code="quotaPeriod" /> | `string` | Quota period of usage. |
| <CopyableCode code="unit" /> | `string` | Unit of the usage. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, vaultName" /> |
