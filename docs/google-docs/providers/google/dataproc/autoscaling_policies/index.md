---
title: autoscaling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscaling_policies
  - dataproc
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
<tr><td><b>Name</b></td><td><code>autoscaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.autoscaling_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. This token is included in the response if there are more results to fetch. |
| `policies` | `array` | Output only. Autoscaling policies list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_autoscaling_policies_list` | `SELECT` | `locationsId, projectsId` | Lists autoscaling policies in the project. |
| `projects_regions_autoscaling_policies_list` | `SELECT` | `projectsId, regionsId` | Lists autoscaling policies in the project. |
| `projects_locations_autoscaling_policies_create` | `INSERT` | `locationsId, projectsId` | Creates new autoscaling policy. |
| `projects_regions_autoscaling_policies_create` | `INSERT` | `projectsId, regionsId` | Creates new autoscaling policy. |
| `projects_locations_autoscaling_policies_delete` | `DELETE` | `autoscalingPoliciesId, locationsId, projectsId` | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| `projects_regions_autoscaling_policies_delete` | `DELETE` | `autoscalingPoliciesId, projectsId, regionsId` | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| `projects_locations_autoscaling_policies_get` | `EXEC` | `autoscalingPoliciesId, locationsId, projectsId` | Retrieves autoscaling policy. |
| `projects_locations_autoscaling_policies_update` | `EXEC` | `autoscalingPoliciesId, locationsId, projectsId` | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
| `projects_regions_autoscaling_policies_get` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Retrieves autoscaling policy. |
| `projects_regions_autoscaling_policies_update` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
