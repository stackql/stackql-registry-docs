---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"` |
| `locationId` | `string` | The canonical id for this location. For example: `"us-east1"`. |
| `metadata` | `object` | Service-specific metadata. For example the available capacity at the given location. |
| `displayName` | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| `labels` | `object` | Cross-service attributes for the location. For example &#123;"cloud.googleapis.com/region": "us-east1"&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId` | Gets information about a location. |
| `list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
| `_list` | `EXEC` | `projectsId` | Lists information about the supported locations for this service. |
