---
title: saved_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_queries
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
<tr><td><b>Name</b></td><td><code>saved_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.saved_queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the SavedQuery. |
| <CopyableCode code="annotationFilter" /> | `string` | Output only. Filters on the Annotations in the dataset. |
| <CopyableCode code="annotationSpecCount" /> | `integer` | Output only. Number of AnnotationSpecs in the context of the SavedQuery. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this SavedQuery was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of the SavedQuery. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="etag" /> | `string` | Used to perform a consistent read-modify-write update. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="metadata" /> | `any` | Some additional information about the SavedQuery. |
| <CopyableCode code="problemType" /> | `string` | Required. Problem type of the SavedQuery. Allowed values: * IMAGE_CLASSIFICATION_SINGLE_LABEL * IMAGE_CLASSIFICATION_MULTI_LABEL * IMAGE_BOUNDING_POLY * IMAGE_BOUNDING_BOX * TEXT_CLASSIFICATION_SINGLE_LABEL * TEXT_CLASSIFICATION_MULTI_LABEL * TEXT_EXTRACTION * TEXT_SENTIMENT * VIDEO_CLASSIFICATION * VIDEO_OBJECT_TRACKING |
| <CopyableCode code="supportAutomlTraining" /> | `boolean` | Output only. If the Annotations belonging to the SavedQuery can be used for AutoML training. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when SavedQuery was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists SavedQueries in a Dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId, locationsId, projectsId, savedQueriesId" /> | Deletes a SavedQuery. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists SavedQueries in a Dataset. |
