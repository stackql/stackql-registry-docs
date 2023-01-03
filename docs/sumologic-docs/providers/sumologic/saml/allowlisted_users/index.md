---
title: allowlisted_users
hide_title: false
hide_table_of_contents: false
keywords:
  - allowlisted_users
  - saml
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>allowlisted_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.saml.allowlisted_users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `firstName` | `string` | First name of the user. |
| `isActive` | `boolean` | Checks if the user is active. |
| `lastLogin` | `string` | Timestamp of the last login of the user. |
| `lastName` | `string` | Last name of the user. |
| `userId` | `string` | Unique identifier of the user. |
| `canManageSaml` | `boolean` | If the user can manage SAML Configurations. |
| `email` | `string` | Email of the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getAllowlistedUsers` | `SELECT` |  | Get a list of allowlisted users. |
| `createAllowlistedUser` | `INSERT` | `userId` | Allowlist a user from SAML lockdown allowing them to sign in using a password in addition to SAML. |
| `deleteAllowlistedUser` | `DELETE` | `userId` | Remove an allowlisted user requiring them to sign in using SAML. |
