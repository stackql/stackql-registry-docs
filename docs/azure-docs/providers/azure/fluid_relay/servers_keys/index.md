---
title: servers_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_keys
  - fluid_relay
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

Creates, updates, deletes, gets or lists a <code>servers_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fluid_relay.servers_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key1" /> | `string` | The primary key for this server |
| <CopyableCode code="key2" /> | `string` | The secondary key for this server |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
key1,
key2
FROM azure.fluid_relay.servers_keys
WHERE fluidRelayServerName = '{{ fluidRelayServerName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```