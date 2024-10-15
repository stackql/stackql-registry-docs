---
title: alert_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_operations
  - authorization
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

Creates, updates, deletes, gets or lists a <code>alert_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the alert operation. |
| <CopyableCode code="createdDateTime" /> | `string` | The created date of the alert operation. |
| <CopyableCode code="lastActionDateTime" /> | `string` | The last action date of the alert operation. |
| <CopyableCode code="resourceLocation" /> | `string` | The location of the alert associated with the operation. |
| <CopyableCode code="status" /> | `string` | The status of the alert operation. |
| <CopyableCode code="statusDetail" /> | `string` | The status detail of the alert operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, scope" /> | Get the specified alert operation. |

## `SELECT` examples

Get the specified alert operation.


```sql
SELECT
id,
createdDateTime,
lastActionDateTime,
resourceLocation,
status,
statusDetail
FROM azure.authorization.alert_operations
WHERE operationId = '{{ operationId }}'
AND scope = '{{ scope }}';
```