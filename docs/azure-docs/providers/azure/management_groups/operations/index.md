---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - management_groups
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: {provider}/{resource}/{operation}. |
| <CopyableCode code="display" /> | `object` | The object that represents the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available Management REST API operations. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="" /> | Checks if the specified management group name is valid and unique |
| <CopyableCode code="start_tenant_backfill" /> | `EXEC` | <CopyableCode code="" /> | Starts backfilling subscriptions for the Tenant. |
| <CopyableCode code="tenant_backfill_status" /> | `EXEC` | <CopyableCode code="" /> | Gets tenant backfill status |

## `SELECT` examples

Lists all of the available Management REST API operations.


```sql
SELECT
name,
display
FROM azure.management_groups.operations
;
```