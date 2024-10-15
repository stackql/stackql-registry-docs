---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
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

Creates, updates, deletes, gets or lists a <code>zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.zones" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_zones', value: 'view', },
        { label: 'zones', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | The etag of the zone. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="max_number_of_record_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_number_of_records_per_record_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="name_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_record_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_virtual_networks" /> | `text` | field from the `properties` object |
| <CopyableCode code="resolution_virtual_networks" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="signing_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="zoneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | The etag of the zone. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the zone. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the DNS zones in all resource groups in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the DNS zones within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Creates or updates a DNS zone. Does not modify DNS records within the zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Updates a DNS zone. Does not modify DNS records within the zone. |

## `SELECT` examples

Lists the DNS zones in all resource groups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_zones', value: 'view', },
        { label: 'zones', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
location,
max_number_of_record_sets,
max_number_of_records_per_record_set,
name_servers,
number_of_record_sets,
registration_virtual_networks,
resolution_virtual_networks,
resourceGroupName,
signing_keys,
subscriptionId,
system_data,
tags,
type,
zoneName,
zone_type
FROM azure.dns.vw_zones
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.dns.zones
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>zones</code> resource.

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
INSERT INTO azure.dns.zones (
resourceGroupName,
subscriptionId,
zoneName,
etag,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ zoneName }}',
'{{ etag }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: maxNumberOfRecordSets
          value: integer
        - name: maxNumberOfRecordsPerRecordSet
          value: integer
        - name: numberOfRecordSets
          value: integer
        - name: nameServers
          value:
            - string
        - name: zoneType
          value: string
        - name: registrationVirtualNetworks
          value:
            - - name: id
                value: string
        - name: resolutionVirtualNetworks
          value:
            - - name: id
                value: string
        - name: signingKeys
          value:
            - - name: delegationSignerInfo
                value:
                  - - name: digestAlgorithmType
                      value: []
                    - name: digestValue
                      value: string
                    - name: record
                      value: string
              - name: flags
                value: integer
              - name: keyTag
                value: integer
              - name: protocol
                value: integer
              - name: publicKey
                value: string
              - name: securityAlgorithmType
                value: []
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>zones</code> resource.

```sql
/*+ update */
UPDATE azure.dns.zones
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```

## `DELETE` example

Deletes the specified <code>zones</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns.zones
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```
