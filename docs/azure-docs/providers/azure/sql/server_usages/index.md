---
title: server_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - server_usages
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the server usage metric. |
| <CopyableCode code="currentValue" /> | `number` | The current value of the metric. |
| <CopyableCode code="displayName" /> | `string` | The metric display name. |
| <CopyableCode code="limit" /> | `number` | The current limit of the metric. |
| <CopyableCode code="nextResetTime" /> | `string` | The next reset time for the metric (ISO8601 format). |
| <CopyableCode code="resourceName" /> | `string` | The name of the resource. |
| <CopyableCode code="unit" /> | `string` | The units of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Returns server usages. |

## `SELECT` examples

Returns server usages.


```sql
SELECT
name,
currentValue,
displayName,
limit,
nextResetTime,
resourceName,
unit
FROM azure.sql.server_usages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```