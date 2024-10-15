---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - mysql
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.firewall_rules" /></td></tr>
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
| <CopyableCode code="end_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a server firewall rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Gets information about a server firewall rule. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the firewall rules in a given server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId, data__properties" /> | Creates a new firewall rule or updates an existing firewall rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Deletes a firewall rule. |

## `SELECT` examples

List all the firewall rules in a given server.

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
end_ip_address,
firewallRuleName,
resourceGroupName,
serverName,
start_ip_address,
subscriptionId
FROM azure.mysql.vw_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mysql.firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
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
INSERT INTO azure.mysql.firewall_rules (
firewallRuleName,
resourceGroupName,
serverName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ firewallRuleName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
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

## `DELETE` example

Deletes the specified <code>firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mysql.firewall_rules
WHERE firewallRuleName = '{{ firewallRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
