---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the model, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/models/&#123;model_id&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when the model resource was created, which is also when the training started. |
| <CopyableCode code="dataset" /> | `string` | The dataset from which the model is trained, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;` |
| <CopyableCode code="displayName" /> | `string` | The name of the model to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| <CopyableCode code="sourceLanguageCode" /> | `string` | Output only. The BCP-47 language code of the source language. |
| <CopyableCode code="targetLanguageCode" /> | `string` | Output only. The BCP-47 language code of the target language. |
| <CopyableCode code="testExampleCount" /> | `integer` | Output only. Number of examples (sentence pairs) used to test the model. |
| <CopyableCode code="trainExampleCount" /> | `integer` | Output only. Number of examples (sentence pairs) used to train the model. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this model was last updated. |
| <CopyableCode code="validateExampleCount" /> | `integer` | Output only. Number of examples (sentence pairs) used to validate the model. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_models_get" /> | `SELECT` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Gets a model. |
| <CopyableCode code="projects_locations_models_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists models. |
| <CopyableCode code="projects_locations_models_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Model. |
| <CopyableCode code="projects_locations_models_delete" /> | `DELETE` | <CopyableCode code="locationsId, modelsId, projectsId" /> | Deletes a model. |
| <CopyableCode code="_projects_locations_models_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists models. |
