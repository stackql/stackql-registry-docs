---
title: routers_nat_mapping_info
hide_title: false
hide_table_of_contents: false
keywords:
  - routers_nat_mapping_info
  - compute
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
<tr><td><b>Name</b></td><td><code>routers_nat_mapping_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.routers_nat_mapping_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `warning` | `object` | [Output Only] Informational warning message. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#vmEndpointNatMappingsList for lists of Nat mappings of VM endpoints. |
| `nextPageToken` | `string` | [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger than maxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. |
| `result` | `array` | [Output Only] A list of Nat mapping information of VM endpoints. |
| `selfLink` | `string` | [Output Only] Server-defined URL for this resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `routers_getNatMappingInfo` | `SELECT` | `project, region, router` |
