---
title: available
hide_title: false
hide_table_of_contents: false
keywords:
  - available
  - domains
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
<tr><td><b>Name</b></td><td><code>available</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.domains.available" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="available" /> | `boolean` | Whether or not the domain name is available |
| <CopyableCode code="currency" /> | `string` | Currency in which the `price` is listed. Only returned if tld is offered |
| <CopyableCode code="definitive" /> | `boolean` | Whether or not the `available` answer has been definitively verified with the registry |
| <CopyableCode code="domain" /> | `string` | Domain name |
| <CopyableCode code="period" /> | `integer` | Number of years included in the price. Only returned if tld is offered |
| <CopyableCode code="price" /> | `integer` | Price of the domain excluding taxes or fees. Only returned if tld is offered |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="available" /> | `SELECT` | <CopyableCode code="domain" /> | Determine whether or not the specified domain is available for purchase |
| <CopyableCode code="available_bulk" /> | `EXEC` |  | Determine whether or not the specified domains are available for purchase |
