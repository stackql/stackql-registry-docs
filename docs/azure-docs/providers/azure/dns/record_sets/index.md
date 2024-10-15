---
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
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

Creates, updates, deletes, gets or lists a <code>record_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.record_sets" /></td></tr>
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
| <CopyableCode code="caa_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="cname_record" /> | `text` | field from the `properties` object |
| <CopyableCode code="ds_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag of the record set. |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="mx_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="naptr_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="ns_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ptr_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="recordType" /> | `text` | field from the `properties` object |
| <CopyableCode code="relativeRecordSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="soa_record" /> | `text` | field from the `properties` object |
| <CopyableCode code="srv_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="tlsa_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="traffic_management_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="ttl" /> | `text` | field from the `properties` object |
| <CopyableCode code="txt_records" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the record set. |
| <CopyableCode code="zoneName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the record set. |
| <CopyableCode code="name" /> | `string` | The name of the record set. |
| <CopyableCode code="etag" /> | `string` | The etag of the record set. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the records in the record set. |
| <CopyableCode code="type" /> | `string` | The type of the record set. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Gets a record set. |
| <CopyableCode code="list_by_dns_zone" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Lists all record sets in a DNS zone. |
| <CopyableCode code="list_by_type" /> | `SELECT` | <CopyableCode code="recordType, resourceGroupName, subscriptionId, zoneName" /> | Lists the record sets of a specified type in a DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Creates or updates a record set within a DNS zone. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Deletes a record set from a DNS zone. This operation cannot be undone. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted). |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Updates a record set within a DNS zone. |

## `SELECT` examples

Lists all record sets in a DNS zone.

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
caa_records,
cname_record,
ds_records,
etag,
fqdn,
metadata,
mx_records,
naptr_records,
ns_records,
provisioning_state,
ptr_records,
recordType,
relativeRecordSetName,
resourceGroupName,
soa_record,
srv_records,
subscriptionId,
target_resource,
tlsa_records,
traffic_management_profile,
ttl,
txt_records,
type,
zoneName
FROM azure.dns.vw_record_sets
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
type
FROM azure.dns.record_sets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
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
INSERT INTO azure.dns.record_sets (
recordType,
relativeRecordSetName,
resourceGroupName,
subscriptionId,
zoneName,
etag,
properties
)
SELECT 
'{{ recordType }}',
'{{ relativeRecordSetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ zoneName }}',
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
        - name: TTL
          value: integer
        - name: fqdn
          value: string
        - name: provisioningState
          value: string
        - name: targetResource
          value:
            - name: id
              value: string
        - name: ARecords
          value:
            - - name: ipv4Address
                value: string
        - name: AAAARecords
          value:
            - - name: ipv6Address
                value: string
        - name: MXRecords
          value:
            - - name: preference
                value: integer
              - name: exchange
                value: string
        - name: NSRecords
          value:
            - - name: nsdname
                value: string
        - name: PTRRecords
          value:
            - - name: ptrdname
                value: string
        - name: SRVRecords
          value:
            - - name: priority
                value: integer
              - name: weight
                value: integer
              - name: port
                value: integer
              - name: target
                value: string
        - name: TXTRecords
          value:
            - - name: value
                value:
                  - string
        - name: CNAMERecord
          value:
            - name: cname
              value: string
        - name: SOARecord
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
            - name: minimumTTL
              value: integer
        - name: caaRecords
          value:
            - - name: flags
                value: integer
              - name: tag
                value: string
              - name: value
                value: string
        - name: DSRecords
          value:
            - - name: keyTag
                value: integer
              - name: algorithm
                value: []
              - name: digest
                value:
                  - name: algorithmType
                    value: []
                  - name: value
                    value: string
        - name: TLSARecords
          value:
            - - name: usage
                value: integer
              - name: selector
                value: integer
              - name: matchingType
                value: integer
              - name: certAssociationData
                value: string
        - name: NAPTRRecords
          value:
            - - name: order
                value: integer
              - name: preference
                value: integer
              - name: flags
                value: string
              - name: services
                value: string
              - name: regexp
                value: string
              - name: replacement
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>record_sets</code> resource.

```sql
/*+ update */
UPDATE azure.dns.record_sets
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
recordType = '{{ recordType }}'
AND relativeRecordSetName = '{{ relativeRecordSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```

## `DELETE` example

Deletes the specified <code>record_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns.record_sets
WHERE recordType = '{{ recordType }}'
AND relativeRecordSetName = '{{ relativeRecordSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND zoneName = '{{ zoneName }}';
```
