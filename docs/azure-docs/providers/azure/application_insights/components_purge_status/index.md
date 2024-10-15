---
title: components_purge_status
hide_title: false
hide_table_of_contents: false
keywords:
  - components_purge_status
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>components_purge_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components_purge_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.components_purge_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="status" /> | `string` | Status of the operation represented by the requested Id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="purgeId, resourceGroupName, resourceName, subscriptionId" /> | Get status for an ongoing purge operation. |

## `SELECT` examples

Get status for an ongoing purge operation.


```sql
SELECT
status
FROM azure.application_insights.components_purge_status
WHERE purgeId = '{{ purgeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```