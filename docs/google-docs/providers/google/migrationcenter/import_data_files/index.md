---
title: import_data_files
hide_title: false
hide_table_of_contents: false
keywords:
  - import_data_files
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
<tr><td><b>Name</b></td><td><code>import_data_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="migrationcenter.import_data_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the file. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the file was created. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="format" /> | `string` | Required. The payload format. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the import data file. |
| <CopyableCode code="uploadFileInfo" /> | `object` | A resource that contains a URI to which a data file can be uploaded. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importDataFilesId, importJobsId, locationsId, projectsId" /> | Gets an import data file. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | List import data files. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Creates an import data file. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="importDataFilesId, importJobsId, locationsId, projectsId" /> | Delete an import data file. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | List import data files. |
