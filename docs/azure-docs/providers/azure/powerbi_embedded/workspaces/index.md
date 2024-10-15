---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
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

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_embedded.workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Workspace id |
| <CopyableCode code="name" /> | `string` | Workspace name |
| <CopyableCode code="properties" /> | `object` | Property bag |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> | Retrieves all existing Power BI workspaces in the specified workspace collection. |

## `SELECT` examples

Retrieves all existing Power BI workspaces in the specified workspace collection.


```sql
SELECT
id,
name,
properties,
type
FROM azure.powerbi_embedded.workspaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceCollectionName = '{{ workspaceCollectionName }}';
```