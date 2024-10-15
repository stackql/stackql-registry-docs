---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - time_series_insights
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

Creates, updates, deletes, gets or lists a <code>environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of the environment. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="sku" /> | `object` | The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate. |
| <CopyableCode code="tags" /> | `object` | Resource tags |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Gets the environment with the specified name in the specified subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the available environments associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the available environments within a subscription, irrespective of the resource groups. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId, data__kind, data__sku" /> | Create or update an environment in the specified subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Deletes the environment with the specified name in the specified subscription and resource group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId, data__kind" /> | Updates the environment with the specified name in the specified subscription and resource group. |

## `SELECT` examples

Lists all the available environments within a subscription, irrespective of the resource groups.


```sql
SELECT
kind,
location,
sku,
tags
FROM azure.time_series_insights.environments
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.time_series_insights.environments (
environmentName,
resourceGroupName,
subscriptionId,
data__kind,
data__sku,
kind,
sku,
location,
tags
)
SELECT 
'{{ environmentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ data__sku }}',
'{{ kind }}',
'{{ sku }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environments</code> resource.

```sql
/*+ update */
UPDATE azure.time_series_insights.environments
SET 
kind = '{{ kind }}',
tags = '{{ tags }}'
WHERE 
environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__kind = '{{ data__kind }}';
```

## `DELETE` example

Deletes the specified <code>environments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.time_series_insights.environments
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
