---
title: integration_runtime_starts
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_starts
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

Creates, updates, deletes, gets or lists a <code>integration_runtime_starts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_starts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtime_starts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="error" /> | `string` | The operation error message. |
| <CopyableCode code="properties" /> | `object` | The operation properties. |
| <CopyableCode code="status" /> | `string` | status of Start Integrationruntimes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, integrationRuntimeOperationId, resourceGroupName, subscriptionId, workspaceName" /> | Get an integration runtime start operation status |

## `SELECT` examples

Get an integration runtime start operation status


```sql
SELECT
name,
error,
properties,
status
FROM azure.synapse.integration_runtime_starts
WHERE integrationRuntimeName = '{{ integrationRuntimeName }}'
AND integrationRuntimeOperationId = '{{ integrationRuntimeOperationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```