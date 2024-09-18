---
title: subnetworks
hide_title: false
hide_table_of_contents: false
keywords:
  - subnetworks
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

Creates, updates, deletes, gets or lists a <code>subnetworks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnetworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.subnetworks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. This field can be set only at resource creation time. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="enableFlowLogs" /> | `boolean` | Whether to enable flow logging for this subnetwork. If this field is not explicitly set, it will not appear in get listings. If not set the default behavior is determined by the org policy, if there is no org policy specified, then it will default to disabled. This field isn't supported if the subnet purpose field is set to REGIONAL_MANAGED_PROXY. |
| <CopyableCode code="externalIpv6Prefix" /> | `string` | The external IPv6 address range that is owned by this subnetwork. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a Subnetwork. An up-to-date fingerprint must be provided in order to update the Subnetwork, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a Subnetwork. |
| <CopyableCode code="gatewayAddress" /> | `string` | [Output Only] The gateway address for default routes to reach destination addresses outside this subnetwork. |
| <CopyableCode code="internalIpv6Prefix" /> | `string` | The internal IPv6 address range that is owned by this subnetwork. |
| <CopyableCode code="ipCidrRange" /> | `string` | The range of internal addresses that are owned by this subnetwork. Provide this property when you create the subnetwork. For example, 10.0.0.0/8 or 100.64.0.0/10. Ranges must be unique and non-overlapping within a network. Only IPv4 is supported. This field is set at resource creation time. The range can be any range listed in the Valid ranges list. The range can be expanded after creation using expandIpCidrRange. |
| <CopyableCode code="ipv6AccessType" /> | `string` | The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. |
| <CopyableCode code="ipv6CidrRange" /> | `string` | [Output Only] This field is for internal use. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#subnetwork for Subnetwork resources. |
| <CopyableCode code="logConfig" /> | `object` | The available logging options for this subnetwork. |
| <CopyableCode code="network" /> | `string` | The URL of the network to which this subnetwork belongs, provided by the client when initially creating the subnetwork. This field can be set only at resource creation time. |
| <CopyableCode code="privateIpGoogleAccess" /> | `boolean` | Whether the VMs in this subnet can access Google services without assigned external IP addresses. This field can be both set at resource creation time and updated using setPrivateIpGoogleAccess. |
| <CopyableCode code="privateIpv6GoogleAccess" /> | `string` | This field is for internal use. This field can be both set at resource creation time and updated using patch. |
| <CopyableCode code="purpose" /> | `string` | The purpose of the resource. This field can be either PRIVATE, GLOBAL_MANAGED_PROXY, REGIONAL_MANAGED_PROXY, PRIVATE_SERVICE_CONNECT, or PRIVATE is the default purpose for user-created subnets or subnets that are automatically created in auto mode networks. Subnets with purpose set to GLOBAL_MANAGED_PROXY or REGIONAL_MANAGED_PROXY are user-created subnetworks that are reserved for Envoy-based load balancers. A subnet with purpose set to PRIVATE_SERVICE_CONNECT is used to publish services using Private Service Connect. If unspecified, the subnet purpose defaults to PRIVATE. The enableFlowLogs field isn't supported if the subnet purpose field is set to GLOBAL_MANAGED_PROXY or REGIONAL_MANAGED_PROXY. |
| <CopyableCode code="region" /> | `string` | URL of the region where the Subnetwork resides. This field can be set only at resource creation time. |
| <CopyableCode code="reservedInternalRange" /> | `string` | The URL of the reserved internal range. |
| <CopyableCode code="role" /> | `string` | The role of subnetwork. Currently, this field is only used when purpose is set to GLOBAL_MANAGED_PROXY or REGIONAL_MANAGED_PROXY. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Envoy-based load balancers in a region. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. |
| <CopyableCode code="secondaryIpRanges" /> | `array` | An array of configurations for secondary IP ranges for VM instances contained in this subnetwork. The primary IP of such VM must belong to the primary ipCidrRange of the subnetwork. The alias IPs may belong to either primary or secondary ranges. This field can be updated with a patch request. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="stackType" /> | `string` | The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set to IPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used. This field can be both set at resource creation time and updated using patch. |
| <CopyableCode code="state" /> | `string` | [Output Only] The state of the subnetwork, which can be one of the following values: READY: Subnetwork is created and ready to use DRAINING: only applicable to subnetworks that have the purpose set to INTERNAL_HTTPS_LOAD_BALANCER and indicates that connections to the load balancer are being drained. A subnetwork that is draining cannot be used or modified until it reaches a status of READY |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of subnetworks. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, subnetwork" /> | Returns the specified subnetwork. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of subnetworks available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a subnetwork in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, subnetwork" /> | Deletes the specified subnetwork. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, region, subnetwork" /> | Patches the specified subnetwork with the data included in the request. Only certain fields can be updated with a patch request as indicated in the field descriptions. You must specify the current fingerprint of the subnetwork resource being patched. |
| <CopyableCode code="expand_ip_cidr_range" /> | `EXEC` | <CopyableCode code="project, region, subnetwork" /> | Expands the IP CIDR range of the subnetwork to a specified value. |
| <CopyableCode code="set_private_ip_google_access" /> | `EXEC` | <CopyableCode code="project, region, subnetwork" /> | Set whether VMs in this subnet can access Google services without assigning external IP addresses through Private Google Access. |

