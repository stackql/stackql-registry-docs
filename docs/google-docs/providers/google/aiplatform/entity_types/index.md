---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
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
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.entity_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Name of the EntityType. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featurestores/&#123;featurestore&#125;/entityTypes/&#123;entity_type&#125;` The last part entity_type is assigned by the client. The entity_type can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z and underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given a featurestore. |
| `description` | `string` | Optional. Description of the EntityType. |
| `monitoringConfig` | `object` | Configuration of how features in Featurestore are monitored. |
| `offlineStorageTtlDays` | `integer` | Optional. Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than `offline_storage_ttl_days` since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL. |
| `updateTime` | `string` | Output only. Timestamp when this EntityType was most recently updated. |
| `createTime` | `string` | Output only. Timestamp when this EntityType was created. |
| `etag` | `string` | Optional. Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `labels` | `object` | Optional. The labels with user-defined metadata to organize your EntityTypes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one EntityType (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `entityTypesId, featurestoresId, locationsId, projectsId` | Gets details of a single EntityType. |
| `list` | `SELECT` | `featurestoresId, locationsId, projectsId` | Lists EntityTypes in a given Featurestore. |
| `create` | `INSERT` | `featurestoresId, locationsId, projectsId` | Creates a new EntityType in a given Featurestore. |
| `delete` | `DELETE` | `entityTypesId, featurestoresId, locationsId, projectsId` | Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed. |
| `_list` | `EXEC` | `featurestoresId, locationsId, projectsId` | Lists EntityTypes in a given Featurestore. |
| `export_feature_values` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Exports Feature values from all the entities of a target EntityType. |
| `import_feature_values` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Imports Feature values into the Featurestore from a source storage. The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done. If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done. There are also scenarios where the caller can cause inconsistency. - Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned. |
| `patch` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Updates the parameters of a single EntityType. |
| `read_feature_values` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues. |
| `streaming_read_feature_values` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Reads Feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses. |
| `write_feature_values` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Writes Feature values of one or more entities of an EntityType. The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention. |
