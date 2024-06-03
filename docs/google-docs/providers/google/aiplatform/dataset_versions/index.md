---
title: dataset_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_versions
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>dataset_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.dataset_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the DatasetVersion. |
| <CopyableCode code="bigQueryDatasetName" /> | `string` | Output only. Name of the associated BigQuery dataset. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this DatasetVersion was created. |
| <CopyableCode code="displayName" /> | `string` | The user-defined name of the DatasetVersion. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="metadata" /> | `any` | Required. Output only. Additional information about the DatasetVersion. |
| <CopyableCode code="modelReference" /> | `string` | Output only. Reference to the public base model last used by the dataset version. Only set for prompt dataset versions. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this DatasetVersion was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetVersionsId, datasetsId, locationsId, projectsId" /> | Gets a Dataset version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists DatasetVersions in a Dataset. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Create a version from a Dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetVersionsId, datasetsId, locationsId, projectsId" /> | Deletes a Dataset version. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetVersionsId, datasetsId, locationsId, projectsId" /> | Updates a DatasetVersion. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists DatasetVersions in a Dataset. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="datasetVersionsId, datasetsId, locationsId, projectsId" /> | Restores a dataset version. |
