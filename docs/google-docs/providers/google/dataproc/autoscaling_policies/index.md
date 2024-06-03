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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autoscaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.autoscaling_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. |
| <CopyableCode code="name" /> | `string` | Output only. The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.autoscalingPolicies, the resource name of the policy has the following format: projects/&#123;project_id&#125;/regions/&#123;region&#125;/autoscalingPolicies/&#123;policy_id&#125; For projects.locations.autoscalingPolicies, the resource name of the policy has the following format: projects/&#123;project_id&#125;/locations/&#123;location&#125;/autoscalingPolicies/&#123;policy_id&#125; |
| <CopyableCode code="basicAlgorithm" /> | `object` | Basic algorithm for autoscaling. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this autoscaling policy. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with an autoscaling policy. |
| <CopyableCode code="secondaryWorkerConfig" /> | `object` | Configuration for the size bounds of an instance group, including its proportional size to other groups. |
| <CopyableCode code="workerConfig" /> | `object` | Configuration for the size bounds of an instance group, including its proportional size to other groups. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_autoscaling_policies_get" /> | `SELECT` | <CopyableCode code="autoscalingPoliciesId, locationsId, projectsId" /> | Retrieves autoscaling policy. |
| <CopyableCode code="projects_locations_autoscaling_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists autoscaling policies in the project. |
| <CopyableCode code="projects_regions_autoscaling_policies_get" /> | `SELECT` | <CopyableCode code="autoscalingPoliciesId, projectsId, regionsId" /> | Retrieves autoscaling policy. |
| <CopyableCode code="projects_regions_autoscaling_policies_list" /> | `SELECT` | <CopyableCode code="projectsId, regionsId" /> | Lists autoscaling policies in the project. |
| <CopyableCode code="projects_locations_autoscaling_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates new autoscaling policy. |
| <CopyableCode code="projects_regions_autoscaling_policies_create" /> | `INSERT` | <CopyableCode code="projectsId, regionsId" /> | Creates new autoscaling policy. |
| <CopyableCode code="projects_locations_autoscaling_policies_delete" /> | `DELETE` | <CopyableCode code="autoscalingPoliciesId, locationsId, projectsId" /> | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| <CopyableCode code="projects_regions_autoscaling_policies_delete" /> | `DELETE` | <CopyableCode code="autoscalingPoliciesId, projectsId, regionsId" /> | Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters. |
| <CopyableCode code="projects_locations_autoscaling_policies_update" /> | `UPDATE` | <CopyableCode code="autoscalingPoliciesId, locationsId, projectsId" /> | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
| <CopyableCode code="projects_regions_autoscaling_policies_update" /> | `UPDATE` | <CopyableCode code="autoscalingPoliciesId, projectsId, regionsId" /> | Updates (replaces) autoscaling policy.Disabled check for update_mask, because all updates will be full replacements. |
| <CopyableCode code="_projects_locations_autoscaling_policies_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists autoscaling policies in the project. |
| <CopyableCode code="_projects_regions_autoscaling_policies_list" /> | `EXEC` | <CopyableCode code="projectsId, regionsId" /> | Lists autoscaling policies in the project. |
