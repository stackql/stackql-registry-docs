---
title: post_user_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - post_user_infos
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
<tr><td><b>Name</b></td><td><code>post_user_infos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.post_user_infos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The kind of this entity. Always blogger#postUserInfo. |
| `post` | `object` |  |
| `post_user_info` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `postUserInfos_get` | `SELECT` | `blogId, postId, userId` | Gets one post and user info pair, by post_id and user_id. |
| `postUserInfos_list` | `SELECT` | `blogId, userId` | Lists post and user info pairs. |
