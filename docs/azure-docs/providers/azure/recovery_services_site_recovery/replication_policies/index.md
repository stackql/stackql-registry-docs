---
title: replication_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_policies
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

Creates, updates, deletes, gets or lists a <code>replication_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_policies', value: 'view', },
        { label: 'replication_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Protection profile custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a replication policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the replication policies for a vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create a replication policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete a replication policy. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="policyName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update a replication policy. |

## `SELECT` examples

Lists the replication policies for a vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_policies', value: 'view', },
        { label: 'replication_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
friendly_name,
location,
policyName,
provider_specific_details,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_policies
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
FROM azure.recovery_services_site_recovery.replication_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_policies</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_policies (
policyName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ policyName }}',
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
        - name: providerSpecificInput
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_policies</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replication_policies
SET 
properties = '{{ properties }}'
WHERE 
policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_policies
WHERE policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
