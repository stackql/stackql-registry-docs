---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - logging
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name for the location, which may vary between implementations. For example: "projects/example-project/locations/us-east1" |
| `locationId` | `string` | The canonical id for this location. For example: "us-east1". |
| `metadata` | `object` | Service-specific metadata. For example the available capacity at the given location. |
| `displayName` | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| `labels` | `object` | Cross-service attributes for the location. For example {"cloud.googleapis.com/region": "us-east1"}  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_get` | `SELECT` | `billingAccountsId, locationsId` | Gets information about a location. |
| `billingAccounts_locations_list` | `SELECT` | `billingAccountsId` | Lists information about the supported locations for this service. |
| `folders_locations_get` | `SELECT` | `foldersId, locationsId` | Gets information about a location. |
| `folders_locations_list` | `SELECT` | `foldersId` | Lists information about the supported locations for this service. |
| `list` | `SELECT` | `name` | Lists information about the supported locations for this service. |
| `organizations_locations_get` | `SELECT` | `locationsId, organizationsId` | Gets information about a location. |
| `organizations_locations_list` | `SELECT` | `organizationsId` | Lists information about the supported locations for this service. |
| `projects_locations_get` | `SELECT` | `locationsId, projectsId` | Gets information about a location. |
| `projects_locations_list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
