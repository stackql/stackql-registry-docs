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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.saved_queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the SavedQuery. |
| `problemType` | `string` | Required. Problem type of the SavedQuery. Allowed values: * IMAGE_CLASSIFICATION_SINGLE_LABEL * IMAGE_CLASSIFICATION_MULTI_LABEL * IMAGE_BOUNDING_POLY * IMAGE_BOUNDING_BOX * TEXT_CLASSIFICATION_SINGLE_LABEL * TEXT_CLASSIFICATION_MULTI_LABEL * TEXT_EXTRACTION * TEXT_SENTIMENT * VIDEO_CLASSIFICATION * VIDEO_OBJECT_TRACKING |
| `displayName` | `string` | Required. The user-defined name of the SavedQuery. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| `annotationFilter` | `string` | Output only. Filters on the Annotations in the dataset. |
| `annotationSpecCount` | `integer` | Output only. Number of AnnotationSpecs in the context of the SavedQuery. |
| `createTime` | `string` | Output only. Timestamp when this SavedQuery was created. |
| `updateTime` | `string` | Output only. Timestamp when SavedQuery was last updated. |
| `metadata` | `any` | Some additional information about the SavedQuery. |
| `supportAutomlTraining` | `boolean` | Output only. If the Annotations belonging to the SavedQuery can be used for AutoML training. |
| `etag` | `string` | Used to perform a consistent read-modify-write update. If not set, a blind "overwrite" update happens. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `datasetsId, locationsId, projectsId` | Lists SavedQueries in a Dataset. |
| `delete` | `DELETE` | `datasetsId, locationsId, projectsId, savedQueriesId` | Deletes a SavedQuery. |
| `_list` | `EXEC` | `datasetsId, locationsId, projectsId` | Lists SavedQueries in a Dataset. |
