---
title: private_link_service_resource_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_service_resource_operation_results
  - powerbi_privatelinks
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

Creates, updates, deletes, gets or lists a <code>private_link_service_resource_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_service_resource_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_privatelinks.private_link_service_resource_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation id. |
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="endTime" /> | `string` | The operation end time. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="startTime" /> | `string` | The operation start time. |
| <CopyableCode code="status" /> | `string` | The operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, subscriptionId" /> | Gets operation result of Private Link Service Resources for Power BI. |

## `SELECT` examples

Gets operation result of Private Link Service Resources for Power BI.


```sql
SELECT
id,
name,
endTime,
error,
startTime,
status
FROM azure.powerbi_privatelinks.private_link_service_resource_operation_results
WHERE operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```