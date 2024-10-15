---
title: restorable_gremlin_graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_gremlin_graphs
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>restorable_gremlin_graphs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restorable_gremlin_graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.restorable_gremlin_graphs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource Identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="properties" /> | `object` | The properties of an Azure Cosmos DB Gremlin graph event |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceId, location, subscriptionId" /> | Show the event feed of all mutations done on all the Azure Cosmos DB Gremlin graphs under a specific database. This helps in scenario where container was accidentally deleted. This API requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission |

## `SELECT` examples

Show the event feed of all mutations done on all the Azure Cosmos DB Gremlin graphs under a specific database. This helps in scenario where container was accidentally deleted. This API requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission


```sql
SELECT
id,
name,
properties,
type
FROM azure.cosmos_db.restorable_gremlin_graphs
WHERE instanceId = '{{ instanceId }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```