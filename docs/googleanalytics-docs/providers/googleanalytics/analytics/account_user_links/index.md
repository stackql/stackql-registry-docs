---
title: account_user_links
hide_title: false
hide_table_of_contents: false
keywords:
  - account_user_links
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_user_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.account_user_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Entity user link ID |
| `selfLink` | `string` | Self link for this resource. |
| `userRef` | `object` | JSON template for a user reference. |
| `entity` | `object` | Entity for this link. It can be an account, a web property, or a view (profile). |
| `kind` | `string` | Resource type for entity user link. |
| `permissions` | `object` | Permissions the user has for this entity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_accountUserLinks_list` | `SELECT` | `accountId` | Lists account-user links for a given account. |
| `management_accountUserLinks_delete` | `DELETE` | `accountId, linkId` | Removes a user from the given account. |
| `management_accountUserLinks_insert` | `EXEC` | `accountId` | Adds a new user to the given account. |
| `management_accountUserLinks_update` | `EXEC` | `accountId, linkId` | Updates permissions for an existing user on the given account. |
