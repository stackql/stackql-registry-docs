---
title: outbound_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_firewall_rules
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

Creates, updates, deletes, gets or lists a <code>outbound_firewall_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outbound_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.outbound_firewall_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_outbound_firewall_rules', value: 'view', },
        { label: 'outbound_firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="outboundRuleFqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an outbound firewall rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="outboundRuleFqdn, resourceGroupName, serverName, subscriptionId" /> | Gets an outbound firewall rule. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets all outbound firewall rules on a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="outboundRuleFqdn, resourceGroupName, serverName, subscriptionId" /> | Create a outbound firewall rule with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="outboundRuleFqdn, resourceGroupName, serverName, subscriptionId" /> | Deletes a outbound firewall rule with a given name. |

## `SELECT` examples

Gets all outbound firewall rules on a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_outbound_firewall_rules', value: 'view', },
        { label: 'outbound_firewall_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
outboundRuleFqdn,
provisioning_state,
resourceGroupName,
serverName,
subscriptionId
FROM azure.sql.vw_outbound_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.outbound_firewall_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>outbound_firewall_rules</code> resource.

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
INSERT INTO azure.sql.outbound_firewall_rules (
outboundRuleFqdn,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ outboundRuleFqdn }}',
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
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>outbound_firewall_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.outbound_firewall_rules
WHERE outboundRuleFqdn = '{{ outboundRuleFqdn }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
