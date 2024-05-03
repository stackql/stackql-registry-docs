---
title: export_jobs_operation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - export_jobs_operation_result
  - data_protection
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
<tr><td><b>Name</b></td><td><code>export_jobs_operation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.export_jobs_operation_result" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobSasKey" /> | `string` | SAS key to access the blob. |
| <CopyableCode code="blobUrl" /> | `string` | URL of the blob into which the serialized string of list of jobs is exported. |
| <CopyableCode code="excelFileBlobSasKey" /> | `string` | SAS key to access the ExcelFile blob. |
| <CopyableCode code="excelFileBlobUrl" /> | `string` | URL of the blob into which the ExcelFile is uploaded. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> |
