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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `displayName` | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| `labels` | `object` | Cross-service attributes for the location. For example &#123;"cloud.googleapis.com/region": "us-east1"&#125;  |
| `locationId` | `string` | The canonical id for this location. For example: "us-east1". |
| `metadata` | `object` | Service-specific metadata. For example the available capacity at the given location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_get` | `SELECT` | `billingAccountsId, locationsId` | Gets information about a location. |
| `billing_accounts_locations_list` | `SELECT` | `billingAccountsId` | Lists information about the supported locations for this service. |
| `folders_locations_get` | `SELECT` | `foldersId, locationsId` | Gets information about a location. |
| `folders_locations_list` | `SELECT` | `foldersId` | Lists information about the supported locations for this service. |
| `locations_list` | `SELECT` | `name` | Lists information about the supported locations for this service. |
| `organizations_locations_get` | `SELECT` | `locationsId, organizationsId` | Gets information about a location. |
| `organizations_locations_list` | `SELECT` | `organizationsId` | Lists information about the supported locations for this service. |
| `projects_locations_get` | `SELECT` | `locationsId, projectsId` | Gets information about a location. |
| `projects_locations_list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
| `_billing_accounts_locations_list` | `EXEC` | `billingAccountsId` | Lists information about the supported locations for this service. |
| `_folders_locations_list` | `EXEC` | `foldersId` | Lists information about the supported locations for this service. |
| `_locations_list` | `EXEC` | `name` | Lists information about the supported locations for this service. |
| `_organizations_locations_list` | `EXEC` | `organizationsId` | Lists information about the supported locations for this service. |
| `_projects_locations_list` | `EXEC` | `projectsId` | Lists information about the supported locations for this service. |
