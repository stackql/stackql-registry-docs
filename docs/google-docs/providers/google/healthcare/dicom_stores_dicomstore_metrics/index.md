---
title: dicom_stores_dicomstore_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - dicom_stores_dicomstore_metrics
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

Creates, updates, deletes or gets an <code>dicom_stores_dicomstore_metric</code> resource or lists <code>dicom_stores_dicomstore_metrics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dicom_stores_dicomstore_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.dicom_stores_dicomstore_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the DICOM store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/dicomStores/{dicom_store_id}`. |
| <CopyableCode code="blobStorageSizeBytes" /> | `string` | Total blob storage bytes for all instances in the store. |
| <CopyableCode code="instanceCount" /> | `string` | Number of instances in the store. |
| <CopyableCode code="seriesCount" /> | `string` | Number of series in the store. |
| <CopyableCode code="structuredStorageSizeBytes" /> | `string` | Total structured storage bytes for all instances in the store. |
| <CopyableCode code="studyCount" /> | `string` | Number of studies in the store. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_dicomstore_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> | Gets metrics associated with the DICOM store. |

## `SELECT` examples

Gets metrics associated with the DICOM store.

```sql
SELECT
name,
blobStorageSizeBytes,
instanceCount,
seriesCount,
structuredStorageSizeBytes,
studyCount
FROM google.healthcare.dicom_stores_dicomstore_metrics
WHERE datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
