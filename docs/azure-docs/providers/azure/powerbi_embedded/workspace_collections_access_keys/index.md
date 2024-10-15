---
title: workspace_collections_access_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_collections_access_keys
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

Creates, updates, deletes, gets or lists a <code>workspace_collections_access_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_collections_access_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_embedded.workspace_collections_access_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key1" /> | `string` | Access key 1 |
| <CopyableCode code="key2" /> | `string` | Access key 2 |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Retrieves the primary and secondary access keys for the specified Power BI Workspace Collection. |

## `SELECT` examples

Retrieves the primary and secondary access keys for the specified Power BI Workspace Collection.


```sql
SELECT
key1,
key2
FROM azure.powerbi_embedded.workspace_collections_access_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceCollectionName = '{{ workspaceCollectionName }}';
```