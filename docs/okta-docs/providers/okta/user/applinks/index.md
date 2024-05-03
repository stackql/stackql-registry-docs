---
title: applinks
hide_title: false
hide_table_of_contents: false
keywords:
  - applinks
  - user
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.applinks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="appAssignmentId" /> | `string` |
| <CopyableCode code="appInstanceId" /> | `string` |
| <CopyableCode code="appName" /> | `string` |
| <CopyableCode code="credentialsSetup" /> | `boolean` |
| <CopyableCode code="hidden" /> | `boolean` |
| <CopyableCode code="label" /> | `string` |
| <CopyableCode code="linkUrl" /> | `string` |
| <CopyableCode code="logoUrl" /> | `string` |
| <CopyableCode code="sortOrder" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="userId, subdomain" /> |
