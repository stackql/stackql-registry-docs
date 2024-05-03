---
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
  - agreements
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.agreements.agreements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agreementKey" /> | `string` | Unique identifier for the legal agreement |
| <CopyableCode code="content" /> | `string` | Contents of the legal agreement, suitable for embedding |
| <CopyableCode code="title" /> | `string` | Title of the legal agreement |
| <CopyableCode code="url" /> | `string` | URL to a page containing the legal agreement |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keys" /> |
