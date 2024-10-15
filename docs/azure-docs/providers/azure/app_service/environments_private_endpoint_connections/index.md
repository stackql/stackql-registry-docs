---
title: environments_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_private_endpoint_connections
  - app_service
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

Creates, updates, deletes, gets or lists a <code>environments_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.environments_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | RemotePrivateEndpointConnectionARMResource resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Description for Gets a private endpoint connection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Description for Deletes a private endpoint connection |

## `SELECT` examples

Description for Gets a private endpoint connection


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.environments_private_endpoint_connections
WHERE name = '{{ name }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `DELETE` example

Deletes the specified <code>environments_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.environments_private_endpoint_connections
WHERE name = '{{ name }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
