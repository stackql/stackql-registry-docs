---
title: oktacommunication
hide_title: false
hide_table_of_contents: false
keywords:
  - oktacommunication
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
<tr><td><b>Name</b></td><td><code>oktacommunication</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.org.oktacommunication" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="optOutEmailUsers" /> | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subdomain" /> | Gets Okta Communication Settings of your organization. |
| <CopyableCode code="optIn" /> | `EXEC` | <CopyableCode code="subdomain" /> | Opts in all users of this org to Okta Communication emails. |
| <CopyableCode code="optOut" /> | `EXEC` | <CopyableCode code="subdomain" /> | Opts out all users of this org from Okta Communication emails. |
