---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this User. |
| `about` | `string` | Profile summary information. |
| `url` | `string` | The user's profile page. |
| `displayName` | `string` | The display name. |
| `locale` | `object` | This user's locale |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `blogs` | `object` | The container of blogs for this user. |
| `kind` | `string` | The kind of this entity. Always blogger#user. |
| `created` | `string` | The timestamp of when this profile was created, in seconds since epoch. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `userId` |
