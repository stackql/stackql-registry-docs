---
title: bgp_peers
hide_title: false
hide_table_of_contents: false
keywords:
  - bgp_peers
  - kubernetesruntime
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
<tr><td><b>Name</b></td><td><code>bgp_peers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesruntime.bgp_peers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bgpPeerName, resourceUri" /> | Get a BgpPeer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List BgpPeer resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bgpPeerName, resourceUri" /> | Create a BgpPeer |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bgpPeerName, resourceUri" /> | Delete a BgpPeer |
