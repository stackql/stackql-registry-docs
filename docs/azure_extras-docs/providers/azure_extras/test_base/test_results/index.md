---
title: test_results
hide_title: false
hide_table_of_contents: false
keywords:
  - test_results
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

Creates, updates, deletes, gets or lists a <code>test_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.test_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_results', value: 'view', },
        { label: 'test_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="analysis_summaries" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="baseline_test_result_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_image_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_image_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="execution_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_party_apps" /> | `text` | field from the `properties` object |
| <CopyableCode code="flighting_ring" /> | `text` | field from the `properties` object |
| <CopyableCode code="grade" /> | `text` | field from the `properties` object |
| <CopyableCode code="inplace_upgrade_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="interop_media_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="interop_media_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_download_data_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_video_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="kb_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="osUpdateType" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_version_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="testResultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_run_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a Test Result. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName, testResultName" /> | Get the Test Result by Id with specified OS Update type for a Test Base Package. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="osUpdateType, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the Test Results with specified OS Update type for a Test Base Package. Can be filtered by osName, releaseName, flightingRing, buildVersion, buildRevision. |

## `SELECT` examples

Lists all the Test Results with specified OS Update type for a Test Base Package. Can be filtered by osName, releaseName, flightingRing, buildVersion, buildRevision.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_results', value: 'view', },
        { label: 'test_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
analysis_summaries,
application_name,
application_version,
baseline_test_result_id,
build_revision,
build_version,
custom_image_display_name,
custom_image_id,
execution_status,
first_party_apps,
flighting_ring,
grade,
inplace_upgrade_properties,
interop_media_type,
interop_media_version,
is_download_data_available,
is_video_available,
kb_number,
osUpdateType,
os_name,
packageName,
package_id,
package_version,
release_name,
release_version_date,
resourceGroupName,
subscriptionId,
testBaseAccountName,
testResultName,
test_end_time,
test_run_time,
test_start_time,
test_status,
test_type
FROM azure_extras.test_base.vw_test_results
WHERE osUpdateType = '{{ osUpdateType }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.test_results
WHERE osUpdateType = '{{ osUpdateType }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

