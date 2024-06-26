---
title: preference_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - preference_sets
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>preference_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.preference_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the preference set. |
| <CopyableCode code="description" /> | `string` | A description of the preference set. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the preference set was created. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the preference set was last updated. |
| <CopyableCode code="virtualMachinePreferences" /> | `object` | VirtualMachinePreferences enables you to create sets of assumptions, for example, a geographical location and pricing track, for your migrated virtual machines. The set of preferences influence recommendations for migrating virtual machine assets. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, preferenceSetsId, projectsId" /> | Gets the details of a preference set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the preference sets in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new preference set in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, preferenceSetsId, projectsId" /> | Deletes a preference set. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, preferenceSetsId, projectsId" /> | Updates the parameters of a preference set. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the preference sets in a given project and location. |
