---
title: groups_security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_security_settings
  - cloudidentity
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
<tr><td><b>Name</b></td><td><code>groups_security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.groups_security_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the security settings. Shall be of the form `groups/{group_id}/securitySettings`. |
| `memberRestriction` | `object` | The definition of MemberRestriction |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `groups_getSecuritySettings` | `SELECT` | `groupsId` |
