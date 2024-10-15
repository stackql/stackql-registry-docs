---
title: admin_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_rules
  - network
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

Creates, updates, deletes, gets or lists a <code>admin_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>admin_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.admin_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="kind" /> | `string` | Whether the rule is custom or default. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, ruleName, subscriptionId" /> | Gets a network manager security configuration admin rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, subscriptionId" /> | List all network manager security configuration admin rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, ruleName, subscriptionId, data__kind" /> | Creates or updates an admin rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, ruleName, subscriptionId" /> | Deletes an admin rule. |

## `SELECT` examples

List all network manager security configuration admin rules.


```sql
SELECT
id,
name,
etag,
kind,
systemData,
type
FROM azure.network.admin_rules
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>admin_rules</code> resource.

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
INSERT INTO azure.network.admin_rules (
configurationName,
networkManagerName,
resourceGroupName,
ruleCollectionName,
ruleName,
subscriptionId,
data__kind,
kind
)
SELECT 
'{{ configurationName }}',
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ ruleCollectionName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>admin_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.admin_rules
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
