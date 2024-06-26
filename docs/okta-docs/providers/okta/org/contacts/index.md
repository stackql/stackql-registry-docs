---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
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
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.org.contacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="contactType" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactType, subdomain" /> | Retrieves the URL of the User associated with the specified Contact Type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Gets Contact Types of your organization. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="contactType, subdomain" /> | Updates the User associated with the specified Contact Type. |
