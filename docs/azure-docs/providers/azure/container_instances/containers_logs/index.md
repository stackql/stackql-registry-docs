---
title: containers_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - containers_logs
  - container_instances
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

Creates, updates, deletes, gets or lists a <code>containers_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.containers_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `string` | The content of the log. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerGroupName, containerName, resourceGroupName, subscriptionId" /> | Get the logs for a specified container instance in a specified resource group and container group. |

## `SELECT` examples

Get the logs for a specified container instance in a specified resource group and container group.


```sql
SELECT
content
FROM azure.container_instances.containers_logs
WHERE containerGroupName = '{{ containerGroupName }}'
AND containerName = '{{ containerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```