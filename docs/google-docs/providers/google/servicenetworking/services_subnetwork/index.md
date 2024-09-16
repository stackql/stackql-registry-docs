---
title: services_subnetwork
hide_title: false
hide_table_of_contents: false
keywords:
  - services_subnetwork
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

Creates, updates, deletes, gets or lists a <code>services_subnetwork</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_subnetwork</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.services_subnetwork" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_subnetwork" /> | `INSERT` | <CopyableCode code="servicesId, servicesId1, servicesId2" /> | For service producers, provisions a new subnet in a peered service's shared VPC network in the requested region and with the requested size that's expressed as a CIDR range (number of leading bits of ipV4 network mask). The method checks against the assigned allocated ranges to find a non-conflicting IP address range. The method will reuse a subnet if subsequent calls contain the same subnet name, region, and prefix length. This method will make producer's tenant project to be a shared VPC service project as needed. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services_subnetwork</code> resource.

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
INSERT INTO google.servicenetworking.services_subnetwork (
servicesId,
servicesId1,
servicesId2,
useCustomComputeIdempotencyWindow,
subnetworkUsers,
outsideAllocationPublicIpRange,
role,
purpose,
requestedAddress,
description,
secondaryIpRangeSpecs,
requestedRanges,
consumer,
skipRequestedAddressValidation,
region,
allowSubnetCidrRoutesOverlap,
checkServiceNetworkingUsePermission,
subnetwork,
computeIdempotencyWindow,
consumerNetwork,
privateIpv6GoogleAccess,
ipPrefixLength,
internalRange
)
SELECT 
'{{ servicesId }}',
'{{ servicesId1 }}',
'{{ servicesId2 }}',
true|false,
'{{ subnetworkUsers }}',
'{{ outsideAllocationPublicIpRange }}',
'{{ role }}',
'{{ purpose }}',
'{{ requestedAddress }}',
'{{ description }}',
'{{ secondaryIpRangeSpecs }}',
'{{ requestedRanges }}',
'{{ consumer }}',
true|false,
'{{ region }}',
true|false,
true|false,
'{{ subnetwork }}',
'{{ computeIdempotencyWindow }}',
'{{ consumerNetwork }}',
'{{ privateIpv6GoogleAccess }}',
'{{ ipPrefixLength }}',
'{{ internalRange }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: useCustomComputeIdempotencyWindow
      value: '{{ useCustomComputeIdempotencyWindow }}'
    - name: subnetworkUsers
      value:
        - name: type
          value: '{{ type }}'
    - name: outsideAllocationPublicIpRange
      value: '{{ outsideAllocationPublicIpRange }}'
    - name: role
      value: '{{ role }}'
    - name: purpose
      value: '{{ purpose }}'
    - name: requestedAddress
      value: '{{ requestedAddress }}'
    - name: description
      value: '{{ description }}'
    - name: secondaryIpRangeSpecs
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: requestedRanges
      value:
        - name: type
          value: '{{ type }}'
    - name: consumer
      value: '{{ consumer }}'
    - name: skipRequestedAddressValidation
      value: '{{ skipRequestedAddressValidation }}'
    - name: region
      value: '{{ region }}'
    - name: allowSubnetCidrRoutesOverlap
      value: '{{ allowSubnetCidrRoutesOverlap }}'
    - name: checkServiceNetworkingUsePermission
      value: '{{ checkServiceNetworkingUsePermission }}'
    - name: subnetwork
      value: '{{ subnetwork }}'
    - name: computeIdempotencyWindow
      value: '{{ computeIdempotencyWindow }}'
    - name: consumerNetwork
      value: '{{ consumerNetwork }}'
    - name: privateIpv6GoogleAccess
      value: '{{ privateIpv6GoogleAccess }}'
    - name: ipPrefixLength
      value: '{{ ipPrefixLength }}'
    - name: internalRange
      value: '{{ internalRange }}'

```
</TabItem>
</Tabs>
