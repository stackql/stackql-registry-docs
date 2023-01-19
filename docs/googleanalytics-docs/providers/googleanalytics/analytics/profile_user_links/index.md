---
title: profile_user_links
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_user_links
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
<tr><td><b>Name</b></td><td><code>profile_user_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.profile_user_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Entity user link ID |
| `kind` | `string` | Resource type for entity user link. |
| `permissions` | `object` | Permissions the user has for this entity. |
| `selfLink` | `string` | Self link for this resource. |
| `userRef` | `object` | JSON template for a user reference. |
| `entity` | `object` | Entity for this link. It can be an account, a web property, or a view (profile). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_profileUserLinks_list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists profile-user links for a given view (profile). |
| `management_profileUserLinks_delete` | `DELETE` | `accountId, linkId, profileId, webPropertyId` | Removes a user from the given view (profile). |
| `management_profileUserLinks_insert` | `EXEC` | `accountId, profileId, webPropertyId` | Adds a new user to the given view (profile). |
| `management_profileUserLinks_update` | `EXEC` | `accountId, linkId, profileId, webPropertyId` | Updates permissions for an existing user on the given view (profile). |
