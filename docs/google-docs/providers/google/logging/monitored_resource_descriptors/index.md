---
title: monitored_resource_descriptors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_resource_descriptors
  - logging
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
<tr><td><b>Id</b></td><td><code>google.logging.monitored_resource_descriptors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceDescriptors` | `array` | A list of resource descriptors. |
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then nextPageToken is included. To get the next set of results, call this method again using the value of nextPageToken as pageToken. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `monitored_resource_descriptors_list` | `SELECT` |  |
