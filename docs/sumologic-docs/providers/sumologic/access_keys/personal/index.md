---
title: personal
hide_title: false
hide_table_of_contents: false
keywords:
  - personal
  - access_keys
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>personal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.access_keys.personal" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the access key. |
| <CopyableCode code="corsHeaders" /> | `array` | An array of domains for which the access key is valid. Whether Sumo Logic accepts or rejects an API request depends on whether it contains an ORIGIN header and the entries in the allowlist. Sumo Logic will reject:<br />  1. Requests with an ORIGIN header but the allowlist is empty.<br />  2. Requests with an ORIGIN header that don't match any entry in the allowlist. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the access key. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates whether the access key is disabled or not. |
| <CopyableCode code="label" /> | `string` | The name of the access key. |
| <CopyableCode code="lastUsed" /> | `string` | Last used timestamp in UTC.  &lt;br&gt; **Note:** Property not in use, it is part of an upcoming feature. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listPersonalAccessKeys" /> | `SELECT` | <CopyableCode code="region" /> |
