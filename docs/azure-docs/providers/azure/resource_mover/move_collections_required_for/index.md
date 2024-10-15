---
title: move_collections_required_for
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections_required_for
  - resource_mover
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

Creates, updates, deletes, gets or lists a <code>move_collections_required_for</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>move_collections_required_for</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.move_collections_required_for" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="sourceIds" /> | `array` | Gets or sets the list of source Ids for which the input resource is required. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="moveCollectionName, resourceGroupName, sourceId, subscriptionId" /> | List of the move resources for which an arm resource is required for. |

## `SELECT` examples

List of the move resources for which an arm resource is required for.


```sql
SELECT
sourceIds
FROM azure.resource_mover.move_collections_required_for
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceId = '{{ sourceId }}'
AND subscriptionId = '{{ subscriptionId }}';
```