---
title: replication_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_fabrics
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_fabrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_fabrics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_fabrics', value: 'view', },
        { label: 'replication_fabrics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="bcdr_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="internal_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rollover_encryption_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Fabric properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an Azure Site Recovery fabric. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of the Azure Site Recovery fabrics in the vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an Azure Site Recovery fabric (for e.g. Hyper-V site). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete or remove an Azure Site Recovery fabric. |
| <CopyableCode code="check_consistency" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to perform a consistency check on the fabric. |
| <CopyableCode code="migrate_to_aad" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to migrate an Azure Site Recovery fabric to AAD. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge(force delete) an Azure Site Recovery fabric. |
| <CopyableCode code="reassociate_gateway" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | The operation to move replications from a process server to another process server. |
| <CopyableCode code="remove_infra" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="renew_certificate" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, resourceName, subscriptionId" /> | Renews the connection certificate for the ASR replication fabric. |

## `SELECT` examples

Gets a list of the Azure Site Recovery fabrics in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_fabrics', value: 'view', },
        { label: 'replication_fabrics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bcdr_state,
custom_details,
encryption_details,
fabricName,
friendly_name,
health,
health_error_details,
internal_identifier,
location,
resourceGroupName,
resourceName,
rollover_encryption_details,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_fabrics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.recovery_services_site_recovery.replication_fabrics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_fabrics</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_fabrics (
fabricName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ fabricName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: customDetails
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>replication_fabrics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_fabrics
WHERE fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
