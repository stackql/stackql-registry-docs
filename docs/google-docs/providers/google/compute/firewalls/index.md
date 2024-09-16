---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - compute
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

Creates, updates, deletes, gets or lists a <code>firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this field when you create the resource. |
| <CopyableCode code="allowed" /> | `array` | The list of ALLOW rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="denied" /> | `array` | The list of DENY rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a denied connection. |
| <CopyableCode code="destinationRanges" /> | `array` | If destination ranges are specified, the firewall rule applies only to traffic that has destination IP address in these ranges. These ranges must be expressed in CIDR format. Both IPv4 and IPv6 are supported. |
| <CopyableCode code="direction" /> | `string` | Direction of traffic to which this firewall applies, either `INGRESS` or `EGRESS`. The default is `INGRESS`. For `EGRESS` traffic, you cannot specify the sourceTags fields. |
| <CopyableCode code="disabled" /> | `boolean` | Denotes whether the firewall rule is disabled. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#firewall for firewall rules. |
| <CopyableCode code="logConfig" /> | `object` | The available logging options for a firewall rule. |
| <CopyableCode code="network" /> | `string` | URL of the network resource for this firewall rule. If not specified when creating a firewall rule, the default network is used: global/networks/default If you choose to specify this field, you can specify the network as a full or partial URL. For example, the following are all valid URLs: - https://www.googleapis.com/compute/v1/projects/myproject/global/networks/my-network - projects/myproject/global/networks/my-network - global/networks/default  |
| <CopyableCode code="priority" /> | `integer` | Priority for this rule. This is an integer between `0` and `65535`, both inclusive. The default value is `1000`. Relative priorities determine which rule takes effect if multiple rules apply. Lower values indicate higher priority. For example, a rule with priority `0` has higher precedence than a rule with priority `1`. DENY rules take precedence over ALLOW rules if they have equal priority. Note that VPC networks have implied rules with a priority of `65535`. To avoid conflicts with the implied rules, use a priority number less than `65535`. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="sourceRanges" /> | `array` | If source ranges are specified, the firewall rule applies only to traffic that has a source IP address in these ranges. These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both fields are set, the rule applies to traffic that has a source IP address within sourceRanges OR a source IP from a resource with a matching tag listed in the sourceTags field. The connection does not need to match both fields for the rule to apply. Both IPv4 and IPv6 are supported. |
| <CopyableCode code="sourceServiceAccounts" /> | `array` | If source service accounts are specified, the firewall rules apply only to traffic originating from an instance with a service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same time as sourceServiceAccounts. If both are set, the firewall applies to traffic that has a source IP address within the sourceRanges OR a source IP that belongs to an instance with service account listed in sourceServiceAccount. The connection does not need to match both fields for the firewall to apply. sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags. |
| <CopyableCode code="sourceTags" /> | `array` | If source tags are specified, the firewall rule applies only to traffic with source IPs that match the primary network interfaces of VM instances that have the tag and are in the same VPC network. Source tags cannot be used to control traffic to an instance's external IP address, it only applies to traffic between instances in the same virtual network. Because tags are associated with instances, not IP addresses. One or both of sourceRanges and sourceTags may be set. If both fields are set, the firewall applies to traffic that has a source IP address within sourceRanges OR a source IP from a resource with a matching tag listed in the sourceTags field. The connection does not need to match both fields for the firewall to apply. |
| <CopyableCode code="targetServiceAccounts" /> | `array` | A list of service accounts indicating sets of instances located in the network that may make network connections as specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network. |
| <CopyableCode code="targetTags" /> | `array` | A list of tags that controls which instances the firewall rule applies to. If targetTags are specified, then the firewall rule applies only to instances in the VPC network that have one of those tags. If no targetTags are specified, the firewall rule applies to all instances on the specified network. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewall, project" /> | Returns the specified firewall. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of firewall rules available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a firewall rule in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewall, project" /> | Deletes the specified firewall. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="firewall, project" /> | Updates the specified firewall rule with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="firewall, project" /> | Updates the specified firewall rule with the data included in the request. Note that all fields will be updated if using PUT, even fields that are not specified. To update individual fields, please use PATCH instead. |

