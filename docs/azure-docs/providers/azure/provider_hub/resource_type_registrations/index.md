---
title: resource_type_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_type_registrations
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

Creates, updates, deletes, gets or lists a <code>resource_type_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_type_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.resource_type_registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Gets a resource type details in the given subscription and provider. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the resource types for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Creates or updates a resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Deletes a resource type |

## `SELECT` examples

Gets the list of the resource types for the given provider.


```sql
SELECT
properties
FROM azure.provider_hub.resource_type_registrations
WHERE providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_type_registrations</code> resource.

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
INSERT INTO azure.provider_hub.resource_type_registrations (
providerNamespace,
resourceType,
subscriptionId,
properties
)
SELECT 
'{{ providerNamespace }}',
'{{ resourceType }}',
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

Deletes the specified <code>resource_type_registrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.provider_hub.resource_type_registrations
WHERE providerNamespace = '{{ providerNamespace }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
