---
title: subnetworks_usable
hide_title: false
hide_table_of_contents: false
keywords:
  - subnetworks_usable
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

Creates, updates, deletes, gets or lists a <code>subnetworks_usable</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnetworks_usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.subnetworks_usable" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="externalIpv6Prefix" /> | `string` | [Output Only] The external IPv6 address range that is assigned to this subnetwork. |
| <CopyableCode code="internalIpv6Prefix" /> | `string` | [Output Only] The internal IPv6 address range that is assigned to this subnetwork. |
| <CopyableCode code="ipCidrRange" /> | `string` | The range of internal addresses that are owned by this subnetwork. |
| <CopyableCode code="ipv6AccessType" /> | `string` | The access type of IPv6 address this subnet holds. It's immutable and can only be specified during creation or the first time the subnet is updated into IPV4_IPV6 dual stack. |
| <CopyableCode code="network" /> | `string` | Network URL. |
| <CopyableCode code="purpose" /> | `string` | The purpose of the resource. This field can be either PRIVATE, GLOBAL_MANAGED_PROXY, REGIONAL_MANAGED_PROXY, PRIVATE_SERVICE_CONNECT, or PRIVATE is the default purpose for user-created subnets or subnets that are automatically created in auto mode networks. Subnets with purpose set to GLOBAL_MANAGED_PROXY or REGIONAL_MANAGED_PROXY are user-created subnetworks that are reserved for Envoy-based load balancers. A subnet with purpose set to PRIVATE_SERVICE_CONNECT is used to publish services using Private Service Connect. If unspecified, the subnet purpose defaults to PRIVATE. The enableFlowLogs field isn't supported if the subnet purpose field is set to GLOBAL_MANAGED_PROXY or REGIONAL_MANAGED_PROXY. |
| <CopyableCode code="role" /> | `string` | The role of subnetwork. Currently, this field is only used when purpose is set to GLOBAL_MANAGED_PROXY or REGIONAL_MANAGED_PROXY. The value can be set to ACTIVE or BACKUP. An ACTIVE subnetwork is one that is currently being used for Envoy-based load balancers in a region. A BACKUP subnetwork is one that is ready to be promoted to ACTIVE or is currently draining. This field can be updated with a patch request. |
| <CopyableCode code="secondaryIpRanges" /> | `array` | Secondary IP ranges. |
| <CopyableCode code="stackType" /> | `string` | The stack type for the subnet. If set to IPV4_ONLY, new VMs in the subnet are assigned IPv4 addresses only. If set to IPV4_IPV6, new VMs in the subnet can be assigned both IPv4 and IPv6 addresses. If not specified, IPV4_ONLY is used. This field can be both set at resource creation time and updated using patch. |
| <CopyableCode code="subnetwork" /> | `string` | Subnetwork URL. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_usable" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of all usable subnetworks in the project. |

## `SELECT` examples

Retrieves an aggregated list of all usable subnetworks in the project.

```sql
SELECT
externalIpv6Prefix,
internalIpv6Prefix,
ipCidrRange,
ipv6AccessType,
network,
purpose,
role,
secondaryIpRanges,
stackType,
subnetwork
FROM google.compute.subnetworks_usable
WHERE project = '{{ project }}';
```
