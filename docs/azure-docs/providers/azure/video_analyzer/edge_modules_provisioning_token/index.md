---
title: edge_modules_provisioning_token
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_modules_provisioning_token
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>edge_modules_provisioning_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.edge_modules_provisioning_token" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expirationDate" /> | `string` | The expiration date of the registration token. The Azure Video Analyzer IoT edge module must be initialized and connected to the Internet prior to the token expiration date. |
| <CopyableCode code="token" /> | `string` | The token blob to be provided to the Azure Video Analyzer IoT edge module through the Azure IoT Edge module twin properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, edgeModuleName, resourceGroupName, subscriptionId, data__expirationDate" /> |
