---
title: xpn_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - xpn_resources
  - compute
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
<tr><td><b>Name</b></td><td><code>xpn_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.xpn_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resources` | `array` | Service resources (a.k.a service projects) attached to this project as their shared VPC host. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#projectsGetXpnResources for lists of service resources (a.k.a service projects) |
| `nextPageToken` | `string` | [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger than maxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_xpn_resources` | `SELECT` | `project` |
