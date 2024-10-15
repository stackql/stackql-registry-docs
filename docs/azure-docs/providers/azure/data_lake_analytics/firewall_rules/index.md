---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - data_lake_analytics
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.firewall_rules" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The firewall rule properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Analytics firewall rule. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Analytics firewall rules within the specified Data Lake Analytics account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the specified firewall rule. During update, the firewall rule with the specified name will be replaced with this new firewall rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId" /> | Deletes the specified firewall rule from the specified Data Lake Analytics account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId" /> | Updates the specified firewall rule. |

## `SELECT` examples

Lists the Data Lake Analytics firewall rules within the specified Data Lake Analytics account.

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
id,
name,
accountName,
end_ip_address,
firewallRuleName,
resourceGroupName,
start_ip_address,
subscriptionId,
type
FROM azure.data_lake_analytics.vw_firewall_rules
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.data_lake_analytics.firewall_rules
WHERE accountName = '{{ accountName }}'
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
INSERT INTO azure.data_lake_analytics.firewall_rules (
accountName,
firewallRuleName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ firewallRuleName }}',
'{{ resourceGroupName }}',
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
        - name: startIpAddress
          value: string
        - name: endIpAddress
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>firewall_rules</code> resource.

```sql
/*+ update */
UPDATE azure.data_lake_analytics.firewall_rules
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND firewallRuleName = '{{ firewallRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_analytics.firewall_rules
WHERE accountName = '{{ accountName }}'
AND firewallRuleName = '{{ firewallRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
