---
title: blog_user_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - blog_user_infos
  - blogger
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>blog_user_infos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.blog_user_infos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `blog` | `object` |  |
| `blog_user_info` | `object` |  |
| `kind` | `string` | The kind of this entity. Always blogger#blogUserInfo. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `blogUserInfos_get` | `SELECT` | `blogId, userId` |
