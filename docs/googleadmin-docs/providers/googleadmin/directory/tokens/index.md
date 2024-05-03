---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="anonymous" /> | `boolean` | Whether the application is registered with Google. The value is `true` if the application has an anonymous Client ID. |
| <CopyableCode code="clientId" /> | `string` | The Client ID of the application the token is issued to. |
| <CopyableCode code="displayText" /> | `string` | The displayable name of the application the token is issued to. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. This is always `admin#directory#token`. |
| <CopyableCode code="nativeApp" /> | `boolean` | Whether the token is issued to an installed application. The value is `true` if the application is installed to a desktop or mobile device. |
| <CopyableCode code="scopes" /> | `array` | A list of authorization scopes the application is granted. |
| <CopyableCode code="userKey" /> | `string` | The unique ID of the user that issued the token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clientId, userKey" /> | Gets information about an access token issued by a user. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="userKey" /> | Returns the set of tokens specified user has issued to 3rd party applications. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clientId, userKey" /> | Deletes all access tokens issued by a user for an application. |
