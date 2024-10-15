---
title: disk_accesses_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses_private_endpoint_connections
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

Creates, updates, deletes, gets or lists a <code>disk_accesses_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_accesses_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_accesses_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | private endpoint connection Id |
| <CopyableCode code="name" /> | `string` | private endpoint connection name |
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="type" /> | `string` | private endpoint connection type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | List information about private endpoint connections under a disk access resource |

## `SELECT` examples

List information about private endpoint connections under a disk access resource


```sql
SELECT
id,
name,
properties,
type
FROM azure.compute.disk_accesses_private_endpoint_connections
WHERE diskAccessName = '{{ diskAccessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```