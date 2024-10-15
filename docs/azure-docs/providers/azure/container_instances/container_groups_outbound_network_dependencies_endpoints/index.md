---
title: container_groups_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - container_groups_outbound_network_dependencies_endpoints
  - container_instances
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

Creates, updates, deletes, gets or lists a <code>container_groups_outbound_network_dependencies_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_groups_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.container_groups_outbound_network_dependencies_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Gets all the network dependencies for this container group to allow complete control of network setting and configuration. For container groups, this will always be an empty list. |

## `SELECT` examples

Gets all the network dependencies for this container group to allow complete control of network setting and configuration. For container groups, this will always be an empty list.


```sql
SELECT
column_anon
FROM azure.container_instances.container_groups_outbound_network_dependencies_endpoints
WHERE containerGroupName = '{{ containerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```