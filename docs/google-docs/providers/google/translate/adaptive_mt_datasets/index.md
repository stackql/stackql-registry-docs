---
title: adaptive_mt_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_mt_datasets
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
<tr><td><b>Name</b></td><td><code>adaptive_mt_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="translate.adaptive_mt_datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the dataset, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/adaptiveMtDatasets/&#123;dataset_id&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this dataset was created. |
| <CopyableCode code="displayName" /> | `string` | The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| <CopyableCode code="exampleCount" /> | `integer` | The number of examples in the dataset. |
| <CopyableCode code="sourceLanguageCode" /> | `string` | The BCP-47 language code of the source language. |
| <CopyableCode code="targetLanguageCode" /> | `string` | The BCP-47 language code of the target language. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this dataset was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_adaptive_mt_datasets_get" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Gets the Adaptive MT dataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all Adaptive MT datasets for which the caller has read permission. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Adaptive MT dataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_delete" /> | `DELETE` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Deletes an Adaptive MT dataset, including all its entries and associated metadata. |
| <CopyableCode code="_projects_locations_adaptive_mt_datasets_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all Adaptive MT datasets for which the caller has read permission. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_import_adaptive_mt_file" /> | `EXEC` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Imports an AdaptiveMtFile and adds all of its sentences into the AdaptiveMtDataset. |
