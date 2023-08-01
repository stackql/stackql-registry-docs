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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `securityProfiles` | `array` | List of security profiles in the organization. The profiles may be attached or unattached to any environment. This will return latest revision of each profile. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_security_profiles_get` | `SELECT` | `organizationsId, securityProfilesId` | GetSecurityProfile gets the specified security profile. Returns NOT_FOUND if security profile is not present for the specified organization. |
| `organizations_security_profiles_list` | `SELECT` | `organizationsId` | ListSecurityProfiles lists all the security profiles associated with the org including attached and unattached profiles. |
