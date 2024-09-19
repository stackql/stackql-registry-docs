---
title: series_series_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - series_series_metrics
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>series_series_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>series_series_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.series_series_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobStorageSizeBytes" /> | `string` | Total blob storage bytes for all instances in the series. |
| <CopyableCode code="instanceCount" /> | `string` | Number of instances in the series. |
| <CopyableCode code="series" /> | `string` | The series resource path. For example, `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}/dicomWeb/studies/{study_uid}/series/{series_uid}`. |
| <CopyableCode code="structuredStorageSizeBytes" /> | `string` | Total structured storage bytes for all instances in the series. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_series_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId, seriesId, studiesId" /> | GetSeriesMetrics returns metrics for a series. |

## `SELECT` examples

GetSeriesMetrics returns metrics for a series.

```sql
SELECT
blobStorageSizeBytes,
instanceCount,
series,
structuredStorageSizeBytes
FROM google.healthcare.series_series_metrics
WHERE datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND seriesId = '{{ seriesId }}'
AND studiesId = '{{ studiesId }}';
```
