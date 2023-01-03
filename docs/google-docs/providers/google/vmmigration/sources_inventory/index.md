---
title: sources_inventory
hide_title: false
hide_table_of_contents: false
keywords:
  - sources_inventory
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>sources_inventory</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.sources_inventory</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `vmwareVms` | `object` | VmwareVmsDetails describes VMs in vCenter. |
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `updateTime` | `string` | Output only. The timestamp when the source was last queried (if the result is from the cache). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_sources_fetchInventory` | `SELECT` | `locationsId, projectsId, sourcesId` |
