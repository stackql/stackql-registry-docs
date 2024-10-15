---
title: replication_protection_intents
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_intents
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

Creates, updates, deletes, gets or lists a <code>replication_protection_intents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protection_intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_intents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_intents', value: 'view', },
        { label: 'replication_protection_intents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="creation_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="intentObjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_active" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
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
| <CopyableCode code="properties" /> | `object` | Replication protection intent custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="intentObjectName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR replication protection intent. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protection intent objects in the vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="intentObjectName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an ASR replication protection intent item. |

## `SELECT` examples

Gets the list of ASR replication protection intent objects in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_intents', value: 'view', },
        { label: 'replication_protection_intents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
creation_time_utc,
friendly_name,
intentObjectName,
is_active,
job_id,
job_state,
location,
provider_specific_details,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_protection_intents
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
FROM azure.recovery_services_site_recovery.replication_protection_intents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_protection_intents</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_protection_intents (
intentObjectName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ intentObjectName }}',
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
        - name: providerSpecificDetails
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>
