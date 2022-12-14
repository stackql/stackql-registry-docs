---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - clouderrorreporting
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
<tr><td><b>Id</b></td><td><code>google.clouderrorreporting.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The group resource name. Example: projects/my-project-123/groups/CNSgkpnppqKCUw |
| `trackingIssues` | `array` | Associated tracking issues. |
| `groupId` | `string` | Group IDs are unique for a given project. If the same kind of error occurs in different service contexts, it will receive the same group ID. |
| `resolutionStatus` | `string` | Error group's resolution status. An unspecified resolution status will be interpreted as OPEN |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_groups_get` | `SELECT` | `groupsId, projectsId` | Get the specified group. |
| `projects_groups_update` | `EXEC` | `groupsId, projectsId` | Replace the data for the specified group. Fails if the group does not exist. |
