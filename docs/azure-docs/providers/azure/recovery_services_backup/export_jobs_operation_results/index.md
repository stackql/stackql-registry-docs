---
title: export_jobs_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - export_jobs_operation_results
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
<tr><td><b>Name</b></td><td><code>export_jobs_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.export_jobs_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="headers" /> | `object` | HTTP headers associated with this operation. |
| <CopyableCode code="operation" /> | `object` | Base class for operation result info. |
| <CopyableCode code="statusCode" /> | `string` | HTTP Status Code of the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, operationId, resourceGroupName, subscriptionId, vaultName" /> |
