---
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
  - private_dns
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

Creates, updates, deletes, gets or lists a <code>record_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.private_dns.record_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_record_sets', value: 'view', },
        { label: 'record_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the record set. |
| <CopyableCode code="name" /> | `text` | The name of the record set. |
| <CopyableCode code="a_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="aaaa_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="cname_record" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the record set. |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_auto_registered" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="mx_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateZoneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ptr_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="recordType" /> | `text` | field from the `properties` object |
| <CopyableCode code="relativeRecordSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="soa_record" /> | `text` | field from the `properties` object |
| <CopyableCode code="srv_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="ttl" /> | `text` | field from the `properties` object |
| <CopyableCode code="txt_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the record set. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the record set. |
| <CopyableCode code="name" /> | `string` | The name of the record set. |
| <CopyableCode code="etag" /> | `string` | The ETag of the record set. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the records in the record set. |
| <CopyableCode code="type" /> | `string` | The type of the record set. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Gets a record set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Lists all record sets in a Private DNS zone. |
| <CopyableCode code="list_by_type" /> | `SELECT` | <CopyableCode code="privateZoneName, recordType, resourceGroupName, subscriptionId" /> | Lists the record sets of a specified type in a Private DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Creates or updates a record set within a Private DNS zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Deletes a record set from a Private DNS zone. This operation cannot be undone. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Updates a record set within a Private DNS zone. |

## `SELECT` examples

Lists all record sets in a Private DNS zone.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_record_sets', value: 'view', },
        { label: 'record_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
a_records,
aaaa_records,
cname_record,
etag,
fqdn,
is_auto_registered,
metadata,
mx_records,
privateZoneName,
ptr_records,
recordType,
relativeRecordSetName,
resourceGroupName,
soa_record,
srv_records,
subscriptionId,
ttl,
txt_records,
type
FROM azure.private_dns.vw_record_sets
WHERE privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.private_dns.record_sets
WHERE privateZoneName = '{{ privateZoneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>record_sets</code> resource.

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
INSERT INTO azure.private_dns.record_sets (
privateZoneName,
recordType,
relativeRecordSetName,
resourceGroupName,
subscriptionId,
etag,
properties
)
SELECT 
'{{ privateZoneName }}',
'{{ recordType }}',
'{{ relativeRecordSetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: metadata
          value: object
        - name: ttl
          value: integer
        - name: fqdn
          value: string
        - name: isAutoRegistered
          value: boolean
        - name: aRecords
          value:
            - - name: ipv4Address
                value: string
        - name: aaaaRecords
          value:
            - - name: ipv6Address
                value: string
        - name: cnameRecord
          value:
            - name: cname
              value: string
        - name: mxRecords
          value:
            - - name: preference
                value: integer
              - name: exchange
                value: string
        - name: ptrRecords
          value:
            - - name: ptrdname
                value: string
        - name: soaRecord
          value:
            - name: host
              value: string
            - name: email
              value: string
            - name: serialNumber
              value: integer
            - name: refreshTime
              value: integer
            - name: retryTime
              value: integer
            - name: expireTime
              value: integer
            - name: minimumTtl
              value: integer
        - name: srvRecords
          value:
            - - name: priority
                value: integer
              - name: weight
                value: integer
              - name: port
                value: integer
              - name: target
                value: string
        - name: txtRecords
          value:
            - - name: value
                value:
                  - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>record_sets</code> resource.

```sql
/*+ update */
UPDATE azure.private_dns.record_sets
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
privateZoneName = '{{ privateZoneName }}'
AND recordType = '{{ recordType }}'
AND relativeRecordSetName = '{{ relativeRecordSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>record_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.private_dns.record_sets
WHERE privateZoneName = '{{ privateZoneName }}'
AND recordType = '{{ recordType }}'
AND relativeRecordSetName = '{{ relativeRecordSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
