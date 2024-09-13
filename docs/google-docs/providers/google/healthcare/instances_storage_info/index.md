---
title: instances_storage_info
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_storage_info
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

Creates, updates, deletes or gets an <code>instances_storage_info</code> resource or lists <code>instances_storage_info</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_storage_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.instances_storage_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobStorageInfo" /> | `object` | BlobStorageInfo contains details about the data stored in Blob Storage for the referenced resource. Note: Storage class is only valid for DICOM and hence will only be populated for DICOM resources. |
| <CopyableCode code="referencedResource" /> | `string` | The resource whose storage info is returned. For example: `projects/{projectID}/locations/{locationID}/datasets/{datasetID}/dicomStores/{dicomStoreID}/dicomWeb/studies/{studyUID}/series/{seriesUID}/instances/{instanceUID}` |
| <CopyableCode code="structuredStorageInfo" /> | `object` | StructuredStorageInfo contains details about the data stored in Structured Storage for the referenced resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_storage_info" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, instancesId, locationsId, projectsId, seriesId, studiesId" /> | GetStorageInfo returns the storage info of the specified resource. |

## `SELECT` examples

GetStorageInfo returns the storage info of the specified resource.

```sql
SELECT
blobStorageInfo,
referencedResource,
structuredStorageInfo
FROM google.healthcare.instances_storage_info
WHERE datasetsId = '{{ datasetsId }}'
AND dicomStoresId = '{{ dicomStoresId }}'
AND instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND seriesId = '{{ seriesId }}'
AND studiesId = '{{ studiesId }}'; 
```
