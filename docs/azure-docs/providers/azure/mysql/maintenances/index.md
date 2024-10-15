---
title: maintenances
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenances
  - mysql
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

Creates, updates, deletes, gets or lists a <code>maintenances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.maintenances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a maintenance resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List maintenances. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="maintenanceName, resourceGroupName, serverName, subscriptionId" /> | Update maintenances. |
| <CopyableCode code="read" /> | `EXEC` | <CopyableCode code="maintenanceName, resourceGroupName, serverName, subscriptionId" /> | Read maintenance. |

## `SELECT` examples

List maintenances.


```sql
SELECT
properties
FROM azure.mysql.maintenances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `UPDATE` example

Updates a <code>maintenances</code> resource.

```sql
/*+ update */
UPDATE azure.mysql.maintenances
SET 
properties = '{{ properties }}'
WHERE 
maintenanceName = '{{ maintenanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
