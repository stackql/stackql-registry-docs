---
title: dns_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_record_sets
  - servicenetworking
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

Creates, updates, deletes, gets or lists a <code>dns_record_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.dns_record_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dnsRecordSets" /> | `array` | DNS record Set Resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="servicesId" /> | Producers can use this method to retrieve a list of available DNS RecordSets available inside the private zone on the tenant host project accessible from their network. |
| <CopyableCode code="add" /> | `INSERT` | <CopyableCode code="servicesId" /> | Service producers can use this method to add DNS record sets to private DNS zones in the shared producer host project. |
| <CopyableCode code="remove" /> | `DELETE` | <CopyableCode code="servicesId" /> | Service producers can use this method to remove DNS record sets from private DNS zones in the shared producer host project. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="servicesId" /> | Service producers can use this method to update DNS record sets from private DNS zones in the shared producer host project. |

## `SELECT` examples

Producers can use this method to retrieve a list of available DNS RecordSets available inside the private zone on the tenant host project accessible from their network.

```sql
SELECT
dnsRecordSets
FROM google.servicenetworking.dns_record_sets
WHERE servicesId = '{{ servicesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dns_record_sets</code> resource.

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
INSERT INTO google.servicenetworking.dns_record_sets (
servicesId,
zone,
dnsRecordSet,
consumerNetwork
)
SELECT 
'{{ servicesId }}',
'{{ zone }}',
'{{ dnsRecordSet }}',
'{{ consumerNetwork }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: zone
      value: '{{ zone }}'
    - name: dnsRecordSet
      value:
        - name: type
          value: '{{ type }}'
        - name: ttl
          value: '{{ ttl }}'
        - name: data
          value:
            - name: type
              value: '{{ type }}'
        - name: domain
          value: '{{ domain }}'
    - name: consumerNetwork
      value: '{{ consumerNetwork }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dns_record_sets</code> resource.

```sql
/*+ update */
UPDATE google.servicenetworking.dns_record_sets
SET 
zone = '{{ zone }}',
existingDnsRecordSet = '{{ existingDnsRecordSet }}',
consumerNetwork = '{{ consumerNetwork }}',
newDnsRecordSet = '{{ newDnsRecordSet }}'
WHERE 
servicesId = '{{ servicesId }}';
```

## `DELETE` example

Deletes the specified <code>dns_record_sets</code> resource.

```sql
/*+ delete */
DELETE FROM google.servicenetworking.dns_record_sets
WHERE servicesId = '{{ servicesId }}';
```
