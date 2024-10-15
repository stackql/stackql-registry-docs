---
title: graph_resources_graph_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_resources_graph_resources
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>graph_resources_graph_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph_resources_graph_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.graph_resources_graph_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, graphName, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Cosmos DB Graph Resource. |

## `DELETE` example

Deletes the specified <code>graph_resources_graph_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.graph_resources_graph_resources
WHERE accountName = '{{ accountName }}'
AND graphName = '{{ graphName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
