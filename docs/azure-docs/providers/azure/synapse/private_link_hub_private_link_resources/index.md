---
title: private_link_hub_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_hub_private_link_resources
  - synapse
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
<tr><td><b>Name</b></td><td><code>private_link_hub_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_link_hub_private_link_resources" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateLinkHubName, privateLinkResourceName, resourceGroupName, subscriptionId" /> | Get private link resource in private link hub |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Get all private link resources for a private link hub |
