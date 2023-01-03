---
title: security_profiles_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles_revisions
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
<tr><td><b>Name</b></td><td><code>security_profiles_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.security_profiles_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `securityProfiles` | `array` | List of security profile revisions. The revisions may be attached or unattached to any environment. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_securityProfiles_listRevisions` | `SELECT` | `organizationsId, securityProfilesId` |
