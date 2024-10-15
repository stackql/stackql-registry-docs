---
title: spark_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - spark_configurations
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

Creates, updates, deletes, gets or lists a <code>spark_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spark_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.spark_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_spark_configurations', value: 'view', },
        { label: 'spark_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotations" /> | `text` | field from the `properties` object |
| <CopyableCode code="config_merge_rule" /> | `text` | field from the `properties` object |
| <CopyableCode code="configs" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sparkConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SparkConfiguration Artifact information |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sparkConfigurationName, subscriptionId, workspaceName" /> | Get SparkConfiguration by name in a workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List sparkConfigurations in a workspace. |

## `SELECT` examples

List sparkConfigurations in a workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_spark_configurations', value: 'view', },
        { label: 'spark_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
annotations,
config_merge_rule,
configs,
created,
created_by,
notes,
resourceGroupName,
sparkConfigurationName,
subscriptionId,
workspaceName
FROM azure.synapse.vw_spark_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.spark_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

