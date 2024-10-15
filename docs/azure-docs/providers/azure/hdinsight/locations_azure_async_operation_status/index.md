---
title: locations_azure_async_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_azure_async_operation_status
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>locations_azure_async_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_azure_async_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.locations_azure_async_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `object` | The error message associated with the cluster creation. |
| <CopyableCode code="status" /> | `string` | The async operation state. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> | Get the async operation status. |

## `SELECT` examples

Get the async operation status.


```sql
SELECT
error,
status
FROM azure.hdinsight.locations_azure_async_operation_status
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```