---
title: image_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - image_imports
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.image_imports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource path of the ImageImport. |
| <CopyableCode code="cloudStorageUri" /> | `string` | Immutable. The path to the Cloud Storage file from which the image should be imported. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the image import was created. |
| <CopyableCode code="diskImageTargetDefaults" /> | `object` | The target details of the image resource that will be created by the import job. |
| <CopyableCode code="encryption" /> | `object` | Encryption message describes the details of the applied encryption. |
| <CopyableCode code="recentImageImportJobs" /> | `array` | Output only. The result of the most recent runs for this ImageImport. All jobs for this ImageImport can be listed via ListImageImportJobs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Gets details of a single ImageImport. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ImageImports in a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ImageImport in a given project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Deletes a single ImageImport. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists ImageImports in a given project. |