## `SELECT` examples

Retrieves an aggregated list of subnetworks. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
creationTimestamp,
enableFlowLogs,
externalIpv6Prefix,
fingerprint,
gatewayAddress,
internalIpv6Prefix,
ipCidrRange,
ipv6AccessType,
ipv6CidrRange,
kind,
logConfig,
network,
privateIpGoogleAccess,
privateIpv6GoogleAccess,
purpose,
region,
reservedInternalRange,
role,
secondaryIpRanges,
selfLink,
stackType,
state
FROM google.compute.subnetworks
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subnetworks</code> resource.

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
INSERT INTO google.compute.subnetworks (
project,
region,
name,
description,
network,
ipCidrRange,
reservedInternalRange,
gatewayAddress,
region,
privateIpGoogleAccess,
secondaryIpRanges,
fingerprint,
enableFlowLogs,
privateIpv6GoogleAccess,
ipv6CidrRange,
externalIpv6Prefix,
internalIpv6Prefix,
purpose,
role,
state,
logConfig,
stackType,
ipv6AccessType
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ network }}',
'{{ ipCidrRange }}',
'{{ reservedInternalRange }}',
'{{ gatewayAddress }}',
'{{ region }}',
true|false,
'{{ secondaryIpRanges }}',
'{{ fingerprint }}',
true|false,
'{{ privateIpv6GoogleAccess }}',
'{{ ipv6CidrRange }}',
'{{ externalIpv6Prefix }}',
'{{ internalIpv6Prefix }}',
'{{ purpose }}',
'{{ role }}',
'{{ state }}',
'{{ logConfig }}',
'{{ stackType }}',
'{{ ipv6AccessType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
kind: string
id: string
creationTimestamp: string
name: string
description: string
network: string
ipCidrRange: string
reservedInternalRange: string
gatewayAddress: string
region: string
selfLink: string
privateIpGoogleAccess: boolean
secondaryIpRanges:
  - rangeName: string
    ipCidrRange: string
    reservedInternalRange: string
fingerprint: string
enableFlowLogs: boolean
privateIpv6GoogleAccess: string
ipv6CidrRange: string
externalIpv6Prefix: string
internalIpv6Prefix: string
purpose: string
role: string
state: string
logConfig:
  enable: boolean
  aggregationInterval: string
  flowSampling: number
  metadata: string
  metadataFields:
    - type: string
  filterExpr: string
stackType: string
ipv6AccessType: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>subnetworks</code> resource.

```sql
/*+ update */
UPDATE google.compute.subnetworks
SET 
name = '{{ name }}',
description = '{{ description }}',
network = '{{ network }}',
ipCidrRange = '{{ ipCidrRange }}',
reservedInternalRange = '{{ reservedInternalRange }}',
gatewayAddress = '{{ gatewayAddress }}',
region = '{{ region }}',
privateIpGoogleAccess = true|false,
secondaryIpRanges = '{{ secondaryIpRanges }}',
fingerprint = '{{ fingerprint }}',
enableFlowLogs = true|false,
privateIpv6GoogleAccess = '{{ privateIpv6GoogleAccess }}',
ipv6CidrRange = '{{ ipv6CidrRange }}',
externalIpv6Prefix = '{{ externalIpv6Prefix }}',
internalIpv6Prefix = '{{ internalIpv6Prefix }}',
purpose = '{{ purpose }}',
role = '{{ role }}',
state = '{{ state }}',
logConfig = '{{ logConfig }}',
stackType = '{{ stackType }}',
ipv6AccessType = '{{ ipv6AccessType }}'
WHERE 
project = '{{ project }}'
AND region = '{{ region }}'
AND subnetwork = '{{ subnetwork }}';
```

## `DELETE` example

Deletes the specified <code>subnetworks</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.subnetworks
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND subnetwork = '{{ subnetwork }}';
```
