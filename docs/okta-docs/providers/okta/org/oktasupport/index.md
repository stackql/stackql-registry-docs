---
title: oktasupport
hide_title: false
hide_table_of_contents: false
keywords:
  - oktasupport
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
<tr><td><b>Name</b></td><td><code>oktasupport</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.org.oktasupport" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="expiration" /> | `string` |
| <CopyableCode code="support" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subdomain" /> | Gets Okta Support Settings of your organization. |
| <CopyableCode code="extend" /> | `EXEC` | <CopyableCode code="subdomain" /> | Extends the length of time that Okta Support can access your org by 24 hours. This means that 24 hours are added to the remaining access time. |
| <CopyableCode code="grant" /> | `EXEC` | <CopyableCode code="subdomain" /> | Enables you to temporarily allow Okta Support to access your org as an administrator for eight hours. |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="subdomain" /> | Revokes Okta Support access to your organization. |
