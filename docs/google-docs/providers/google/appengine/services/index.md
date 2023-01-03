---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - appengine
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Relative name of the service within the application. Example: default.@OutputOnly |
| `name` | `string` | Full path to the Service resource in the API. Example: apps/myapp/services/default.@OutputOnly |
| `networkSettings` | `object` | A NetworkSettings resource is a container for ingress settings for a version or service. |
| `split` | `object` | Traffic routing configuration for versions within a single service. Traffic splits define how traffic directed to the service is assigned to versions. |
| `labels` | `object` | A set of labels to apply to this service. Labels are key/value pairs that describe the service and all resources that belong to it (e.g., versions). The labels can be used to search and group resources, and are propagated to the usage and billing reports, enabling fine-grain analysis of costs. An example of using labels is to tag resources belonging to different environments (e.g., "env=prod", "env=qa"). Label keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, dashes, and international characters. Label keys must start with a lowercase letter or an international character. Each service can have at most 32 labels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `apps_services_get` | `SELECT` | `appsId, servicesId` | Gets the current configuration of the specified service. |
| `apps_services_list` | `SELECT` | `appsId` | Lists all the services in the application. |
| `apps_services_delete` | `DELETE` | `appsId, servicesId` | Deletes the specified service and all enclosed versions. |
| `apps_services_patch` | `EXEC` | `appsId, servicesId` | Updates the configuration of the specified service. |
