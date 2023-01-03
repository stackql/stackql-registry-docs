---
title: delivery_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_pipelines
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
<tr><td><b>Name</b></td><td><code>delivery_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.delivery_pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. Name of the `DeliveryPipeline`. Format is projects/{project}/ locations/{location}/deliveryPipelines/a-z{0,62}. |
| `description` | `string` | Description of the `DeliveryPipeline`. Max length is 255 characters. |
| `serialPipeline` | `object` | SerialPipeline defines a sequential set of stages for a `DeliveryPipeline`. |
| `uid` | `string` | Output only. Unique identifier of the `DeliveryPipeline`. |
| `createTime` | `string` | Output only. Time at which the pipeline was created. |
| `labels` | `object` | Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;= 128 bytes. |
| `suspended` | `boolean` | When suspended, no new releases or rollouts can be created, but in-progress ones will complete. |
| `annotations` | `object` | User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `updateTime` | `string` | Output only. Most recent time at which the pipeline was updated. |
| `condition` | `object` | PipelineCondition contains all conditions relevant to a Delivery Pipeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_deliveryPipelines_get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId` | Gets details of a single DeliveryPipeline. |
| `projects_locations_deliveryPipelines_list` | `SELECT` | `locationsId, projectsId` | Lists DeliveryPipelines in a given project and location. |
| `projects_locations_deliveryPipelines_create` | `INSERT` | `locationsId, projectsId` | Creates a new DeliveryPipeline in a given project and location. |
| `projects_locations_deliveryPipelines_delete` | `DELETE` | `deliveryPipelinesId, locationsId, projectsId` | Deletes a single DeliveryPipeline. |
| `projects_locations_deliveryPipelines_patch` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId` | Updates the parameters of a single DeliveryPipeline. |
