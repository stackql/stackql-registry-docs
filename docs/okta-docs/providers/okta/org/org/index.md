---
title: org
hide_title: false
hide_table_of_contents: false
keywords:
  - org
  - org
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
<tr><td><b>Name</b></td><td><code>org</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.org.org" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="address1" /> | `string` |
| <CopyableCode code="address2" /> | `string` |
| <CopyableCode code="city" /> | `string` |
| <CopyableCode code="companyName" /> | `string` |
| <CopyableCode code="country" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="endUserSupportHelpURL" /> | `string` |
| <CopyableCode code="expiresAt" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="phoneNumber" /> | `string` |
| <CopyableCode code="postalCode" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="subdomain" /> | `string` |
| <CopyableCode code="supportPhoneNumber" /> | `string` |
| <CopyableCode code="website" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subdomain" /> | Get settings of your organization. |
| <CopyableCode code="partialUpdate" /> | `EXEC` | <CopyableCode code="subdomain" /> | Partial update settings of your organization. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="subdomain" /> | Update settings of your organization. |
