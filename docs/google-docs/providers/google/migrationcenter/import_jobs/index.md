---
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
  - migrationcenter
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="migrationcenter.import_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the import job. |
| <CopyableCode code="assetSource" /> | `string` | Required. Reference to a source. |
| <CopyableCode code="completeTime" /> | `string` | Output only. The timestamp when the import job was completed. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the import job was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-friendly display name. Maximum length is 256 characters. |
| <CopyableCode code="executionReport" /> | `object` | A resource that reports result of the import job execution. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the import job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the import job was last updated. |
| <CopyableCode code="validationReport" /> | `object` | A resource that aggregates errors across import job files. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Gets the details of an import job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all import jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an import job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Deletes an import job. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all import jobs. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Updates an import job. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Runs an import job. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Validates an import job. |
