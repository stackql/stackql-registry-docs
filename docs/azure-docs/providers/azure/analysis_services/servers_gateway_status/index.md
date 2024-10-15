---
title: servers_gateway_status
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_gateway_status
  - analysis_services
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

Creates, updates, deletes, gets or lists a <code>servers_gateway_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers_gateway_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.analysis_services.servers_gateway_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="status" /> | `integer` | Live message of list gateway. Status: 0 - Live |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Return the gateway status of the specified Analysis Services server instance. |

## `SELECT` examples

Return the gateway status of the specified Analysis Services server instance.


```sql
SELECT
status
FROM azure.analysis_services.servers_gateway_status
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```