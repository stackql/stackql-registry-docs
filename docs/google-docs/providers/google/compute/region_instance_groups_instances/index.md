---
title: region_instance_groups_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_groups_instances
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
<tr><td><b>Name</b></td><td><code>region_instance_groups_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_instance_groups_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | [Output Only] The status of the instance. |
| `instance` | `string` | [Output Only] The URL of the instance. |
| `namedPorts` | `array` | [Output Only] The named ports that belong to this instance group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `regionInstanceGroups_listInstances` | `SELECT` | `instanceGroup, project, region` |
