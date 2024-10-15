---
title: sql_virtual_machine_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machine_groups
  - sql_vm
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

Creates, updates, deletes, gets or lists a <code>sql_virtual_machine_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_virtual_machine_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.sql_virtual_machine_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_virtual_machine_groups', value: 'view', },
        { label: 'sql_virtual_machine_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_manager_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlVirtualMachineGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_image_offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_image_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="wsfc_domain_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a SQL virtual machine group. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets a SQL virtual machine group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all SQL virtual machine groups in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL virtual machine groups in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId, data__location" /> | Creates or updates a SQL virtual machine group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Deletes a SQL virtual machine group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Updates SQL virtual machine group tags. |

## `SELECT` examples

Gets all SQL virtual machine groups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_virtual_machine_groups', value: 'view', },
        { label: 'sql_virtual_machine_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cluster_configuration,
cluster_manager_type,
location,
provisioning_state,
resourceGroupName,
scale_type,
sqlVirtualMachineGroupName,
sql_image_offer,
sql_image_sku,
subscriptionId,
system_data,
tags,
wsfc_domain_profile
FROM azure.sql_vm.vw_sql_virtual_machine_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.sql_vm.sql_virtual_machine_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_virtual_machine_groups</code> resource.

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
INSERT INTO azure.sql_vm.sql_virtual_machine_groups (
resourceGroupName,
sqlVirtualMachineGroupName,
subscriptionId,
data__location,
location,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlVirtualMachineGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: sqlImageOffer
          value: string
        - name: sqlImageSku
          value: string
        - name: scaleType
          value: string
        - name: clusterManagerType
          value: string
        - name: clusterConfiguration
          value: string
        - name: wsfcDomainProfile
          value:
            - name: domainFqdn
              value: string
            - name: ouPath
              value: string
            - name: clusterBootstrapAccount
              value: string
            - name: clusterOperatorAccount
              value: string
            - name: sqlServiceAccount
              value: string
            - name: isSqlServiceAccountGmsa
              value: boolean
            - name: fileShareWitnessPath
              value: string
            - name: storageAccountUrl
              value: string
            - name: storageAccountPrimaryKey
              value: string
            - name: clusterSubnetType
              value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_virtual_machine_groups</code> resource.

```sql
/*+ update */
UPDATE azure.sql_vm.sql_virtual_machine_groups
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineGroupName = '{{ sqlVirtualMachineGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_virtual_machine_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql_vm.sql_virtual_machine_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineGroupName = '{{ sqlVirtualMachineGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
