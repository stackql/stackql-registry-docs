
---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
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

Creates, updates, deletes or gets an <code>connection</code> resource or lists <code>connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connections" /> | `array` | The list of Connections. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="servicesId" /> | List the private connections that are configured in a service consumer's VPC network. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="servicesId" /> | Creates a private connection that establishes a VPC Network Peering connection to a VPC network in the service producer's organization. The administrator of the service consumer's VPC network invokes this method. The administrator must assign one or more allocated IP ranges for provisioning subnetworks in the service producer's VPC network. This connection is used for all supported services in the service producer's organization, so it only needs to be invoked once. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectionsId, servicesId" /> | Updates the allocated ranges that are assigned to a connection. |

## `SELECT` examples

List the private connections that are configured in a service consumer's VPC network.

```sql
SELECT
connections
FROM google.servicenetworking.connections
WHERE servicesId = '{{ servicesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO google.servicenetworking.connections (
servicesId,
peering,
reservedPeeringRanges,
service,
network
)
SELECT 
'{{ servicesId }}',
'{{ peering }}',
'{{ reservedPeeringRanges }}',
'{{ service }}',
'{{ network }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: peering
        value: '{{ peering }}'
      - name: reservedPeeringRanges
        value: '{{ reservedPeeringRanges }}'
      - name: service
        value: '{{ service }}'
      - name: network
        value: '{{ network }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a connection only if the necessary resources are available.

```sql
UPDATE google.servicenetworking.connections
SET 
peering = '{{ peering }}',
reservedPeeringRanges = '{{ reservedPeeringRanges }}',
service = '{{ service }}',
network = '{{ network }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND servicesId = '{{ servicesId }}';
```
