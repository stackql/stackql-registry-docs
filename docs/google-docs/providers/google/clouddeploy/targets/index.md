---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - clouddeploy
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Name of the `Target`. Format is projects/{project}/locations/{location}/targets/a-z{0,62}. |
| `description` | `string` | Optional. Description of the `Target`. Max length is 255 characters. |
| `uid` | `string` | Output only. Unique identifier of the `Target`. |
| `etag` | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `createTime` | `string` | Output only. Time at which the `Target` was created. |
| `labels` | `object` | Optional. Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| `executionConfigs` | `array` | Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`. |
| `targetId` | `string` | Output only. Resource id of the `Target`. |
| `annotations` | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `requireApproval` | `boolean` | Optional. Whether or not the `Target` requires approval. |
| `gke` | `object` | Information specifying a GKE Cluster. |
| `updateTime` | `string` | Output only. Most recent time at which the `Target` was updated. |
| `anthosCluster` | `object` | Information specifying an Anthos Cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_targets_get` | `SELECT` | `locationsId, projectsId, targetsId` | Gets details of a single Target. |
| `projects_locations_targets_list` | `SELECT` | `locationsId, projectsId` | Lists Targets in a given project and location. |
| `projects_locations_targets_create` | `INSERT` | `locationsId, projectsId` | Creates a new Target in a given project and location. |
| `projects_locations_targets_delete` | `DELETE` | `locationsId, projectsId, targetsId` | Deletes a single Target. |
| `projects_locations_targets_patch` | `EXEC` | `locationsId, projectsId, targetsId` | Updates the parameters of a single Target. |
