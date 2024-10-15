---
title: analysis_results
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_results
  - test_base
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

Creates, updates, deletes, gets or lists a <code>analysis_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.analysis_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_analysis_results', value: 'view', },
        { label: 'analysis_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="analysisResultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="analysisResultType" /> | `text` | field from the `properties` object |
| <CopyableCode code="analysis_result_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="grade" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="testResultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of Analysis Result resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="analysisResultName, packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName" /> | Gets an Analysis Result of a Test Result by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="analysisResultType, packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName" /> | Lists the Analysis Results of a Test Result. The result collection will only contain one element as all the data will be nested in a singleton object. |

## `SELECT` examples

Gets an Analysis Result of a Test Result by name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_analysis_results', value: 'view', },
        { label: 'analysis_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
analysisResultName,
analysisResultType,
analysis_result_type,
grade,
packageName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
testResultName
FROM azure_extras.test_base.vw_analysis_results
WHERE analysisResultName = '{{ analysisResultName }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}'
AND testResultName = '{{ testResultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.analysis_results
WHERE analysisResultName = '{{ analysisResultName }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}'
AND testResultName = '{{ testResultName }}';
```
</TabItem></Tabs>