## `SELECT` examples

Retrieves the list of firewall rules available to the specified project.

```sql
SELECT
id,
name,
description,
allowed,
creationTimestamp,
denied,
destinationRanges,
direction,
disabled,
kind,
logConfig,
network,
priority,
selfLink,
sourceRanges,
sourceServiceAccounts,
sourceTags,
targetServiceAccounts,
targetTags
FROM google.compute.firewalls
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewalls</code> resource.

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
INSERT INTO google.compute.firewalls (
project,
name,
description,
network,
priority,
sourceRanges,
destinationRanges,
sourceTags,
targetTags,
sourceServiceAccounts,
targetServiceAccounts,
allowed,
denied,
direction,
logConfig,
disabled
)
SELECT 
'{{ project }}',
'{{ name }}',
'{{ description }}',
'{{ network }}',
'{{ priority }}',
'{{ sourceRanges }}',
'{{ destinationRanges }}',
'{{ sourceTags }}',
'{{ targetTags }}',
'{{ sourceServiceAccounts }}',
'{{ targetServiceAccounts }}',
'{{ allowed }}',
'{{ denied }}',
'{{ direction }}',
'{{ logConfig }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: network
      value: '{{ network }}'
    - name: priority
      value: '{{ priority }}'
    - name: sourceRanges
      value:
        - name: type
          value: '{{ type }}'
    - name: destinationRanges
      value:
        - name: type
          value: '{{ type }}'
    - name: sourceTags
      value:
        - name: type
          value: '{{ type }}'
    - name: targetTags
      value:
        - name: type
          value: '{{ type }}'
    - name: sourceServiceAccounts
      value:
        - name: type
          value: '{{ type }}'
    - name: targetServiceAccounts
      value:
        - name: type
          value: '{{ type }}'
    - name: allowed
      value:
        - name: IPProtocol
          value: '{{ IPProtocol }}'
        - name: ports
          value:
            - name: type
              value: '{{ type }}'
    - name: denied
      value:
        - name: IPProtocol
          value: '{{ IPProtocol }}'
        - name: ports
          value:
            - name: type
              value: '{{ type }}'
    - name: direction
      value: '{{ direction }}'
    - name: logConfig
      value:
        - name: enable
          value: '{{ enable }}'
        - name: metadata
          value: '{{ metadata }}'
    - name: disabled
      value: '{{ disabled }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>firewalls</code> resource.

```sql
/*+ update */
UPDATE google.compute.firewalls
SET 
name = '{{ name }}',
description = '{{ description }}',
network = '{{ network }}',
priority = '{{ priority }}',
sourceRanges = '{{ sourceRanges }}',
destinationRanges = '{{ destinationRanges }}',
sourceTags = '{{ sourceTags }}',
targetTags = '{{ targetTags }}',
sourceServiceAccounts = '{{ sourceServiceAccounts }}',
targetServiceAccounts = '{{ targetServiceAccounts }}',
allowed = '{{ allowed }}',
denied = '{{ denied }}',
direction = '{{ direction }}',
logConfig = '{{ logConfig }}',
disabled = true|false
WHERE 
firewall = '{{ firewall }}'
AND project = '{{ project }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>firewalls</code> resource.

```sql
/*+ update */
REPLACE google.compute.firewalls
SET 
name = '{{ name }}',
description = '{{ description }}',
network = '{{ network }}',
priority = '{{ priority }}',
sourceRanges = '{{ sourceRanges }}',
destinationRanges = '{{ destinationRanges }}',
sourceTags = '{{ sourceTags }}',
targetTags = '{{ targetTags }}',
sourceServiceAccounts = '{{ sourceServiceAccounts }}',
targetServiceAccounts = '{{ targetServiceAccounts }}',
allowed = '{{ allowed }}',
denied = '{{ denied }}',
direction = '{{ direction }}',
logConfig = '{{ logConfig }}',
disabled = true|false
WHERE 
firewall = '{{ firewall }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>firewalls</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.firewalls
WHERE firewall = '{{ firewall }}'
AND project = '{{ project }}';
```
