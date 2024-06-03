---
title: security_profile_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profile_groups
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
<tr><td><b>Name</b></td><td><code>security_profile_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.security_profile_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern `projects\|organizations/*/locations/&#123;location&#125;/securityProfileGroups/&#123;security_profile_group&#125;`. |
| <CopyableCode code="description" /> | `string` | Optional. An optional description of the profile group. Max length 2048 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Resource creation timestamp. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs. |
| <CopyableCode code="threatPreventionProfile" /> | `string` | Optional. Reference to a SecurityProfile with the threat prevention configuration for the SecurityProfileGroup. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last resource update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_security_profile_groups_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, securityProfileGroupsId" /> | Gets details of a single SecurityProfileGroup. |
| <CopyableCode code="organizations_locations_security_profile_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists SecurityProfileGroups in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profile_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new SecurityProfileGroup in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profile_groups_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, securityProfileGroupsId" /> | Deletes a single SecurityProfileGroup. |
| <CopyableCode code="organizations_locations_security_profile_groups_patch" /> | `UPDATE` | <CopyableCode code="locationsId, organizationsId, securityProfileGroupsId" /> | Updates the parameters of a single SecurityProfileGroup. |
| <CopyableCode code="_organizations_locations_security_profile_groups_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists SecurityProfileGroups in a given organization and location. |
