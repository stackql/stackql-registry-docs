---
title: status
hide_title: false
hide_table_of_contents: false
keywords:
  - status
  - service_allowlist
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
<tr><td><b>Name</b></td><td><code>status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.service_allowlist.status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentEnabled" /> | `boolean` | Whether service allowlisting is enabled for Content. |
| <CopyableCode code="loginEnabled" /> | `boolean` | Whether service allowlisting is enabled for Login. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getAllowlistingStatus" /> | `SELECT` | <CopyableCode code="region" /> |
