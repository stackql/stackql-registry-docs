---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>failover_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.failover_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_failover_groups', value: 'view', },
        { label: 'failover_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="failoverGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_managed_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spec" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlManagedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a failover group resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Retrieves a failover group resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlManagedInstanceName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId, data__properties" /> | Creates or replaces a failover group resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Deletes a failover group resource |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_failover_groups', value: 'view', },
        { label: 'failover_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
failoverGroupName,
partner_managed_instance_id,
provisioning_state,
resourceGroupName,
spec,
sqlManagedInstanceName,
status,
subscriptionId
FROM azure.azure_arc_data.vw_failover_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlManagedInstanceName = '{{ sqlManagedInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.azure_arc_data.failover_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlManagedInstanceName = '{{ sqlManagedInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>failover_groups</code> resource.

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
INSERT INTO azure.azure_arc_data.failover_groups (
failoverGroupName,
resourceGroupName,
sqlManagedInstanceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ failoverGroupName }}',
'{{ resourceGroupName }}',
'{{ sqlManagedInstanceName }}',
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
        - name: provisioningState
          value: string
        - name: partnerManagedInstanceId
          value: string
        - name: spec
          value:
            - name: sharedName
              value: string
            - name: sourceMI
              value: string
            - name: partnerMI
              value: string
            - name: partnerMirroringURL
              value: string
            - name: partnerMirroringCert
              value: string
            - name: partnerSyncMode
              value: string
            - name: role
              value: string
        - name: status
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>failover_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.failover_groups
WHERE failoverGroupName = '{{ failoverGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlManagedInstanceName = '{{ sqlManagedInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
