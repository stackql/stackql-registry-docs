
---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
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

Creates, updates, deletes or gets an <code>network</code> resource or lists <code>networks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this field when you create the resource. |
| <CopyableCode code="IPv4Range" /> | `string` | Deprecated in favor of subnet mode networks. The range of internal addresses that are legal on this network. This range is a CIDR specification, for example: 192.168.0.0/16. Provided by the client when the network is created. |
| <CopyableCode code="autoCreateSubnetworks" /> | `boolean` | Must be set to create a VPC network. If not set, a legacy network is created. When set to true, the VPC network is created in auto mode. When set to false, the VPC network is created in custom mode. An auto mode VPC network starts with one subnet per region. Each subnet has a predetermined range as described in Auto mode VPC network IP ranges. For custom mode VPC networks, you can add subnets using the subnetworks insert method. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="enableUlaInternalIpv6" /> | `boolean` | Enable ULA internal ipv6 on this network. Enabling this feature will assign a /48 from google defined ULA prefix fd20::/20. . |
| <CopyableCode code="firewallPolicy" /> | `string` | [Output Only] URL of the firewall policy the network is associated with. |
| <CopyableCode code="gatewayIPv4" /> | `string` | [Output Only] The gateway address for default routing out of the network, selected by Google Cloud. |
| <CopyableCode code="internalIpv6Range" /> | `string` | When enabling ula internal ipv6, caller optionally can specify the /48 range they want from the google defined ULA prefix fd20::/20. The input must be a valid /48 ULA IPv6 address and must be within the fd20::/20. Operation will fail if the speficied /48 is already in used by another resource. If the field is not speficied, then a /48 range will be randomly allocated from fd20::/20 and returned via this field. . |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#network for networks. |
| <CopyableCode code="mtu" /> | `integer` | Maximum Transmission Unit in bytes. The minimum value for this field is 1300 and the maximum value is 8896. The suggested value is 1500, which is the default MTU used on the Internet, or 8896 if you want to use Jumbo frames. If unspecified, the value defaults to 1460. |
| <CopyableCode code="networkFirewallPolicyEnforcementOrder" /> | `string` | The network firewall policy enforcement order. Can be either AFTER_CLASSIC_FIREWALL or BEFORE_CLASSIC_FIREWALL. Defaults to AFTER_CLASSIC_FIREWALL if the field is not specified. |
| <CopyableCode code="peerings" /> | `array` | [Output Only] A list of network peerings for the resource. |
| <CopyableCode code="routingConfig" /> | `object` | A routing configuration attached to a network resource. The message includes the list of routers associated with the network, and a flag indicating the type of routing behavior to enforce network-wide. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL for this resource with the resource id. |
| <CopyableCode code="subnetworks" /> | `array` | [Output Only] Server-defined fully-qualified URLs for all subnetworks in this VPC network. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="network, project" /> | Returns the specified network. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of networks available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a network in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="network, project" /> | Deletes the specified network. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="network, project" /> | Patches the specified network with the data included in the request. Only routingConfig can be modified. |
| <CopyableCode code="switch_to_custom_mode" /> | `EXEC` | <CopyableCode code="network, project" /> | Switches the network mode from auto subnet mode to custom subnet mode. |

## `SELECT` examples

Retrieves the list of networks available to the specified project.

```sql
SELECT
id,
name,
description,
IPv4Range,
autoCreateSubnetworks,
creationTimestamp,
enableUlaInternalIpv6,
firewallPolicy,
gatewayIPv4,
internalIpv6Range,
kind,
mtu,
networkFirewallPolicyEnforcementOrder,
peerings,
routingConfig,
selfLink,
selfLinkWithId,
subnetworks
FROM google.compute.networks
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>networks</code> resource.

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
INSERT INTO google.compute.networks (
project,
kind,
id,
creationTimestamp,
name,
description,
IPv4Range,
gatewayIPv4,
selfLink,
selfLinkWithId,
autoCreateSubnetworks,
subnetworks,
peerings,
routingConfig,
mtu,
firewallPolicy,
networkFirewallPolicyEnforcementOrder,
enableUlaInternalIpv6,
internalIpv6Range
)
SELECT 
'{{ project }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ IPv4Range }}',
'{{ gatewayIPv4 }}',
'{{ selfLink }}',
'{{ selfLinkWithId }}',
true|false,
'{{ subnetworks }}',
'{{ peerings }}',
'{{ routingConfig }}',
'{{ mtu }}',
'{{ firewallPolicy }}',
'{{ networkFirewallPolicyEnforcementOrder }}',
true|false,
'{{ internalIpv6Range }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: IPv4Range
        value: '{{ IPv4Range }}'
      - name: gatewayIPv4
        value: '{{ gatewayIPv4 }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: selfLinkWithId
        value: '{{ selfLinkWithId }}'
      - name: autoCreateSubnetworks
        value: '{{ autoCreateSubnetworks }}'
      - name: subnetworks
        value: '{{ subnetworks }}'
      - name: peerings
        value: '{{ peerings }}'
      - name: routingConfig
        value: '{{ routingConfig }}'
      - name: mtu
        value: '{{ mtu }}'
      - name: firewallPolicy
        value: '{{ firewallPolicy }}'
      - name: networkFirewallPolicyEnforcementOrder
        value: '{{ networkFirewallPolicyEnforcementOrder }}'
      - name: enableUlaInternalIpv6
        value: '{{ enableUlaInternalIpv6 }}'
      - name: internalIpv6Range
        value: '{{ internalIpv6Range }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a network only if the necessary resources are available.

```sql
UPDATE google.compute.networks
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
IPv4Range = '{{ IPv4Range }}',
gatewayIPv4 = '{{ gatewayIPv4 }}',
selfLink = '{{ selfLink }}',
selfLinkWithId = '{{ selfLinkWithId }}',
autoCreateSubnetworks = true|false,
subnetworks = '{{ subnetworks }}',
peerings = '{{ peerings }}',
routingConfig = '{{ routingConfig }}',
mtu = '{{ mtu }}',
firewallPolicy = '{{ firewallPolicy }}',
networkFirewallPolicyEnforcementOrder = '{{ networkFirewallPolicyEnforcementOrder }}',
enableUlaInternalIpv6 = true|false,
internalIpv6Range = '{{ internalIpv6Range }}'
WHERE 
network = '{{ network }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified network resource.

```sql
DELETE FROM google.compute.networks
WHERE network = '{{ network }}'
AND project = '{{ project }}';
```
