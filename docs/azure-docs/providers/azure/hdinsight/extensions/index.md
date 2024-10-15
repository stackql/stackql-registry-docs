---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
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

Creates, updates, deletes, gets or lists a <code>extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterMonitoringEnabled" /> | `boolean` | The status of the monitor on the HDInsight cluster. |
| <CopyableCode code="workspaceId" /> | `string` | The workspace ID of the monitor on the HDInsight cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, extensionName, resourceGroupName, subscriptionId" /> | Gets the extension properties for the specified HDInsight cluster extension. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, extensionName, resourceGroupName, subscriptionId" /> | Creates an HDInsight cluster extension. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, extensionName, resourceGroupName, subscriptionId" /> | Deletes the specified extension for HDInsight cluster. |
| <CopyableCode code="disable_azure_monitor" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Disables the Azure Monitor on the HDInsight cluster. |
| <CopyableCode code="disable_azure_monitor_agent" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Disables the Azure Monitor Agent on the HDInsight cluster. |
| <CopyableCode code="disable_monitoring" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Disables the Operations Management Suite (OMS) on the HDInsight cluster. |
| <CopyableCode code="enable_azure_monitor" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Enables the Azure Monitor on the HDInsight cluster. |
| <CopyableCode code="enable_azure_monitor_agent" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Enables the Azure Monitor Agent on the HDInsight cluster. |
| <CopyableCode code="enable_monitoring" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Enables the Operations Management Suite (OMS) on the HDInsight cluster. |

## `SELECT` examples

Gets the extension properties for the specified HDInsight cluster extension.


```sql
SELECT
clusterMonitoringEnabled,
workspaceId
FROM azure.hdinsight.extensions
WHERE clusterName = '{{ clusterName }}'
AND extensionName = '{{ extensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>extensions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.hdinsight.extensions (
clusterName,
extensionName,
resourceGroupName,
subscriptionId,
workspaceId,
primaryKey
)
SELECT 
'{{ clusterName }}',
'{{ extensionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
'{{ primaryKey }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: workspaceId
      value: string
    - name: primaryKey
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hdinsight.extensions
WHERE clusterName = '{{ clusterName }}'
AND extensionName = '{{ extensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
