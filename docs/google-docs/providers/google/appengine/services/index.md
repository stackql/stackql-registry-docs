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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `services` | `array` | The services belonging to the requested application. |
| `nextPageToken` | `string` | Continuation token for fetching the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appsId, servicesId` | Gets the current configuration of the specified service. |
| `list` | `SELECT` | `appsId` | Lists all the services in the application. |
| `delete` | `DELETE` | `appsId, servicesId` | Deletes the specified service and all enclosed versions. |
| `patch` | `EXEC` | `appsId, servicesId` | Updates the configuration of the specified service. |
