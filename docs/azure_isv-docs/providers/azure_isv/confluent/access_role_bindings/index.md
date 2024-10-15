---
title: access_role_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - access_role_bindings
  - confluent
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

Creates, updates, deletes, gets or lists a <code>access_role_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_role_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.access_role_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `array` | List of Role Binding records |
| <CopyableCode code="kind" /> | `string` | Type of response |
| <CopyableCode code="metadata" /> | `object` | Metadata of the list |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, roleBindingId, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
data,
kind,
metadata
FROM azure_isv.confluent.access_role_bindings
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_role_bindings</code> resource.

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
INSERT INTO azure_isv.confluent.access_role_bindings (
organizationName,
resourceGroupName,
subscriptionId,
principal,
role_name,
crn_pattern
)
SELECT 
'{{ organizationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ principal }}',
'{{ role_name }}',
'{{ crn_pattern }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: principal
      value: string
    - name: role_name
      value: string
    - name: crn_pattern
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>access_role_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.confluent.access_role_bindings
WHERE organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleBindingId = '{{ roleBindingId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
