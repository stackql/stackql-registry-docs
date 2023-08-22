---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of the group. Group names must be unique. They use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub&#125;/groups/&#123;group_id&#125;` |
| `description` | `string` | Optional. The description of the group. |
| `updateTime` | `string` | Output only. The time the group was last updated. |
| `createTime` | `string` | Output only. The time the group was created. |
| `labels` | `object` | Optional. Labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| `state` | `string` | Output only. The current lifecycle state of this group. |
| `uid` | `string` | Output only. The Google-generated UUID for the group. This value is unique across all group resources. If a group is deleted and another with the same name is created, the new route table is assigned a different unique_id. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupsId, hubsId, projectsId` | Gets details about a Network Connectivity Center group. |
| `list` | `SELECT` | `hubsId, projectsId` | Lists groups in a given hub. |
| `_list` | `EXEC` | `hubsId, projectsId` | Lists groups in a given hub. |
