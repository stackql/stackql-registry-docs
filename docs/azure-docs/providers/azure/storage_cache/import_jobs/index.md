---
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.import_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the import job. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Returns an import job. |
| <CopyableCode code="list_by_aml_filesystem" /> | `SELECT` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Returns all import jobs the user has access to under an AML File System. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Create or update an import job. Import jobs are automatically deleted 72 hours after completion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Schedules an import job for deletion. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Update an import job instance. |
