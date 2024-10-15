---
title: managed_database_recommended_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_recommended_sensitivity_labels
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

Creates, updates, deletes, gets or lists a <code>managed_database_recommended_sensitivity_labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_recommended_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_recommended_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Update recommended sensitivity labels states of a given database using an operations batch. |

## `UPDATE` example

Updates a <code>managed_database_recommended_sensitivity_labels</code> resource.

```sql
/*+ update */
UPDATE azure.sql.managed_database_recommended_sensitivity_labels
SET 
operations = '{{ operations }}'
WHERE 
databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
