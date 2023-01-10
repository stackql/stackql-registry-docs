---
title: userinfo
hide_title: false
hide_table_of_contents: false
keywords:
  - userinfo
  - oauth2
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
<tr><td><b>Name</b></td><td><code>userinfo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.oauth2.userinfo</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The obfuscated ID of the user. |
| `name` | `string` | The user's full name. |
| `locale` | `string` | The user's preferred locale. |
| `picture` | `string` | URL of the user's picture image. |
| `link` | `string` | URL of the profile page. |
| `verified_email` | `boolean` | Boolean flag which is true if the email address is verified. Always verified because we only return the user's primary email address. |
| `email` | `string` | The user's email address. |
| `hd` | `string` | The hosted domain e.g. example.com if the user is Google apps user. |
| `family_name` | `string` | The user's last name. |
| `gender` | `string` | The user's gender. |
| `given_name` | `string` | The user's first name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` |  |
