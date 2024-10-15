---
title: default_rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_rollouts
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

Creates, updates, deletes, gets or lists a <code>default_rollouts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.default_rollouts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the rollout. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Gets the default rollout details. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the rollouts for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Creates or updates the rollout details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Deletes the rollout resource. Rollout must be in terminal state. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Stops or cancels the rollout, if in progress. |

## `SELECT` examples

Gets the list of the rollouts for the given provider.


```sql
SELECT
properties
FROM azure.provider_hub.default_rollouts
WHERE providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>default_rollouts</code> resource.

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
INSERT INTO azure.provider_hub.default_rollouts (
providerNamespace,
rolloutName,
subscriptionId,
properties
)
SELECT 
'{{ providerNamespace }}',
'{{ rolloutName }}',
'{{ subscriptionId }}',
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

## `DELETE` example

Deletes the specified <code>default_rollouts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.provider_hub.default_rollouts
WHERE providerNamespace = '{{ providerNamespace }}'
AND rolloutName = '{{ rolloutName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
