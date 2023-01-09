---
title: webproperty_user_links
hide_title: false
hide_table_of_contents: false
keywords:
  - webproperty_user_links
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
<tr><td><b>Name</b></td><td><code>webproperty_user_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.webproperty_user_links</code></td></tr>
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
| `management_webpropertyUserLinks_list` | `SELECT` | `accountId, webPropertyId` | Lists webProperty-user links for a given web property. |
| `management_webpropertyUserLinks_delete` | `DELETE` | `accountId, linkId, webPropertyId` | Removes a user from the given web property. |
| `management_webpropertyUserLinks_insert` | `EXEC` | `accountId, webPropertyId` | Adds a new user to the given web property. |
| `management_webpropertyUserLinks_update` | `EXEC` | `accountId, linkId, webPropertyId` | Updates permissions for an existing user on the given web property. |
