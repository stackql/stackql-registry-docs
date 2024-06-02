---
title: data_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_policies
  - bigquerydatapolicy
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
<tr><td><b>Name</b></td><td><code>data_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigquerydatapolicy.data_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of this data policy, in the format of `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/dataPolicies/&#123;data_policy_id&#125;`. |
| <CopyableCode code="dataMaskingPolicy" /> | `object` | The data masking policy that is used to specify data masking rule. |
| <CopyableCode code="dataPolicyId" /> | `string` | User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as &#123;data_policy_id&#125; in part of the resource name. |
| <CopyableCode code="dataPolicyType" /> | `string` | Type of data policy. |
| <CopyableCode code="policyTag" /> | `string` | Policy tag resource name, in the format of `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/taxonomies/&#123;taxonomy_id&#125;/policyTags/&#123;policyTag_id&#125;`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Gets the data policy specified by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all of the data policies in the specified parent project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), policy tag, and data policy type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Deletes the data policy specified by its resource name. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List all of the data policies in the specified parent project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Updates the metadata for an existing data policy. The target data policy can be specified by the resource name. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="dataPoliciesId, locationsId, projectsId" /> | Renames the id (display name) of the specified data policy. |
