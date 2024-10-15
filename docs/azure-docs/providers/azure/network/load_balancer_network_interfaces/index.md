---
title: load_balancer_network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_network_interfaces
  - network
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

Creates, updates, deletes, gets or lists a <code>load_balancer_network_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_network_interfaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | NetworkInterface properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets associated load balancer network interfaces. |

## `SELECT` examples

Gets associated load balancer network interfaces.


```sql
SELECT
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type
FROM azure.network.load_balancer_network_interfaces
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```