---
title: resource_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_record_sets
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

Creates, updates, deletes, gets or lists a <code>resource_record_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.resource_record_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | For example, www.example.com. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="routingPolicy" /> | `object` | A RRSetRoutingPolicy represents ResourceRecordSet data that is returned dynamically with the response varying based on configured properties such as geolocation or by weighted random selection. |
| <CopyableCode code="rrdatas" /> | `array` | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples. |
| <CopyableCode code="signatureRrdatas" /> | `array` | As defined in RFC 4034 (section 3.2). |
| <CopyableCode code="ttl" /> | `integer` | Number of seconds that this `ResourceRecordSet` can be cached by resolvers. |
| <CopyableCode code="type" /> | `string` | The identifier of a supported record type. See the list of Supported DNS record types. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedZone, name, project, type" /> | Fetches the representation of an existing ResourceRecordSet. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedZone, project" /> | Enumerates ResourceRecordSets that you have created but not yet deleted. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managedZone, project" /> | Creates a new ResourceRecordSet. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedZone, name, project, type" /> | Deletes a previously created ResourceRecordSet. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="managedZone, name, project, type" /> | Applies a partial update to an existing ResourceRecordSet. |

## `SELECT` examples

Enumerates ResourceRecordSets that you have created but not yet deleted.

```sql
SELECT
name,
kind,
routingPolicy,
rrdatas,
signatureRrdatas,
ttl,
type
FROM google.dns.resource_record_sets
WHERE managedZone = '{{ managedZone }}'
AND project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_record_sets</code> resource.

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
INSERT INTO google.dns.resource_record_sets (
managedZone,
project,
name,
type,
ttl,
rrdatas,
signatureRrdatas,
routingPolicy
)
SELECT 
'{{ managedZone }}',
'{{ project }}',
'{{ name }}',
'{{ type }}',
'{{ ttl }}',
'{{ rrdatas }}',
'{{ signatureRrdatas }}',
'{{ routingPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: type
      value: '{{ type }}'
    - name: ttl
      value: '{{ ttl }}'
    - name: rrdatas
      value:
        - name: type
          value: '{{ type }}'
    - name: signatureRrdatas
      value:
        - name: type
          value: '{{ type }}'
    - name: routingPolicy
      value:
        - name: geo
          value:
            - name: items
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: enableFencing
              value: '{{ enableFencing }}'
        - name: wrr
          value:
            - name: items
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: primaryBackup
          value:
            - name: primaryTargets
              value:
                - name: internalLoadBalancers
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: externalEndpoints
                  value:
                    - name: type
                      value: '{{ type }}'
            - name: trickleTraffic
              value: '{{ trickleTraffic }}'
        - name: healthCheck
          value: '{{ healthCheck }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resource_record_sets</code> resource.

```sql
/*+ update */
UPDATE google.dns.resource_record_sets
SET 
name = '{{ name }}',
type = '{{ type }}',
ttl = '{{ ttl }}',
rrdatas = '{{ rrdatas }}',
signatureRrdatas = '{{ signatureRrdatas }}',
routingPolicy = '{{ routingPolicy }}'
WHERE 
managedZone = '{{ managedZone }}'
AND name = '{{ name }}'
AND project = '{{ project }}'
AND type = '{{ type }}';
```

## `DELETE` example

Deletes the specified <code>resource_record_sets</code> resource.

```sql
/*+ delete */
DELETE FROM google.dns.resource_record_sets
WHERE managedZone = '{{ managedZone }}'
AND name = '{{ name }}'
AND project = '{{ project }}'
AND type = '{{ type }}';
```
