---
title: workspace_collections_by_names
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_collections_by_names
  - powerbi_embedded
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

Creates, updates, deletes, gets or lists a <code>workspace_collections_by_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_collections_by_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_embedded.workspace_collections_by_names" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource id |
| <CopyableCode code="name" /> | `string` | Workspace collection name |
| <CopyableCode code="location" /> | `string` | Azure location |
| <CopyableCode code="properties" /> | `object` | Properties |
| <CopyableCode code="sku" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Retrieves an existing Power BI Workspace Collection. |

## `SELECT` examples

Retrieves an existing Power BI Workspace Collection.


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure.powerbi_embedded.workspace_collections_by_names
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceCollectionName = '{{ workspaceCollectionName }}';
```