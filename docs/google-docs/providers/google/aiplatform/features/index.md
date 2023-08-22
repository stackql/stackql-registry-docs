---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
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
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.features</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Name of the Feature. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featurestores/&#123;featurestore&#125;/entityTypes/&#123;entity_type&#125;/features/&#123;feature&#125;` The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type. |
| `description` | `string` | Description of the Feature. |
| `valueType` | `string` | Required. Immutable. Type of Feature value. |
| `labels` | `object` | Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| `monitoringStatsAnomalies` | `array` | Output only. The list of historical stats and anomalies with specified objectives. |
| `updateTime` | `string` | Output only. Timestamp when this EntityType was most recently updated. |
| `createTime` | `string` | Output only. Timestamp when this EntityType was created. |
| `disableMonitoring` | `boolean` | Optional. If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType. |
| `etag` | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `entityTypesId, featuresId, featurestoresId, locationsId, projectsId` | Gets details of a single Feature. |
| `list` | `SELECT` | `entityTypesId, featurestoresId, locationsId, projectsId` | Lists Features in a given EntityType. |
| `create` | `INSERT` | `entityTypesId, featurestoresId, locationsId, projectsId` | Creates a new Feature in a given EntityType. |
| `delete` | `DELETE` | `entityTypesId, featuresId, featurestoresId, locationsId, projectsId` | Deletes a single Feature. |
| `_list` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Lists Features in a given EntityType. |
| `batch_create` | `EXEC` | `entityTypesId, featurestoresId, locationsId, projectsId` | Creates a batch of Features in a given EntityType. |
| `patch` | `EXEC` | `entityTypesId, featuresId, featurestoresId, locationsId, projectsId` | Updates the parameters of a single Feature. |
