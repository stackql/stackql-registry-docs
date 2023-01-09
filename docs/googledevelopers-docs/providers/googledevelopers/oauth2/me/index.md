---
title: me
hide_title: false
hide_table_of_contents: false
keywords:
  - me
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
<tr><td><b>Name</b></td><td><code>me</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.oauth2.me</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The obfuscated ID of the user. |
| `name` | `string` | The user's full name. |
| `locale` | `string` | The user's preferred locale. |
| `email` | `string` | The user's email address. |
| `gender` | `string` | The user's gender. |
| `link` | `string` | URL of the profile page. |
| `family_name` | `string` | The user's last name. |
| `hd` | `string` | The hosted domain e.g. example.com if the user is Google apps user. |
| `picture` | `string` | URL of the user's picture image. |
| `given_name` | `string` | The user's first name. |
| `verified_email` | `boolean` | Boolean flag which is true if the email address is verified. Always verified because we only return the user's primary email address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `userinfo_v2_me_get` | `SELECT` |  |
