---
title: instance_group_managers_errors
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers_errors
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
<tr><td><b>Name</b></td><td><code>instance_group_managers_errors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_group_managers_errors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `error` | `object` |  |
| `instanceActionDetails` | `object` |  |
| `timestamp` | `string` | [Output Only] The time that this error occurred. This value is in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instanceGroupManagers_listErrors` | `SELECT` | `instanceGroupManager, project, zone` |
