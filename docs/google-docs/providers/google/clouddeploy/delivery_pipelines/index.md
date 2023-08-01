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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `unreachable` | `array` | Locations that could not be reached. |
| `deliveryPipelines` | `array` | The `DeliveryPipeline` objects. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId` | Gets details of a single DeliveryPipeline. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists DeliveryPipelines in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new DeliveryPipeline in a given project and location. |
| `delete` | `DELETE` | `deliveryPipelinesId, locationsId, projectsId` | Deletes a single DeliveryPipeline. |
| `patch` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId` | Updates the parameters of a single DeliveryPipeline. |
