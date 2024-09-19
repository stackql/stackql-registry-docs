---
title: image_import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - image_import_jobs
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>image_import_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.image_import_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource path of the ImageImportJob. |
| <CopyableCode code="cloudStorageUri" /> | `string` | Output only. The path to the Cloud Storage file from which the image should be imported. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the image import was created (as an API call, not when it was actually created in the target). |
| <CopyableCode code="createdResources" /> | `array` | Output only. The resource paths of the resources created by the image import job. |
| <CopyableCode code="diskImageTargetDetails" /> | `object` | The target details of the image resource that will be created by the import job. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the image import was ended. |
| <CopyableCode code="errors" /> | `array` | Output only. Provides details on the error that led to the image import state in case of an error. |
| <CopyableCode code="machineImageTargetDetails" /> | `object` | The target details of the machine image resource that will be created by the image import job. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the image import. |
| <CopyableCode code="steps" /> | `array` | Output only. The image import steps list representing its progress. |
| <CopyableCode code="warnings" /> | `array` | Output only. Warnings that occurred during the image import. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageImportJobsId, imageImportsId, locationsId, projectsId" /> | Gets details of a single ImageImportJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Lists ImageImportJobs in a given project. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="imageImportJobsId, imageImportsId, locationsId, projectsId" /> | Initiates the cancellation of a running clone job. |

## `SELECT` examples

Lists ImageImportJobs in a given project.

```sql
SELECT
name,
cloudStorageUri,
createTime,
createdResources,
diskImageTargetDetails,
endTime,
errors,
machineImageTargetDetails,
state,
steps,
warnings
FROM google.vmmigration.image_import_jobs
WHERE imageImportsId = '{{ imageImportsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
