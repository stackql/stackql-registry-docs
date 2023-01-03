---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - recaptchaenterprise
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
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recaptchaenterprise.memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `relatedAccountGroupMemberships` | `array` | The memberships listed by the query. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_relatedaccountgroups_memberships_list` | `SELECT` | `projectsId, relatedaccountgroupsId` |
