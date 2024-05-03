---
title: subdomain
hide_title: false
hide_table_of_contents: false
keywords:
  - subdomain
  - account
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
<tr><td><b>Name</b></td><td><code>subdomain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.account.subdomain" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format.<br /> |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="subdomain" /> | `string` | The new subdomain. |
| <CopyableCode code="url" /> | `string` | Login URL corresponding to the subdomain. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getSubdomain" /> | `SELECT` | <CopyableCode code="region" /> | Get the configured subdomain. |
| <CopyableCode code="createSubdomain" /> | `INSERT` | <CopyableCode code="data__subdomain, region" /> | Create a subdomain. Only the Account Owner can create a subdomain. |
| <CopyableCode code="deleteSubdomain" /> | `DELETE` | <CopyableCode code="region" /> | Delete the configured subdomain. |
| <CopyableCode code="updateSubdomain" /> | `EXEC` | <CopyableCode code="data__subdomain, region" /> | Update a subdomain. Only the Account Owner can update the subdomain. |
