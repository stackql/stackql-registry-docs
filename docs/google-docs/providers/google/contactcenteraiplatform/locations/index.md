---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - contactcenteraiplatform
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
<tr><td><b>Id</b></td><td><code>google.contactcenteraiplatform.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `locations` | `array` | A list of locations that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId` | Gets information about a location. |
| `list` | `SELECT` | `projectsId` | Lists information about the supported locations for this service. |
| `query_contact_center_quota` | `EXEC` | `locationsId, projectsId` | Queries the contact center quota, an aggregation over all the projects, that belongs to the billing account, which the input project belongs to. |
