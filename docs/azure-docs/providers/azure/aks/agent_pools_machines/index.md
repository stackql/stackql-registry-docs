---
title: agent_pools_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools_machines
  - aks
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

Creates, updates, deletes, gets or lists a <code>agent_pools_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.agent_pools_machines" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId, data__machineNames" /> |  |

## `DELETE` example

Deletes the specified <code>agent_pools_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aks.agent_pools_machines
WHERE agentPoolName = '{{ agentPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__machineNames = '{{ data__machineNames }}';
```
