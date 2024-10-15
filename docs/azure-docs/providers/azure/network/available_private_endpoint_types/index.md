---
title: available_private_endpoint_types
hide_title: false
hide_table_of_contents: false
keywords:
  - available_private_endpoint_types
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

Creates, updates, deletes, gets or lists a <code>available_private_endpoint_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_private_endpoint_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.available_private_endpoint_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique identifier of the AvailablePrivateEndpoint Type resource. |
| <CopyableCode code="name" /> | `string` | The name of the service and resource. |
| <CopyableCode code="displayName" /> | `string` | Display name of the resource. |
| <CopyableCode code="resourceName" /> | `string` | The name of the service and resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns all of the resource types that can be linked to a Private Endpoint in this subscription in this region. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns all of the resource types that can be linked to a Private Endpoint in this subscription in this region. |

## `SELECT` examples

Returns all of the resource types that can be linked to a Private Endpoint in this subscription in this region.


```sql
SELECT
id,
name,
displayName,
resourceName,
type
FROM azure.network.available_private_endpoint_types
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```