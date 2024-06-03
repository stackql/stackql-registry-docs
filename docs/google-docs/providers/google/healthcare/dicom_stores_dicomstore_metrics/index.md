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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dicom_stores_dicomstore_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.dicom_stores_dicomstore_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the DICOM store, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/dicomStores/&#123;dicom_store_id&#125;`. |
| <CopyableCode code="blobStorageSizeBytes" /> | `string` | Total blob storage bytes for all instances in the store. |
| <CopyableCode code="instanceCount" /> | `string` | Number of instances in the store. |
| <CopyableCode code="seriesCount" /> | `string` | Number of series in the store. |
| <CopyableCode code="structuredStorageSizeBytes" /> | `string` | Total structured storage bytes for all instances in the store. |
| <CopyableCode code="studyCount" /> | `string` | Number of studies in the store. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_dicomstore_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId" /> |
