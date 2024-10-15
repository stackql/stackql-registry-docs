---
title: test_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - test_summaries
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

Creates, updates, deletes, gets or lists a <code>test_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.test_summaries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_summaries', value: 'view', },
        { label: 'test_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="application_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_updates_test_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="grade" /> | `text` | field from the `properties` object |
| <CopyableCode code="inplace_upgrades_test_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_updates_test_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="testSummaryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_run_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_summary_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a Test Summary. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, testSummaryName" /> | Gets a Test Summary with specific name from all the Test Summaries of all the packages under a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists the Test Summaries of all the packages under a Test Base Account. |

## `SELECT` examples

Lists the Test Summaries of all the packages under a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_summaries', value: 'view', },
        { label: 'test_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
application_name,
application_version,
execution_status,
feature_updates_test_summary,
grade,
inplace_upgrades_test_summary,
package_id,
package_tags,
resourceGroupName,
security_updates_test_summary,
subscriptionId,
testBaseAccountName,
testSummaryName,
test_run_time,
test_status,
test_summary_id
FROM azure_extras.test_base.vw_test_summaries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.test_summaries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

