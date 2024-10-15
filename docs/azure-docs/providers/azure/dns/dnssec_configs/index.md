---
title: dnssec_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - dnssec_configs
  - dns
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

Creates, updates, deletes, gets or lists a <code>dnssec_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dnssec_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.dnssec_configs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dnssec_configs', value: 'view', },
        { label: 'dnssec_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the DNSSEC configuration. |
| <CopyableCode code="name" /> | `text` | The name of the DNSSEC configuration. |
| <CopyableCode code="etag" /> | `text` | The etag of the DNSSEC configuration. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="signing_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the DNSSEC configuration. |
| <CopyableCode code="zoneName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the DNSSEC configuration. |
| <CopyableCode code="name" /> | `string` | The name of the DNSSEC configuration. |
| <CopyableCode code="etag" /> | `string` | The etag of the DNSSEC configuration. |
| <CopyableCode code="properties" /> | `object` | Represents the DNSSEC properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the DNSSEC configuration. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Gets the DNSSEC configuration. |
| <CopyableCode code="list_by_dns_zone" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Lists the DNSSEC configurations in a DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Creates or updates the DNSSEC configuration on a DNS zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Deletes the DNSSEC configuration on a DNS zone. This operation cannot be undone. |

## `SELECT` examples

Gets the DNSSEC configuration.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dnssec_configs', value: 'view', },
        { label: 'dnssec_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
provisioning_state,
resourceGroupName,
signing_keys,
subscriptionId,
system_data,
type,
zoneName
FROM azure.dns.vw_dnssec_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.dns.dnssec_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dnssec_configs</code> resource.

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
INSERT INTO azure.dns.dnssec_configs (
resourceGroupName,
subscriptionId,
zoneName
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ zoneName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dnssec_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns.dnssec_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```
