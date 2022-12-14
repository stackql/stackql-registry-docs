---
title: region_instance_group_managers__managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_group_managers__managed_instances
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
<tr><td><b>Name</b></td><td><code>region_instance_group_managers__managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_instance_group_managers__managed_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedInstances` | `array` | A list of managed instances. |
| `nextPageToken` | `string` | [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger than maxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `regionInstanceGroupManagers_listManagedInstances` | `SELECT` | `instanceGroupManager, project, region` |
