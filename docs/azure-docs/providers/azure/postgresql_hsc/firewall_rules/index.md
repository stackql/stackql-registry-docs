---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - postgresql_hsc
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.firewall_rules" /></td></tr>
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
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a cluster firewall rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, firewallRuleName, resourceGroupName, subscriptionId" /> | Gets information about a cluster firewall rule. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all the firewall rules on cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, firewallRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates a new cluster firewall rule or updates an existing cluster firewall rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, firewallRuleName, resourceGroupName, subscriptionId" /> | Deletes a cluster firewall rule. |

## `SELECT` examples

Lists all the firewall rules on cluster.

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
clusterName,
end_ip_address,
firewallRuleName,
provisioning_state,
resourceGroupName,
start_ip_address,
subscriptionId
FROM azure.postgresql_hsc.vw_firewall_rules
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql_hsc.firewall_rules
WHERE clusterName = '{{ clusterName }}'
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
INSERT INTO azure.postgresql_hsc.firewall_rules (
clusterName,
firewallRuleName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ clusterName }}',
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
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.postgresql_hsc.firewall_rules
WHERE clusterName = '{{ clusterName }}'
AND firewallRuleName = '{{ firewallRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
