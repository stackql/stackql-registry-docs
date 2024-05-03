---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - group
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="accessibility" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="credentials" /> | `object` |
| <CopyableCode code="features" /> | `array` |
| <CopyableCode code="label" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="licensing" /> | `object` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="settings" /> | `object` |
| <CopyableCode code="signOnMode" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="visibility" /> | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupId, subdomain" /> |
