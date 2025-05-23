---
title: response_policy_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - response_policy_rules
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

Creates, updates, deletes, gets or lists a <code>response_policy_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_policy_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.response_policy_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="behavior" /> | `string` | Answer this query with a behavior rather than DNS data. |
| <CopyableCode code="dnsName" /> | `string` | The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="localData" /> | `object` |  |
| <CopyableCode code="ruleName" /> | `string` | An identifier for this rule. Must be unique with the ResponsePolicy. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Fetches the representation of an existing Response Policy Rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, responsePolicy" /> | Enumerates all Response Policy Rules associated with a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="project, responsePolicy" /> | Creates a new Response Policy Rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Deletes a previously created Response Policy Rule. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Applies a partial update to an existing Response Policy Rule. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="project, responsePolicy, responsePolicyRule" /> | Updates an existing Response Policy Rule. |

## `SELECT` examples

Enumerates all Response Policy Rules associated with a project.

```sql
SELECT
behavior,
dnsName,
kind,
localData,
ruleName
FROM google.dns.response_policy_rules
WHERE project = '{{ project }}'
AND responsePolicy = '{{ responsePolicy }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>response_policy_rules</code> resource.

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
INSERT INTO google.dns.response_policy_rules (
project,
responsePolicy,
ruleName,
dnsName,
localData,
behavior
)
SELECT 
'{{ project }}',
'{{ responsePolicy }}',
'{{ ruleName }}',
'{{ dnsName }}',
'{{ localData }}',
'{{ behavior }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: ruleName
      value: string
    - name: dnsName
      value: string
    - name: localData
      value:
        - name: localDatas
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
    - name: behavior
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>response_policy_rules</code> resource.

```sql
/*+ update */
UPDATE google.dns.response_policy_rules
SET 
ruleName = '{{ ruleName }}',
dnsName = '{{ dnsName }}',
localData = '{{ localData }}',
behavior = '{{ behavior }}'
WHERE 
project = '{{ project }}'
AND responsePolicy = '{{ responsePolicy }}'
AND responsePolicyRule = '{{ responsePolicyRule }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>response_policy_rules</code> resource.

```sql
/*+ update */
REPLACE google.dns.response_policy_rules
SET 
ruleName = '{{ ruleName }}',
dnsName = '{{ dnsName }}',
localData = '{{ localData }}',
behavior = '{{ behavior }}'
WHERE 
project = '{{ project }}'
AND responsePolicy = '{{ responsePolicy }}'
AND responsePolicyRule = '{{ responsePolicyRule }}';
```

## `DELETE` example

Deletes the specified <code>response_policy_rules</code> resource.

```sql
/*+ delete */
DELETE FROM google.dns.response_policy_rules
WHERE project = '{{ project }}'
AND responsePolicy = '{{ responsePolicy }}'
AND responsePolicyRule = '{{ responsePolicyRule }}';
```
