---
title: sql_pool_recommended_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_recommended_sensitivity_labels
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_recommended_sensitivity_labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_recommended_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_recommended_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Update recommended sensitivity labels states of a given SQL Pool using an operations batch. |

## `UPDATE` example

Updates a <code>sql_pool_recommended_sensitivity_labels</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.sql_pool_recommended_sensitivity_labels
SET 
operations = '{{ operations }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
