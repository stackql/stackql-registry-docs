---
title: watchers_topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_topologies
  - network
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

Creates, updates, deletes, gets or lists a <code>watchers_topologies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers_topologies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_topologies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | GUID representing the operation id. |
| <CopyableCode code="createdDateTime" /> | `string` | The datetime when the topology was initially created for the resource group. |
| <CopyableCode code="lastModified" /> | `string` | The datetime when the topology was last modified. |
| <CopyableCode code="resources" /> | `array` | A list of topology resources. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Gets the current network topology by resource group. |

## `SELECT` examples

Gets the current network topology by resource group.


```sql
SELECT
id,
createdDateTime,
lastModified,
resources
FROM azure.network.watchers_topologies
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```