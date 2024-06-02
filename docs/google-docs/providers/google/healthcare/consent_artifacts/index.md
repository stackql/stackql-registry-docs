---
title: consent_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - consent_artifacts
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
<tr><td><b>Name</b></td><td><code>consent_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="healthcare.consent_artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the Consent artifact, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consentArtifacts/&#123;consent_artifact_id&#125;`. Cannot be changed after creation. |
| <CopyableCode code="consentContentScreenshots" /> | `array` | Optional. Screenshots, PDFs, or other binary information documenting the user's consent. |
| <CopyableCode code="consentContentVersion" /> | `string` | Optional. An string indicating the version of the consent information shown to the user. |
| <CopyableCode code="guardianSignature" /> | `object` | User signature. |
| <CopyableCode code="metadata" /> | `object` | Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version. |
| <CopyableCode code="userId" /> | `string` | Required. User's UUID provided by the client. |
| <CopyableCode code="userSignature" /> | `object` | User signature. |
| <CopyableCode code="witnessSignature" /> | `object` | User signature. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Gets the specified Consent artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the Consent artifacts in the specified consent store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Creates a new Consent artifact in the parent consent store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Deletes the specified Consent artifact. Fails if the artifact is referenced by the latest revision of any Consent. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the Consent artifacts in the specified consent store. |
