---
title: eventhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - eventhooks
  - eventhook
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
<tr><td><b>Name</b></td><td><code>eventhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.eventhook.eventhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="channel" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="createdBy" /> | `string` |
| <CopyableCode code="events" /> | `object` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="verificationStatus" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventHookId, subdomain" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventHookId, subdomain" /> |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="eventHookId, subdomain" /> |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="eventHookId, subdomain" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="eventHookId, subdomain" /> |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="eventHookId, subdomain" /> |
