---
title: releases
hide_title: false
hide_table_of_contents: false
keywords:
  - releases
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Name of the `Release`. Format is projects/&#123;project&#125;/ locations/&#123;location&#125;/deliveryPipelines/&#123;deliveryPipeline&#125;/ releases/a-z&#123;0,62&#125;. |
| `description` | `string` | Description of the `Release`. Max length is 255 characters. |
| `uid` | `string` | Output only. Unique identifier of the `Release`. |
| `buildArtifacts` | `array` | List of artifacts to pass through to Skaffold command. |
| `targetSnapshots` | `array` | Output only. Snapshot of the targets taken at release creation time. |
| `abandoned` | `boolean` | Output only. Indicates whether this is an abandoned release. |
| `renderEndTime` | `string` | Output only. Time at which the render completed. |
| `renderStartTime` | `string` | Output only. Time at which the render began. |
| `annotations` | `object` | User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `targetRenders` | `object` | Output only. Map from target ID to details of the render operation for that target. |
| `labels` | `object` | Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| `skaffoldConfigUri` | `string` | Cloud Storage URI of tar.gz archive containing Skaffold configuration. |
| `renderState` | `string` | Output only. Current state of the render operation. |
| `skaffoldConfigPath` | `string` | Filepath of the Skaffold config inside of the config URI. |
| `createTime` | `string` | Output only. Time at which the `Release` was created. |
| `skaffoldVersion` | `string` | The Skaffold version to use when operating on this release, such as "1.20.0". Not all versions are valid; Google Cloud Deploy supports a specific set of versions. If unset, the most recent supported Skaffold version will be used. |
| `targetArtifacts` | `object` | Output only. Map from target ID to the target artifacts created during the render operation. |
| `deliveryPipelineSnapshot` | `object` | A `DeliveryPipeline` resource in the Google Cloud Deploy API. A `DeliveryPipeline` defines a pipeline through which a Skaffold configuration can progress. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_deliveryPipelines_releases_get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Gets details of a single Release. |
| `projects_locations_deliveryPipelines_releases_list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId` | Lists Releases in a given project and location. |
| `projects_locations_deliveryPipelines_releases_create` | `INSERT` | `deliveryPipelinesId, locationsId, projectsId` | Creates a new Release in a given project and location. |
| `projects_locations_deliveryPipelines_releases_abandon` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Abandons a Release in the Delivery Pipeline. |
