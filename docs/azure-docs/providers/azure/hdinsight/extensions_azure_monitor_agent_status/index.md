---
title: extensions_azure_monitor_agent_status
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions_azure_monitor_agent_status
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>extensions_azure_monitor_agent_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions_azure_monitor_agent_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.extensions_azure_monitor_agent_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterMonitoringEnabled" /> | `boolean` | The status of the monitor on the HDInsight cluster. |
| <CopyableCode code="selectedConfigurations" /> | `object` | The selected configurations for azure monitor. |
| <CopyableCode code="workspaceId" /> | `string` | The workspace ID of the monitor on the HDInsight cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets the status of Azure Monitor Agent on the HDInsight cluster. |

## `SELECT` examples

Gets the status of Azure Monitor Agent on the HDInsight cluster.


```sql
SELECT
clusterMonitoringEnabled,
selectedConfigurations,
workspaceId
FROM azure.hdinsight.extensions_azure_monitor_agent_status
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```