---
title: ipv6_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - ipv6_firewall_rules
  - sql
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

Creates, updates, deletes, gets or lists a <code>ipv6_firewall_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipv6_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.ipv6_firewall_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ipv6_firewall_rules', value: 'view', },
        { label: 'ipv6_firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="end_ipv6_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ipv6_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an IPv6 server firewall rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Gets an IPv6 firewall rule. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of IPv6 firewall rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an IPv6 firewall rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Deletes an IPv6 firewall rule. |

## `SELECT` examples

Gets a list of IPv6 firewall rules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ipv6_firewall_rules', value: 'view', },
        { label: 'ipv6_firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
end_ipv6_address,
firewallRuleName,
resourceGroupName,
serverName,
start_ipv6_address,
subscriptionId
FROM azure.sql.vw_ipv6_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.ipv6_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ipv6_firewall_rules</code> resource.

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
INSERT INTO azure.sql.ipv6_firewall_rules (
firewallRuleName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ firewallRuleName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
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
      value:
        - name: startIPv6Address
          value: string
        - name: endIPv6Address
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ipv6_firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.ipv6_firewall_rules
WHERE firewallRuleName = '{{ firewallRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
