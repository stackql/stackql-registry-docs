---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
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
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="networksecurity.security_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. Name of the SecurityProfile resource. It matches pattern `projects\|organizations/*/locations/&#123;location&#125;/securityProfiles/&#123;security_profile&#125;`. |
| <CopyableCode code="description" /> | `string` | Optional. An optional description of the profile. Max length 512 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Resource creation timestamp. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs. |
| <CopyableCode code="threatPreventionProfile" /> | `object` | ThreatPreventionProfile defines an action for specific threat signatures or severity levels. |
| <CopyableCode code="type" /> | `string` | Immutable. The single ProfileType that the SecurityProfile resource configures. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last resource update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_security_profiles_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, securityProfilesId" /> | Gets details of a single SecurityProfile. |
| <CopyableCode code="organizations_locations_security_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists SecurityProfiles in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profiles_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new SecurityProfile in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profiles_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, securityProfilesId" /> | Deletes a single SecurityProfile. |
| <CopyableCode code="_organizations_locations_security_profiles_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists SecurityProfiles in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profiles_patch" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, securityProfilesId" /> | Updates the parameters of a single SecurityProfile. |
