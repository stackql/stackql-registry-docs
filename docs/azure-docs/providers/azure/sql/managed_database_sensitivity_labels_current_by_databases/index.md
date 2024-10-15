---
title: managed_database_sensitivity_labels_current_by_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_sensitivity_labels_current_by_databases
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

Creates, updates, deletes, gets or lists a <code>managed_database_sensitivity_labels_current_by_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_sensitivity_labels_current_by_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_sensitivity_labels_current_by_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Resource that manages the sensitivity label. |
| <CopyableCode code="properties" /> | `object` | Properties of a sensitivity label. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets the sensitivity labels of a given database |

## `SELECT` examples

Gets the sensitivity labels of a given database


```sql
SELECT
managedBy,
properties
FROM azure.sql.managed_database_sensitivity_labels_current_by_databases
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```