---
title: certs
hide_title: false
hide_table_of_contents: false
keywords:
  - certs
  - certs
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.certs.certs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="autoRenew" /> | `boolean` |
| <CopyableCode code="cns" /> | `array` |
| <CopyableCode code="createdAt" /> | `number` |
| <CopyableCode code="expiresAt" /> | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cert_by_id" /> | `SELECT` | <CopyableCode code="id, teamId" /> | Get cert by id |
| <CopyableCode code="remove_cert" /> | `DELETE` | <CopyableCode code="id, teamId" /> | Remove cert |
| <CopyableCode code="issue_cert" /> | `EXEC` | <CopyableCode code="teamId" /> | Issue a new cert |
| <CopyableCode code="upload_cert" /> | `EXEC` | <CopyableCode code="teamId, data__ca, data__cert, data__key" /> | Upload a cert |
