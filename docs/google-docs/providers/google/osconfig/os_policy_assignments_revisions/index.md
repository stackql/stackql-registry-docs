---
title: os_policy_assignments_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - os_policy_assignments_revisions
  - osconfig
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
<tr><td><b>Name</b></td><td><code>os_policy_assignments_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.os_policy_assignments_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `osPolicyAssignments` | `array` | The OS policy assignment revisions |
| `nextPageToken` | `string` | The pagination token to retrieve the next page of OS policy assignment revisions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_revisions` | `SELECT` | `locationsId, osPolicyAssignmentsId, projectsId` |
