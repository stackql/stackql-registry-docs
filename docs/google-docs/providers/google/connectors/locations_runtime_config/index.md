---
title: locations_runtime_config
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_runtime_config
  - connectors
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
<tr><td><b>Name</b></td><td><code>locations_runtime_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.locations_runtime_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `schemaGcsBucket` | `string` | Output only. The Cloud Storage bucket that stores connector's schema reports. |
| `state` | `string` | Output only. The state of the location. |
| `controlPlaneTopic` | `string` | Output only. Pub/Sub topic for control plne to send message. communication. E.g. projects/{project-id}/topics/{topic-id} |
| `serviceDirectory` | `string` | Output only. The name of the Service Directory service name. |
| `locationId` | `string` | Output only. location_id of the runtime location. E.g. "us-west1". |
| `conndTopic` | `string` | Output only. Pub/Sub topic for connd to send message. E.g. projects/{project-id}/topics/{topic-id} |
| `runtimeEndpoint` | `string` | Output only. The endpoint of the connectors runtime ingress. |
| `conndSubscription` | `string` | Output only. Pub/Sub subscription for connd to receive message. E.g. projects/{project-id}/subscriptions/{topic-id} |
| `controlPlaneSubscription` | `string` | Output only. Pub/Sub subscription for control plane to receive message. E.g. projects/{project-id}/subscriptions/{topic-id} |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_getRuntimeConfig` | `SELECT` | `locationsId, projectsId` |
