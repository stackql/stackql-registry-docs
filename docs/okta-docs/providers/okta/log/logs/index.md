---
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
  - log
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
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.log.logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="actor" /> | `object` |
| <CopyableCode code="authenticationContext" /> | `object` |
| <CopyableCode code="client" /> | `object` |
| <CopyableCode code="debugContext" /> | `object` |
| <CopyableCode code="displayMessage" /> | `string` |
| <CopyableCode code="eventType" /> | `string` |
| <CopyableCode code="legacyEventType" /> | `string` |
| <CopyableCode code="outcome" /> | `object` |
| <CopyableCode code="published" /> | `string` |
| <CopyableCode code="request" /> | `object` |
| <CopyableCode code="securityContext" /> | `object` |
| <CopyableCode code="severity" /> | `string` |
| <CopyableCode code="target" /> | `array` |
| <CopyableCode code="transaction" /> | `object` |
| <CopyableCode code="uuid" /> | `string` |
| <CopyableCode code="version" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> |
