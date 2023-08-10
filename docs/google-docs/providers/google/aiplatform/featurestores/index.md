---
title: featurestores
hide_title: false
hide_table_of_contents: false
keywords:
  - featurestores
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
<tr><td><b>Name</b></td><td><code>featurestores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.featurestores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the Featurestore. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featurestores/&#123;featurestore&#125;` |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `labels` | `object` | Optional. The labels with user-defined metadata to organize your Featurestore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Featurestore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| `state` | `string` | Output only. State of the featurestore. |
| `onlineServingConfig` | `object` | OnlineServingConfig specifies the details for provisioning online serving resources. |
| `updateTime` | `string` | Output only. Timestamp when this Featurestore was last updated. |
| `createTime` | `string` | Output only. Timestamp when this Featurestore was created. |
| `etag` | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `onlineStorageTtlDays` | `integer` | Optional. TTL in days for feature values that will be stored in online serving storage. The Feature Store online storage periodically removes obsolete feature values older than `online_storage_ttl_days` since the feature generation time. Note that `online_storage_ttl_days` should be less than or equal to `offline_storage_ttl_days` for each EntityType under a featurestore. If not set, default to 4000 days |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `featurestoresId, locationsId, projectsId` | Gets details of a single Featurestore. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Featurestores in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Featurestore in a given project and location. |
| `delete` | `DELETE` | `featurestoresId, locationsId, projectsId` | Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Featurestores in a given project and location. |
| `batch_read_feature_values` | `EXEC` | `featurestoresId, locationsId, projectsId` | Batch reads Feature values from a Featurestore. This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp. |
| `patch` | `EXEC` | `featurestoresId, locationsId, projectsId` | Updates the parameters of a single Featurestore. |
| `search_features` | `EXEC` | `locationsId, projectsId` | Searches Features matching a query in a given project. |
