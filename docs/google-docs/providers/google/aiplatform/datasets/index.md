---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the Dataset. |
| `description` | `string` | The description of the Dataset. |
| `createTime` | `string` | Output only. Timestamp when this Dataset was created. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `labels` | `object` | The labels with user-defined metadata to organize your Datasets. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Dataset (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Dataset: * "aiplatform.googleapis.com/dataset_metadata_schema": output only, its value is the metadata_schema's title. |
| `metadataArtifact` | `string` | Output only. The resource name of the Artifact that was created in MetadataStore when creating the Dataset. The Artifact resource name pattern is `projects/&#123;project&#125;/locations/&#123;location&#125;/metadataStores/&#123;metadata_store&#125;/artifacts/&#123;artifact&#125;`. |
| `savedQueries` | `array` | All SavedQueries belong to the Dataset will be returned in List/Get Dataset response. The annotation_specs field will not be populated except for UI cases which will only use annotation_spec_count. In CreateDataset request, a SavedQuery is created together if this field is set, up to one SavedQuery can be set in CreateDatasetRequest. The SavedQuery should not contain any AnnotationSpec. |
| `metadata` | `any` | Required. Additional information about the Dataset. |
| `metadataSchemaUri` | `string` | Required. Points to a YAML file stored on Google Cloud Storage describing additional information about the Dataset. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/metadata/. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `dataItemCount` | `string` | Output only. The number of DataItems in this Dataset. Only apply for non-structured Dataset. |
| `updateTime` | `string` | Output only. Timestamp when this Dataset was last updated. |
| `displayName` | `string` | Required. The user-defined name of the Dataset. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetsId, locationsId, projectsId` | Gets a Dataset. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Datasets in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a Dataset. |
| `delete` | `DELETE` | `datasetsId, locationsId, projectsId` | Deletes a Dataset. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Datasets in a Location. |
| `export` | `EXEC` | `datasetsId, locationsId, projectsId` | Exports data from a Dataset. |
| `import` | `EXEC` | `datasetsId, locationsId, projectsId` | Imports data into a Dataset. |
| `patch` | `EXEC` | `datasetsId, locationsId, projectsId` | Updates a Dataset. |
| `search_data_items` | `EXEC` | `datasetsId, locationsId, projectsId` | Searches DataItems in a Dataset. |
