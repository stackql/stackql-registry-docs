---
title: registrations_importable_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations_importable_domains
  - domains
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
<tr><td><b>Name</b></td><td><code>registrations_importable_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.domains.registrations_importable_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `domains` | `array` | A list of domains that the calling user manages in Google Domains. |
| `nextPageToken` | `string` | When present, there are more results to retrieve. Set `page_token` to this value on a subsequent call to get the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_registrations_retrieveImportableDomains` | `SELECT` | `locationsId, projectsId` |
