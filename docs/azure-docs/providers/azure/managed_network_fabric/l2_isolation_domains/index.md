---
title: l2_isolation_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - l2_isolation_domains
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>l2_isolation_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>l2_isolation_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.l2_isolation_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_l2_isolation_domains', value: 'view', },
        { label: 'l2_isolation_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="l2IsolationDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mtu" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vlan_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | L2Isolation Domain Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements L2 Isolation Domain GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays L2IsolationDomains list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays L2IsolationDomains list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Creates layer 2 network connectivity between compute nodes within a rack and across racks.The configuration is applied on the devices only after the isolation domain is enabled. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Deletes layer 2 connectivity between compute nodes by managed by named L2 Isolation name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | API to update certain properties of the L2 Isolation Domain resource. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Commits the configuration of the given resources. |
| <CopyableCode code="update_administrative_state" /> | `EXEC` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Enables isolation domain across the fabric or on specified racks. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Validates the configuration of the resources. |

## `SELECT` examples

Displays L2IsolationDomains list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_l2_isolation_domains', value: 'view', },
        { label: 'l2_isolation_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
l2IsolationDomainName,
location,
mtu,
network_fabric_id,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
vlan_id
FROM azure.managed_network_fabric.vw_l2_isolation_domains
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.l2_isolation_domains
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>l2_isolation_domains</code> resource.

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
INSERT INTO azure.managed_network_fabric.l2_isolation_domains (
l2IsolationDomainName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ l2IsolationDomainName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: annotation
          value: string
        - name: networkFabricId
          value: []
        - name: vlanId
          value: integer
        - name: mtu
          value: integer
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>l2_isolation_domains</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.l2_isolation_domains
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
l2IsolationDomainName = '{{ l2IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>l2_isolation_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.l2_isolation_domains
WHERE l2IsolationDomainName = '{{ l2IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
