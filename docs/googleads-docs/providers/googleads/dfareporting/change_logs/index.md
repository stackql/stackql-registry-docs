---
title: change_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - change_logs
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>change_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.change_logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this change log. |
| `transactionId` | `string` | Transaction ID of this change log. When a single API call results in many changes, each change will have a separate ID in the change log but will share the same transactionId. |
| `userProfileId` | `string` | ID of the user who modified the object. |
| `objectType` | `string` | Object type of the change log. |
| `subaccountId` | `string` | Subaccount ID of the modified object. |
| `accountId` | `string` | Account ID of the modified object. |
| `changeTime` | `string` |  |
| `newValue` | `string` | New value of the object field. |
| `fieldName` | `string` | Field name of the object which changed. |
| `oldValue` | `string` | Old value of the object field. |
| `action` | `string` | Action which caused the change. |
| `userProfileName` | `string` | User profile name of the user who modified the object. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#changeLog". |
| `objectId` | `string` | ID of the object of this change log. The object could be a campaign, placement, ad, or other type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `changeLogs_get` | `SELECT` | `id, profileId` | Gets one change log by ID. |
| `changeLogs_list` | `SELECT` | `profileId` | Retrieves a list of change logs. This method supports paging. |
