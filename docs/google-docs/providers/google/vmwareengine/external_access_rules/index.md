
---
title: external_access_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - external_access_rules
  - vmwareengine
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

Creates, updates, deletes or gets an <code>external_access_rule</code> resource or lists <code>external_access_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_access_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.external_access_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this external access rule. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule` |
| <CopyableCode code="description" /> | `string` | User-provided description for this external access rule. |
| <CopyableCode code="action" /> | `string` | The action that the external access rule performs. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="destinationIpRanges" /> | `array` | If destination ranges are specified, the external access rule applies only to the traffic that has a destination IP address in these ranges. The specified IP addresses must have reserved external IP addresses in the scope of the parent network policy. To match all external IP addresses in the scope of the parent network policy, specify `0.0.0.0/0`. To match a specific external IP address, specify it using the `IpRange.external_address` property. |
| <CopyableCode code="destinationPorts" /> | `array` | A list of destination ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all destination ports, specify `["0-65535"]`. |
| <CopyableCode code="ipProtocol" /> | `string` | The IP protocol to which the external access rule applies. This value can be one of the following three protocol strings (not case-sensitive): `tcp`, `udp`, or `icmp`. |
| <CopyableCode code="priority" /> | `integer` | External access rule priority, which determines the external access rule to use when multiple rules apply. If multiple rules have the same priority, their ordering is non-deterministic. If specific ordering is required, assign unique priorities to enforce such ordering. The external access rule priority is an integer from 100 to 4096, both inclusive. Lower integers indicate higher precedence. For example, a rule with priority `100` has higher precedence than a rule with priority `101`. |
| <CopyableCode code="sourceIpRanges" /> | `array` | If source ranges are specified, the external access rule applies only to traffic that has a source IP address in these ranges. These ranges can either be expressed in the CIDR format or as an IP address. As only inbound rules are supported, `ExternalAddress` resources cannot be the source IP addresses of an external access rule. To match all source addresses, specify `0.0.0.0/0`. |
| <CopyableCode code="sourcePorts" /> | `array` | A list of source ports to which the external access rule applies. This field is only applicable for the UDP or TCP protocol. Each entry must be either an integer or a range. For example: `["22"]`, `["80","443"]`, or `["12345-12349"]`. To match all source ports, specify `["0-65535"]`. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the resource. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="externalAccessRulesId, locationsId, networkPoliciesId, projectsId" /> | Gets details of a single external access rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, networkPoliciesId, projectsId" /> | Lists `ExternalAccessRule` resources in the specified network policy. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, networkPoliciesId, projectsId" /> | Creates a new external access rule in a given network policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="externalAccessRulesId, locationsId, networkPoliciesId, projectsId" /> | Deletes a single external access rule. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="externalAccessRulesId, locationsId, networkPoliciesId, projectsId" /> | Updates the parameters of a single external access rule. Only fields specified in `update_mask` are applied. |

## `SELECT` examples

Lists `ExternalAccessRule` resources in the specified network policy.

```sql
SELECT
name,
description,
action,
createTime,
destinationIpRanges,
destinationPorts,
ipProtocol,
priority,
sourceIpRanges,
sourcePorts,
state,
uid,
updateTime
FROM google.vmwareengine.external_access_rules
WHERE locationsId = '{{ locationsId }}'
AND networkPoliciesId = '{{ networkPoliciesId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_access_rules</code> resource.

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
INSERT INTO google.vmwareengine.external_access_rules (
locationsId,
networkPoliciesId,
projectsId,
name,
createTime,
updateTime,
description,
priority,
action,
ipProtocol,
sourceIpRanges,
sourcePorts,
destinationIpRanges,
destinationPorts,
state,
uid
)
SELECT 
'{{ locationsId }}',
'{{ networkPoliciesId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ priority }}',
'{{ action }}',
'{{ ipProtocol }}',
'{{ sourceIpRanges }}',
'{{ sourcePorts }}',
'{{ destinationIpRanges }}',
'{{ destinationPorts }}',
'{{ state }}',
'{{ uid }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: priority
        value: '{{ priority }}'
      - name: action
        value: '{{ action }}'
      - name: ipProtocol
        value: '{{ ipProtocol }}'
      - name: sourceIpRanges
        value: '{{ sourceIpRanges }}'
      - name: sourcePorts
        value: '{{ sourcePorts }}'
      - name: destinationIpRanges
        value: '{{ destinationIpRanges }}'
      - name: destinationPorts
        value: '{{ destinationPorts }}'
      - name: state
        value: '{{ state }}'
      - name: uid
        value: '{{ uid }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a external_access_rule only if the necessary resources are available.

```sql
UPDATE google.vmwareengine.external_access_rules
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
priority = '{{ priority }}',
action = '{{ action }}',
ipProtocol = '{{ ipProtocol }}',
sourceIpRanges = '{{ sourceIpRanges }}',
sourcePorts = '{{ sourcePorts }}',
destinationIpRanges = '{{ destinationIpRanges }}',
destinationPorts = '{{ destinationPorts }}',
state = '{{ state }}',
uid = '{{ uid }}'
WHERE 
externalAccessRulesId = '{{ externalAccessRulesId }}'
AND locationsId = '{{ locationsId }}'
AND networkPoliciesId = '{{ networkPoliciesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified external_access_rule resource.

```sql
DELETE FROM google.vmwareengine.external_access_rules
WHERE externalAccessRulesId = '{{ externalAccessRulesId }}'
AND locationsId = '{{ locationsId }}'
AND networkPoliciesId = '{{ networkPoliciesId }}'
AND projectsId = '{{ projectsId }}';
```
