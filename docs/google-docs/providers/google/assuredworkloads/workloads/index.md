---
title: workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads
  - assuredworkloads
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
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.assuredworkloads.workloads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The next page token. Return empty if reached the last page. |
| `workloads` | `array` | List of Workloads under a given parent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, organizationsId, workloadsId` | Gets Assured Workload associated with a CRM Node |
| `list` | `SELECT` | `locationsId, organizationsId` | Lists Assured Workloads under a CRM Node. |
| `create` | `INSERT` | `locationsId, organizationsId` | Creates Assured Workload. |
| `delete` | `DELETE` | `locationsId, organizationsId, workloadsId` | Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error. In addition to assuredworkloads.workload.delete permission, the user should also have orgpolicy.policy.set permission on the deleted folder to remove Assured Workloads OrgPolicies. |
| `mutate_partner_permissions` | `EXEC` | `locationsId, organizationsId, workloadsId` | Update the permissions settings for an existing partner workload. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |
| `patch` | `EXEC` | `locationsId, organizationsId, workloadsId` | Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress. |
| `restrict_allowed_resources` | `EXEC` | `locationsId, organizationsId, workloadsId` | Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at https://cloud.google.com/assured-workloads/docs/supported-products In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality. |
