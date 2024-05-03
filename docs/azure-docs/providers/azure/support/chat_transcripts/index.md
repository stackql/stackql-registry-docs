---
title: chat_transcripts
hide_title: false
hide_table_of_contents: false
keywords:
  - chat_transcripts
  - support
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chat_transcripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.chat_transcripts" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="chatTranscriptName, subscriptionId, supportTicketName" /> | Returns chatTranscript details for a support ticket under a subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId, supportTicketName" /> | Lists all chat transcripts for a support ticket under subscription |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId, supportTicketName" /> | Lists all chat transcripts for a support ticket under subscription |
