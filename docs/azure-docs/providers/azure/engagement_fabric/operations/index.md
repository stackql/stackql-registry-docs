---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - engagement_fabric
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.engagement_fabric.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the EngagementFabric operation |
| <CopyableCode code="display" /> | `object` | The display information of the EngagementFabric operation |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, data__name, data__type" /> |  |

## `SELECT` examples




```sql
SELECT
name,
display
FROM azure.engagement_fabric.operations
;
```