---
title: tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - tracks
  - media_services
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
<tr><td><b>Name</b></td><td><code>tracks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.tracks" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName" /> | Get the details of a Track in the Asset |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId" /> | Lists the Tracks in the asset |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName" /> | Create or update a Track in the asset |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName" /> | Deletes a Track in the asset |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId" /> | Lists the Tracks in the asset |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId, trackName" /> | Updates an existing Track in the asset |
