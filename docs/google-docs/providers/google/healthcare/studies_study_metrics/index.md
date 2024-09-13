
---
title: studies_study_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - studies_study_metrics
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

Creates, updates, deletes or gets an <code>studies_study_metric</code> resource or lists <code>studies_study_metrics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studies_study_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.studies_study_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobStorageSizeBytes" /> | `string` | Total blob storage bytes for all instances in the study. |
| <CopyableCode code="instanceCount" /> | `string` | Number of instances in the study. |
| <CopyableCode code="seriesCount" /> | `string` | Number of series in the study. |
| <CopyableCode code="structuredStorageSizeBytes" /> | `string` | Total structured storage bytes for all instances in the study. |
| <CopyableCode code="study" /> | `string` | The study resource path. For example, `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}/dicomWeb/studies/{study_uid}`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_study_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId, studiesId" /> | GetStudyMetrics returns metrics for a study. |

## `SELECT` examples

GetStudyMetrics returns metrics for a study.

```sql
SELECT
blobStorageSizeBytes,
instanceCount,
seriesCount,
structuredStorageSizeBytes,
study
FROM google.healthcare.studies_study_metrics
WHERE datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND studiesId = '{{ studiesId }}'; 
```
