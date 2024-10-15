---
title: ip_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_firewall_rules
  - synapse
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

Creates, updates, deletes, gets or lists a <code>ip_firewall_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.ip_firewall_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_firewall_rules', value: 'view', },
        { label: 'ip_firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="end_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | IP firewall rule properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId, workspaceName" /> | Get a firewall rule |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of firewall rules |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId, workspaceName" /> | Creates or updates a firewall rule |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId, workspaceName" /> | Deletes a firewall rule |
| <CopyableCode code="replace_all" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Replaces firewall rules |

## `SELECT` examples

Returns a list of firewall rules

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_firewall_rules', value: 'view', },
        { label: 'ip_firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
end_ip_address,
provisioning_state,
resourceGroupName,
ruleName,
start_ip_address,
subscriptionId,
workspaceName
FROM azure.synapse.vw_ip_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.ip_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_firewall_rules</code> resource.

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
INSERT INTO azure.synapse.ip_firewall_rules (
resourceGroupName,
ruleName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: endIpAddress
          value: string
        - name: provisioningState
          value: string
        - name: startIpAddress
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ip_firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.ip_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
