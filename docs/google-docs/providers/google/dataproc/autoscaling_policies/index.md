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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `id` | `string` | Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. |
| `name` | `string` | Output only. The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id} For projects.locations.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id} |
| `workerConfig` | `object` | Configuration for the size bounds of an instance group, including its proportional size to other groups. |
| `basicAlgorithm` | `object` | Basic algorithm for autoscaling. |
| `labels` | `object` | Optional. The labels to associate with this autoscaling policy. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with an autoscaling policy. |
| `secondaryWorkerConfig` | `object` | Configuration for the size bounds of an instance group, including its proportional size to other groups. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_autoscalingPolicies_get` | `SELECT` | `autoscalingPoliciesId, locationsId, projectsId` | Retrieves autoscaling policy. |
| `projects_locations_autoscalingPolicies_list` | `SELECT` | `locationsId, projectsId` | Lists autoscaling policies in the project. |
| `projects_regions_autoscalingPolicies_get` | `SELECT` | `autoscalingPoliciesId, projectsId, regionsId` | Retrieves autoscaling policy. |
| `projects_regions_autoscalingPolicies_list` | `SELECT` | `projectsId, regionsId` | Lists autoscaling policies in the project. |
| `projects_locations_autoscalingPolicies_create` | `INSERT` | `locationsId, projectsId` | Creates new autoscaling policy. |
| `projects_regions_autoscalingPolicies_create` | `INSERT` | `projectsId, regionsId` | Creates new autoscaling policy. |
| `projects_locations_autoscalingPolicies_delete` | `DELETE` | `autoscalingPoliciesId, locationsId, projectsId` | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| `projects_regions_autoscalingPolicies_delete` | `DELETE` | `autoscalingPoliciesId, projectsId, regionsId` | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| `projects_locations_autoscalingPolicies_update` | `EXEC` | `autoscalingPoliciesId, locationsId, projectsId` | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
| `projects_regions_autoscalingPolicies_update` | `EXEC` | `autoscalingPoliciesId, projectsId, regionsId` | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
