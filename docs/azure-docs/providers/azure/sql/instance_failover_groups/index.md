---
title: instance_failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_failover_groups
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

Creates, updates, deletes, gets or lists a <code>instance_failover_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.instance_failover_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instance_failover_groups', value: 'view', },
        { label: 'instance_failover_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="failoverGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_instance_pairs" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_only_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_write_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a instance failover group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Gets a failover group. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the failover groups in a location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Creates or updates a failover group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Deletes a failover group. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Fails over from the current primary managed instance to this managed instance. |
| <CopyableCode code="force_failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Fails over from the current primary managed instance to this managed instance. This operation might result in data loss. |

## `SELECT` examples

Lists the failover groups in a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instance_failover_groups', value: 'view', },
        { label: 'instance_failover_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
failoverGroupName,
locationName,
managed_instance_pairs,
partner_regions,
read_only_endpoint,
read_write_endpoint,
replication_role,
replication_state,
resourceGroupName,
secondary_type,
subscriptionId
FROM azure.sql.vw_instance_failover_groups
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.instance_failover_groups
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_failover_groups</code> resource.

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
INSERT INTO azure.sql.instance_failover_groups (
failoverGroupName,
locationName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ failoverGroupName }}',
'{{ locationName }}',
'{{ resourceGroupName }}',
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
        - name: secondaryType
          value: string
        - name: readWriteEndpoint
          value:
            - name: failoverPolicy
              value: string
            - name: failoverWithDataLossGracePeriodMinutes
              value: integer
        - name: readOnlyEndpoint
          value:
            - name: failoverPolicy
              value: string
        - name: replicationRole
          value: string
        - name: replicationState
          value: string
        - name: partnerRegions
          value:
            - - name: location
                value: string
              - name: replicationRole
                value: string
        - name: managedInstancePairs
          value:
            - - name: primaryManagedInstanceId
                value: string
              - name: partnerManagedInstanceId
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instance_failover_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.instance_failover_groups
WHERE failoverGroupName = '{{ failoverGroupName }}'
AND locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
