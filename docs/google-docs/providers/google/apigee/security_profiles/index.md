---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
  - apigee
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
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.security_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Name of the security profile resource. Format: organizations/{org}/securityProfiles/{profile} |
| `revisionUpdateTime` | `string` | Output only. The time when revision was updated. |
| `maxScore` | `integer` | Output only. Maximum security score that can be generated by this profile. |
| `revisionCreateTime` | `string` | Output only. The time when revision was created. |
| `scoringConfigs` | `array` | List of profile scoring configs in this revision. |
| `revisionId` | `string` | Output only. Revision ID of the security profile. |
| `displayName` | `string` | Display name of the security profile. |
| `environments` | `array` | List of environments attached to security profile. |
| `revisionPublishTime` | `string` | Output only. The time when revision was published. Once published, the security profile revision cannot be updated further and can be attached to environments. |
| `minScore` | `integer` | Output only. Minimum security score that can be generated by this profile. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_securityProfiles_get` | `SELECT` | `organizationsId, securityProfilesId` | GetSecurityProfile gets the specified security profile. Returns NOT_FOUND if security profile is not present for the specified organization. |
| `organizations_securityProfiles_list` | `SELECT` | `organizationsId` | ListSecurityProfiles lists all the security profiles associated with the org including attached and unattached profiles. |