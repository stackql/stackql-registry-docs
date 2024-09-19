---
title: dns_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones
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

Creates, updates, deletes, gets or lists a <code>dns_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.dns_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="consumerPeeringZone" /> | `object` | Represents a DNS zone resource. |
| <CopyableCode code="producerPrivateZone" /> | `object` | Represents a DNS zone resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsZonesId, networksId, projectsId, servicesId" /> | Service producers can use this method to retrieve a DNS zone in the shared producer host project and the matching peering zones in consumer project |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networksId, projectsId, servicesId" /> | * Service producers can use this method to retrieve a list of available DNS zones in the shared producer host project and the matching peering zones in the consumer project. * |
| <CopyableCode code="add" /> | `INSERT` | <CopyableCode code="servicesId" /> | Service producers can use this method to add private DNS zones in the shared producer host project and matching peering zones in the consumer project. |
| <CopyableCode code="remove" /> | `DELETE` | <CopyableCode code="servicesId" /> | Service producers can use this method to remove private DNS zones in the shared producer host project and matching peering zones in the consumer project. |

## `SELECT` examples

* Service producers can use this method to retrieve a list of available DNS zones in the shared producer host project and the matching peering zones in the consumer project. *

```sql
SELECT
consumerPeeringZone,
producerPrivateZone
FROM google.servicenetworking.dns_zones
WHERE networksId = '{{ networksId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dns_zones</code> resource.

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
INSERT INTO google.servicenetworking.dns_zones (
servicesId,
name,
dnsSuffix,
consumerNetwork
)
SELECT 
'{{ servicesId }}',
'{{ name }}',
'{{ dnsSuffix }}',
'{{ consumerNetwork }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: dnsSuffix
      value: string
    - name: consumerNetwork
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dns_zones</code> resource.

```sql
/*+ delete */
DELETE FROM google.servicenetworking.dns_zones
WHERE servicesId = '{{ servicesId }}';
```
