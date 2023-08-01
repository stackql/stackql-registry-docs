---
title: monitored_resource_descriptors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_resource_descriptors
  - monitoring
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
<tr><td><b>Name</b></td><td><code>monitored_resource_descriptors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.monitored_resource_descriptors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceDescriptors` | `array` | The monitored resource descriptors that are available to this project and that match filter, if present. |
| `nextPageToken` | `string` | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_monitored_resource_descriptors_get` | `SELECT` | `monitoredResourceDescriptorsId, projectsId` | Gets a single monitored resource descriptor. |
| `projects_monitored_resource_descriptors_list` | `SELECT` | `projectsId` | Lists monitored resource descriptors that match a filter. |
