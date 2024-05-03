---
title: asps
hide_title: false
hide_table_of_contents: false
keywords:
  - asps
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
<tr><td><b>Name</b></td><td><code>asps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.asps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the application that the user, represented by their `userId`, entered when the ASP was created. |
| <CopyableCode code="codeId" /> | `integer` | The unique ID of the ASP. |
| <CopyableCode code="creationTime" /> | `string` | The time when the ASP was created. Expressed in [Unix time](https://en.wikipedia.org/wiki/Epoch_time) format. |
| <CopyableCode code="etag" /> | `string` | ETag of the ASP. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. This is always `admin#directory#asp`. |
| <CopyableCode code="lastTimeUsed" /> | `string` | The time when the ASP was last used. Expressed in [Unix time](https://en.wikipedia.org/wiki/Epoch_time) format. |
| <CopyableCode code="userKey" /> | `string` | The unique ID of the user who issued the ASP. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="codeId, userKey" /> | Gets information about an ASP issued by a user. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="userKey" /> | Lists the ASPs issued by a user. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="codeId, userKey" /> | Deletes an ASP issued by a user. |
