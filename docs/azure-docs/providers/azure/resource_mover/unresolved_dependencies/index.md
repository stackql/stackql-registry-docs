---
title: unresolved_dependencies
hide_title: false
hide_table_of_contents: false
keywords:
  - unresolved_dependencies
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

Creates, updates, deletes, gets or lists a <code>unresolved_dependencies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>unresolved_dependencies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.unresolved_dependencies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the arm id of the dependency. |
| <CopyableCode code="count" /> | `integer` | Gets or sets the count. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Gets a list of unresolved dependencies. |

## `SELECT` examples

Gets a list of unresolved dependencies.


```sql
SELECT
id,
count
FROM azure.resource_mover.unresolved_dependencies
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```