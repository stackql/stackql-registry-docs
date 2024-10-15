---
title: recommended_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_sensitivity_labels
  - sql
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

Creates, updates, deletes, gets or lists a <code>recommended_sensitivity_labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommended_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.recommended_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Update recommended sensitivity labels states of a given database using an operations batch. |

## `UPDATE` example

Updates a <code>recommended_sensitivity_labels</code> resource.

```sql
/*+ update */
UPDATE azure.sql.recommended_sensitivity_labels
SET 
operations = '{{ operations }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
