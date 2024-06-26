---
title: generate
hide_title: false
hide_table_of_contents: false
keywords:
  - generate
  - video_indexer
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>generate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.video_indexer.generate" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="access_token" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__permissionType, data__scope" /> | Generate an Azure Video Indexer access token. |
| <CopyableCode code="restricted_viewer_access_token" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__scope" /> | Generate an Azure Video Indexer restricted viewer access token. |
