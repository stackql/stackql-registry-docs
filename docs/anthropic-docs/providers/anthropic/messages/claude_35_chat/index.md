---
title: claude_35_chat
hide_title: false
hide_table_of_contents: false
keywords:
  - claude_35_chat
  - messages
  - anthropic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Anthropic resources using SQL.
custom_edit_url: null
image: /img/providers/anthropic/stackql-anthropic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>claude_35_chat</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="anthropic.messages.claude_35_chat" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/anthropic/v00.00.00000/services/messages.yaml), located under `components -> x-stackQL-resources -> claude_35_chat`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="content" /> ||
| <CopyableCode code="input_tokens" /> | `text` |
| <CopyableCode code="model" /> | `text` |
| <CopyableCode code="output_tokens" /> | `text` |
| <CopyableCode code="role" /> | `text` |
| <CopyableCode code="stop_reason" /> | `text` |
| <CopyableCode code="stop_sequence" /> | `text` |
## Methods
No additional methods available for this resource
