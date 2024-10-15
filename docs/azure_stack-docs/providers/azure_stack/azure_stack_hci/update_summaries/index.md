---
title: update_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - update_summaries
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>update_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>update_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.update_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of Update summaries |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get all Update summaries under the HCI cluster |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all Update summaries under the HCI cluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete Update Summaries |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Put Update summaries under the HCI cluster |

## `SELECT` examples

Get all Update summaries under the HCI cluster


```sql
SELECT
location,
properties
FROM azure_stack.azure_stack_hci.update_summaries
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>update_summaries</code> resource.

```sql
/*+ update */
REPLACE azure_stack.azure_stack_hci.update_summaries
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>update_summaries</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.update_summaries
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
