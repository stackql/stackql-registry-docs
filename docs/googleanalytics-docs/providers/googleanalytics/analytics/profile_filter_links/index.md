---
title: profile_filter_links
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_filter_links
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
<tr><td><b>Name</b></td><td><code>profile_filter_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.profile_filter_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Profile filter link ID. |
| `selfLink` | `string` | Link for this profile filter link. |
| `filterRef` | `object` | JSON template for a profile filter link. |
| `kind` | `string` | Resource type for Analytics filter. |
| `profileRef` | `object` | JSON template for a linked view (profile). |
| `rank` | `integer` | The rank of this profile filter link relative to the other filters linked to the same profile.<br />For readonly (i.e., list and get) operations, the rank always starts at 1.<br />For write (i.e., create, update, or delete) operations, you may specify a value between 0 and 255 inclusively, [0, 255]. In order to insert a link at the end of the list, either don't specify a rank or set a rank to a number greater than the largest rank in the list. In order to insert a link to the beginning of the list specify a rank that is less than or equal to 1. The new link will move all existing filters with the same or lower rank down the list. After the link is inserted/updated/deleted all profile filter links will be renumbered starting at 1. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_profileFilterLinks_get` | `SELECT` | `accountId, linkId, profileId, webPropertyId` | Returns a single profile filter link. |
| `management_profileFilterLinks_list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists all profile filter links for a profile. |
| `management_profileFilterLinks_delete` | `DELETE` | `accountId, linkId, profileId, webPropertyId` | Delete a profile filter link. |
| `management_profileFilterLinks_insert` | `EXEC` | `accountId, profileId, webPropertyId` | Create a new profile filter link. |
| `management_profileFilterLinks_patch` | `EXEC` | `accountId, linkId, profileId, webPropertyId` | Update an existing profile filter link. This method supports patch semantics. |
| `management_profileFilterLinks_update` | `EXEC` | `accountId, linkId, profileId, webPropertyId` | Update an existing profile filter link. |
