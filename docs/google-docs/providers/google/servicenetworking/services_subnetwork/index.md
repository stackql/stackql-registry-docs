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
role,
ipPrefixLength,
skipRequestedAddressValidation,
consumerNetwork,
internalRange,
secondaryIpRangeSpecs,
description,
useCustomComputeIdempotencyWindow,
requestedRanges,
allowSubnetCidrRoutesOverlap,
computeIdempotencyWindow,
subnetwork,
requestedAddress,
outsideAllocationPublicIpRange,
privateIpv6GoogleAccess,
consumer,
subnetworkUsers,
purpose,
region,
checkServiceNetworkingUsePermission
)
SELECT 
'{{ servicesId }}',
'{{ servicesId1 }}',
'{{ servicesId2 }}',
'{{ role }}',
'{{ ipPrefixLength }}',
{{ skipRequestedAddressValidation }},
'{{ consumerNetwork }}',
'{{ internalRange }}',
'{{ secondaryIpRangeSpecs }}',
'{{ description }}',
{{ useCustomComputeIdempotencyWindow }},
'{{ requestedRanges }}',
{{ allowSubnetCidrRoutesOverlap }},
'{{ computeIdempotencyWindow }}',
'{{ subnetwork }}',
'{{ requestedAddress }}',
'{{ outsideAllocationPublicIpRange }}',
'{{ privateIpv6GoogleAccess }}',
'{{ consumer }}',
'{{ subnetworkUsers }}',
'{{ purpose }}',
'{{ region }}',
{{ checkServiceNetworkingUsePermission }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: role
      value: string
    - name: ipPrefixLength
      value: integer
    - name: skipRequestedAddressValidation
      value: boolean
    - name: consumerNetwork
      value: string
    - name: internalRange
      value: string
    - name: secondaryIpRangeSpecs
      value:
        - - name: ipPrefixLength
            value: integer
          - name: outsideAllocationPublicIpRange
            value: string
          - name: requestedAddress
            value: string
          - name: rangeName
            value: string
    - name: description
      value: string
    - name: useCustomComputeIdempotencyWindow
      value: boolean
    - name: requestedRanges
      value:
        - string
    - name: allowSubnetCidrRoutesOverlap
      value: boolean
    - name: computeIdempotencyWindow
      value: string
    - name: subnetwork
      value: string
    - name: requestedAddress
      value: string
    - name: outsideAllocationPublicIpRange
      value: string
    - name: privateIpv6GoogleAccess
      value: string
    - name: consumer
      value: string
    - name: subnetworkUsers
      value:
        - string
    - name: purpose
      value: string
    - name: region
      value: string
    - name: checkServiceNetworkingUsePermission
      value: boolean

```
</TabItem>
</Tabs>
