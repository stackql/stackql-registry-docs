---
title: restorable_gremlin_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_gremlin_resources
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

Creates, updates, deletes, gets or lists a <code>restorable_gremlin_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restorable_gremlin_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.restorable_gremlin_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="databaseName" /> | `string` | The name of the gremlin database available for restore. |
| <CopyableCode code="graphNames" /> | `array` | The names of the graphs available for restore. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceId, location, subscriptionId" /> | Return a list of gremlin database and graphs combo that exist on the account at the given timestamp and location. This helps in scenarios to validate what resources exist at given timestamp and location. This API requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission. |

## `SELECT` examples

Return a list of gremlin database and graphs combo that exist on the account at the given timestamp and location. This helps in scenarios to validate what resources exist at given timestamp and location. This API requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission.


```sql
SELECT
id,
name,
databaseName,
graphNames,
type
FROM azure.cosmos_db.restorable_gremlin_resources
WHERE instanceId = '{{ instanceId }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```