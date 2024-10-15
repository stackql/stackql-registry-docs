---
title: provider_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_registrations
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

Creates, updates, deletes, gets or lists a <code>provider_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.provider_registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the provider registration details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of the provider registrations in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Creates or updates the provider registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, subscriptionId" /> | Deletes a provider registration. |
| <CopyableCode code="generate_operations" /> | `EXEC` | <CopyableCode code="providerNamespace, subscriptionId" /> | Generates the operations api for the given provider. |

## `SELECT` examples

Gets the list of the provider registrations in the subscription.


```sql
SELECT
properties
FROM azure.provider_hub.provider_registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_registrations</code> resource.

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
INSERT INTO azure.provider_hub.provider_registrations (
providerNamespace,
subscriptionId,
properties
)
SELECT 
'{{ providerNamespace }}',
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

Deletes the specified <code>provider_registrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.provider_hub.provider_registrations
WHERE providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```
