---
title: adaptive_mt_files
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_mt_files
  - translate
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
<tr><td><b>Name</b></td><td><code>adaptive_mt_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="translate.adaptive_mt_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the file, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/adaptiveMtDatasets/&#123;dataset&#125;/adaptiveMtFiles/&#123;file&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this file was created. |
| <CopyableCode code="displayName" /> | `string` | The file's display name. |
| <CopyableCode code="entryCount" /> | `integer` | The number of entries that the file contains. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this file was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_get" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, adaptiveMtFilesId, locationsId, projectsId" /> | Gets and AdaptiveMtFile |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_list" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Lists all AdaptiveMtFiles associated to an AdaptiveMtDataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_delete" /> | `DELETE` | <CopyableCode code="adaptiveMtDatasetsId, adaptiveMtFilesId, locationsId, projectsId" /> | Deletes an AdaptiveMtFile along with its sentences. |
| <CopyableCode code="_projects_locations_adaptive_mt_datasets_adaptive_mt_files_list" /> | `EXEC` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Lists all AdaptiveMtFiles associated to an AdaptiveMtDataset. |
