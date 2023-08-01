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
| `locations` | `array` | A list of locations that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_list` | `SELECT` | `billingAccountsId` | Lists information about the supported locations for this service. |
| `folders_locations_list` | `SELECT` | `foldersId` | Lists information about the supported locations for this service. |
| `locations_list` | `SELECT` | `name` | Lists information about the supported locations for this service. |
| `organizations_locations_list` | `SELECT` | `organizationsId` | Lists information about the supported locations for this service. |
| `projects_locations_list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
| `billing_accounts_locations_get` | `EXEC` | `billingAccountsId, locationsId` | Gets information about a location. |
| `folders_locations_get` | `EXEC` | `foldersId, locationsId` | Gets information about a location. |
| `organizations_locations_get` | `EXEC` | `locationsId, organizationsId` | Gets information about a location. |
| `projects_locations_get` | `EXEC` | `locationsId, projectsId` | Gets information about a location. |
