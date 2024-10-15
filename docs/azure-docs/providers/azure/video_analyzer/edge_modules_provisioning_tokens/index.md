---
title: edge_modules_provisioning_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_modules_provisioning_tokens
  - video_analyzer
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>edge_modules_provisioning_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_modules_provisioning_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.edge_modules_provisioning_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expirationDate" /> | `string` | The expiration date of the registration token. The Azure Video Analyzer IoT edge module must be initialized and connected to the Internet prior to the token expiration date. |
| <CopyableCode code="token" /> | `string` | The token blob to be provided to the Azure Video Analyzer IoT edge module through the Azure IoT Edge module twin properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, edgeModuleName, resourceGroupName, subscriptionId, data__expirationDate" /> | Creates a new provisioning token. A provisioning token allows for a single instance of Azure Video analyzer IoT edge module to be initialized and authorized to the cloud account. The provisioning token itself is short lived and it is only used for the initial handshake between IoT edge module and the cloud. After the initial handshake, the IoT edge module will agree on a set of authentication keys which will be auto-rotated as long as the module is able to periodically connect to the cloud. A new provisioning token can be generated for the same IoT edge module in case the module state lost or reset. |

## `SELECT` examples

Creates a new provisioning token. A provisioning token allows for a single instance of Azure Video analyzer IoT edge module to be initialized and authorized to the cloud account. The provisioning token itself is short lived and it is only used for the initial handshake between IoT edge module and the cloud. After the initial handshake, the IoT edge module will agree on a set of authentication keys which will be auto-rotated as long as the module is able to periodically connect to the cloud. A new provisioning token can be generated for the same IoT edge module in case the module state lost or reset.


```sql
SELECT
expirationDate,
token
FROM azure.video_analyzer.edge_modules_provisioning_tokens
WHERE accountName = '{{ accountName }}'
AND edgeModuleName = '{{ edgeModuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__expirationDate = '{{ data__expirationDate }}';
```