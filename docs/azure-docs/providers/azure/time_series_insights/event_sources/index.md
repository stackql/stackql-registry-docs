---
title: event_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - event_sources
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

Creates, updates, deletes, gets or lists a <code>event_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.event_sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of the event source. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="tags" /> | `object` | Resource tags |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId" /> | Gets the event source with the specified name in the specified environment. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Lists all the available event sources associated with the subscription and within the specified resource group and environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId, data__kind" /> | Create or update an event source under the specified environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId" /> | Deletes the event source with the specified name in the specified subscription, resource group, and environment |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId, data__kind" /> | Updates the event source with the specified name in the specified subscription, resource group, and environment. |

## `SELECT` examples

Lists all the available event sources associated with the subscription and within the specified resource group and environment.


```sql
SELECT
kind,
location,
tags
FROM azure.time_series_insights.event_sources
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_sources</code> resource.

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
INSERT INTO azure.time_series_insights.event_sources (
environmentName,
eventSourceName,
resourceGroupName,
subscriptionId,
data__kind,
kind,
localTimestamp,
location,
tags
)
SELECT 
'{{ environmentName }}',
'{{ eventSourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ kind }}',
'{{ localTimestamp }}',
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
    - name: localTimestamp
      value:
        - name: format
          value: string
        - name: timeZoneOffset
          value:
            - name: propertyName
              value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>event_sources</code> resource.

```sql
/*+ update */
UPDATE azure.time_series_insights.event_sources
SET 
kind = '{{ kind }}',
tags = '{{ tags }}'
WHERE 
environmentName = '{{ environmentName }}'
AND eventSourceName = '{{ eventSourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__kind = '{{ data__kind }}';
```

## `DELETE` example

Deletes the specified <code>event_sources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.time_series_insights.event_sources
WHERE environmentName = '{{ environmentName }}'
AND eventSourceName = '{{ eventSourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
