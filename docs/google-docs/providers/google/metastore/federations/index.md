---
title: federations
hide_title: false
hide_table_of_contents: false
keywords:
  - federations
  - metastore
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
<tr><td><b>Name</b></td><td><code>federations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.federations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the federation, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/federations/&#123;federation_id&#125;`. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore federation. |
| `labels` | `object` | User-defined labels for the metastore federation. |
| `version` | `string` | Immutable. The Apache Hive metastore version of the federation. All backend metastore versions must be compatible with the federation version. |
| `endpointUri` | `string` | Output only. The federation endpoint. |
| `backendMetastores` | `object` | A map from BackendMetastore rank to BackendMetastores from which the federation service serves metadata at query time. The map key represents the order in which BackendMetastores should be evaluated to resolve database names at query time and should be greater than or equal to zero. A BackendMetastore with a lower number will be evaluated before a BackendMetastore with a higher number. |
| `state` | `string` | Output only. The current state of the federation. |
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore federation, if available. |
| `createTime` | `string` | Output only. The time when the metastore federation was created. |
| `updateTime` | `string` | Output only. The time when the metastore federation was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `federationsId, locationsId, projectsId` | Gets the details of a single federation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists federations in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a metastore federation in a project and location. |
| `delete` | `DELETE` | `federationsId, locationsId, projectsId` | Deletes a single federation. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists federations in a project and location. |
| `patch` | `EXEC` | `federationsId, locationsId, projectsId` | Updates the fields of a federation. |
