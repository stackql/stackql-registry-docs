---
title: export_jobs_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - export_jobs_operation_results
  - data_protection
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>export_jobs_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>export_jobs_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.export_jobs_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobSasKey" /> | `string` | SAS key to access the blob. |
| <CopyableCode code="blobUrl" /> | `string` | URL of the blob into which the serialized string of list of jobs is exported. |
| <CopyableCode code="excelFileBlobSasKey" /> | `string` | SAS key to access the ExcelFile blob. |
| <CopyableCode code="excelFileBlobUrl" /> | `string` | URL of the blob into which the ExcelFile is uploaded. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, vaultName" /> | Gets the operation result of operation triggered by Export Jobs API. If the operation is successful, then it also contains URL of a Blob and a SAS key to access the same. The blob contains exported jobs in JSON serialized format. |

## `SELECT` examples

Gets the operation result of operation triggered by Export Jobs API. If the operation is successful, then it also contains URL of a Blob and a SAS key to access the same. The blob contains exported jobs in JSON serialized format.


```sql
SELECT
blobSasKey,
blobUrl,
excelFileBlobSasKey,
excelFileBlobUrl
FROM azure.data_protection.export_jobs_operation_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```