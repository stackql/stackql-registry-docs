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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studies_study_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="healthcare.studies_study_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobStorageSizeBytes" /> | `string` | Total blob storage bytes for all instances in the study. |
| <CopyableCode code="instanceCount" /> | `string` | Number of instances in the study. |
| <CopyableCode code="seriesCount" /> | `string` | Number of series in the study. |
| <CopyableCode code="structuredStorageSizeBytes" /> | `string` | Total structured storage bytes for all instances in the study. |
| <CopyableCode code="study" /> | `string` | The study resource path. For example, `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/dicomStores/&#123;dicom_store_id&#125;/dicomWeb/studies/&#123;study_uid&#125;`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_study_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, dicomStoresId, locationsId, projectsId, studiesId" /> |
