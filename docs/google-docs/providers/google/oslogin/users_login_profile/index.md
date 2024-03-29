---
title: users_login_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - users_login_profile
  - oslogin
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
<tr><td><b>Name</b></td><td><code>users_login_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.oslogin.users_login_profile</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. A unique user ID. |
| `sshPublicKeys` | `object` | A map from SSH public key fingerprint to the associated key object. |
| `posixAccounts` | `array` | The list of POSIX accounts associated with the user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_login_profile` | `SELECT` | `usersId` |
