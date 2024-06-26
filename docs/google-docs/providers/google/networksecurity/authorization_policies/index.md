---
title: authorization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policies
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>authorization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.authorization_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the AuthorizationPolicy resource. It matches pattern `projects/&#123;project&#125;/locations/&#123;location&#125;/authorizationPolicies/`. |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="action" /> | `string` | Required. The action to take when a rule match is found. Possible values are "ALLOW" or "DENY". |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the AuthorizationPolicy resource. |
| <CopyableCode code="rules" /> | `array` | Optional. List of rules to match. Note that at least one of the rules must match in order for the action specified in the 'action' field to be taken. A rule is a match if there is a matching source and destination. If left blank, the action specified in the `action` field will be applied on every request. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_authorization_policies_get" /> | `SELECT` | <CopyableCode code="authorizationPoliciesId, locationsId, projectsId" /> | Gets details of a single AuthorizationPolicy. |
| <CopyableCode code="projects_locations_authorization_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists AuthorizationPolicies in a given project and location. |
| <CopyableCode code="projects_locations_authorization_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new AuthorizationPolicy in a given project and location. |
| <CopyableCode code="projects_locations_authorization_policies_delete" /> | `DELETE` | <CopyableCode code="authorizationPoliciesId, locationsId, projectsId" /> | Deletes a single AuthorizationPolicy. |
| <CopyableCode code="projects_locations_authorization_policies_patch" /> | `UPDATE` | <CopyableCode code="authorizationPoliciesId, locationsId, projectsId" /> | Updates the parameters of a single AuthorizationPolicy. |
| <CopyableCode code="_projects_locations_authorization_policies_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists AuthorizationPolicies in a given project and location. |
