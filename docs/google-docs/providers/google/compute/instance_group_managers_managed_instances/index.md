---
title: instance_group_managers_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers_managed_instances
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
<tr><td><b>Name</b></td><td><code>instance_group_managers_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_group_managers_managed_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger than maxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. |
| `managedInstances` | `array` | [Output Only] The list of instances in the managed instance group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instanceGroupManagers_listManagedInstances` | `SELECT` | `instanceGroupManager, project, zone` |
