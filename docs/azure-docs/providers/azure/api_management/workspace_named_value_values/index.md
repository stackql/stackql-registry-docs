---
title: workspace_named_value_values
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_named_value_values
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_named_value_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_named_value_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_named_value_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `string` | This is secret value of the NamedValue entity. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the secret of the named value specified by its identifier. |

## `SELECT` examples

Gets the secret of the named value specified by its identifier.


```sql
SELECT
value
FROM azure.api_management.workspace_named_value_values
WHERE namedValueId = '{{ namedValueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```