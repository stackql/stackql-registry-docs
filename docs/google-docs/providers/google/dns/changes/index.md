---
title: changes
hide_title: false
hide_table_of_contents: false
keywords:
  - changes
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

Creates, updates, deletes, gets or lists a <code>changes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.changes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the resource; defined by the server (output only). |
| <CopyableCode code="additions" /> | `array` | Which ResourceRecordSets to add? |
| <CopyableCode code="deletions" /> | `array` | Which ResourceRecordSets to remove? Must match existing data exactly. |
| <CopyableCode code="isServing" /> | `boolean` | If the DNS queries for the zone will be served. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="startTime" /> | `string` | The time that this operation was started by the server (output only). This is in RFC3339 text format. |
| <CopyableCode code="status" /> | `string` | Status of the operation (output only). A status of "done" means that the request to update the authoritative servers has been sent, but the servers might not be updated yet. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="changeId, managedZone, project" /> | Fetches the representation of an existing Change. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedZone, project" /> | Enumerates Changes to a ResourceRecordSet collection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managedZone, project" /> | Atomically updates the ResourceRecordSet collection. |

## `SELECT` examples

Enumerates Changes to a ResourceRecordSet collection.

```sql
SELECT
id,
additions,
deletions,
isServing,
kind,
startTime,
status
FROM google.dns.changes
WHERE managedZone = '{{ managedZone }}'
AND project = '{{ project }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>changes</code> resource.

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
INSERT INTO google.dns.changes (
managedZone,
project,
additions,
deletions,
startTime,
status,
isServing
)
SELECT 
'{{ managedZone }}',
'{{ project }}',
'{{ additions }}',
'{{ deletions }}',
'{{ startTime }}',
'{{ status }}',
{{ isServing }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: additions
      value:
        - - name: name
            value: string
          - name: type
            value: string
          - name: ttl
            value: integer
          - name: rrdatas
            value:
              - string
          - name: signatureRrdatas
            value:
              - string
          - name: routingPolicy
            value:
              - name: geo
                value:
                  - name: items
                    value:
                      - - name: location
                          value: string
                        - name: rrdatas
                          value:
                            - string
                        - name: signatureRrdatas
                          value:
                            - string
                        - name: healthCheckedTargets
                          value:
                            - name: internalLoadBalancers
                              value:
                                - - name: loadBalancerType
                                    value: string
                                  - name: ipAddress
                                    value: string
                                  - name: port
                                    value: string
                                  - name: ipProtocol
                                    value: string
                                  - name: networkUrl
                                    value: string
                                  - name: project
                                    value: string
                                  - name: region
                                    value: string
                                  - name: kind
                                    value: string
                            - name: externalEndpoints
                              value:
                                - string
                        - name: kind
                          value: string
                  - name: enableFencing
                    value: boolean
                  - name: kind
                    value: string
              - name: wrr
                value:
                  - name: items
                    value:
                      - - name: weight
                          value: number
                        - name: rrdatas
                          value:
                            - string
                        - name: signatureRrdatas
                          value:
                            - string
                        - name: kind
                          value: string
                  - name: kind
                    value: string
              - name: primaryBackup
                value:
                  - name: trickleTraffic
                    value: number
                  - name: kind
                    value: string
              - name: healthCheck
                value: string
              - name: kind
                value: string
          - name: kind
            value: string
    - name: deletions
      value:
        - - name: name
            value: string
          - name: type
            value: string
          - name: ttl
            value: integer
          - name: rrdatas
            value:
              - string
          - name: signatureRrdatas
            value:
              - string
          - name: kind
            value: string
    - name: startTime
      value: string
    - name: id
      value: string
    - name: status
      value: string
    - name: isServing
      value: boolean
    - name: kind
      value: string

```
</TabItem>
</Tabs>
