---
title: user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles
  - classroom
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.classroom.user_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the user. Read-only. |
| `name` | `object` | Details of the user's name. |
| `verifiedTeacher` | `boolean` | Represents whether a G Suite for Education user's domain administrator has explicitly verified them as being a teacher. If the user is not a member of a G Suite for Education domain, than this field is always false. Read-only |
| `emailAddress` | `string` | Email address of the user. Read-only. |
| `permissions` | `array` | Global permissions of the user. Read-only. |
| `photoUrl` | `string` | URL of user's profile photo. Read-only. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `userProfiles_get` | `SELECT` | `userId` |
