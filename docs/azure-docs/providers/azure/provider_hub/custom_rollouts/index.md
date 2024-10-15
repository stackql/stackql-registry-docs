---
title: custom_rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_rollouts
  - provider_hub
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

Creates, updates, deletes, gets or lists a <code>custom_rollouts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.custom_rollouts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the rollout. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Gets the custom rollout details. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the custom rollouts for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId, data__properties" /> | Creates or updates the rollout details. |

## `SELECT` examples

Gets the list of the custom rollouts for the given provider.


```sql
SELECT
properties
FROM azure.provider_hub.custom_rollouts
WHERE providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_rollouts</code> resource.

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
INSERT INTO azure.provider_hub.custom_rollouts (
providerNamespace,
rolloutName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ providerNamespace }}',
'{{ rolloutName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string

```
</TabItem>
</Tabs>
