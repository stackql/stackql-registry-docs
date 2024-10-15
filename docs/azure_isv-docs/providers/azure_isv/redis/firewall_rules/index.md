---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - redis
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

Creates, updates, deletes, gets or lists a <code>firewall_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.firewall_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_rules', value: 'view', },
        { label: 'firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cacheName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Specifies a range of IP addresses permitted to connect to the cache |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, ruleName, subscriptionId" /> | Gets a single firewall rule in a specified redis cache. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Gets all firewall rules in the specified redis cache. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheName, resourceGroupName, ruleName, subscriptionId, data__properties" /> | Create or update a redis cache firewall rule |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, resourceGroupName, ruleName, subscriptionId" /> | Deletes a single firewall rule in a specified redis cache. |

## `SELECT` examples

Gets all firewall rules in the specified redis cache.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_rules', value: 'view', },
        { label: 'firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cacheName,
end_ip,
resourceGroupName,
ruleName,
start_ip,
subscriptionId
FROM azure_isv.redis.vw_firewall_rules
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.redis.firewall_rules
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_rules</code> resource.

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
INSERT INTO azure_isv.redis.firewall_rules (
cacheName,
resourceGroupName,
ruleName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ cacheName }}',
'{{ resourceGroupName }}',
'{{ ruleName }}',
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
      value:
        - name: startIP
          value: string
        - name: endIP
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis.firewall_rules
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
