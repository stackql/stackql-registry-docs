---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - tokens
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.tokens.tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the token. |
| <CopyableCode code="name" /> | `string` | Name of the token. |
| <CopyableCode code="description" /> | `string` | Description of the token. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="status" /> | `string` | Status of the token. Can be `Active`, or `Inactive`. |
| <CopyableCode code="type" /> | `string` | Type of the token. Valid values: 1) CollectorRegistrationTokenResponse |
| <CopyableCode code="version" /> | `integer` | Version of the token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getToken" /> | `SELECT` | <CopyableCode code="id, region" /> | Get a token with the given identifier in the token library. |
| <CopyableCode code="listTokens" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all tokens in the token library. |
| <CopyableCode code="createToken" /> | `INSERT` | <CopyableCode code="data__name, data__status, data__type, region" /> | Create a token in the token library. |
| <CopyableCode code="deleteToken" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete a token with the given identifier in the token library. |
| <CopyableCode code="updateToken" /> | `EXEC` | <CopyableCode code="id, data__name, data__status, data__type, data__version, region" /> | Update a token with the given identifier in the token library. |
