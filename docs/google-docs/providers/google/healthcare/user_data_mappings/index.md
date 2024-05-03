---
title: user_data_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_data_mappings
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
<tr><td><b>Name</b></td><td><code>user_data_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.user_data_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the User data mapping, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/userDataMappings/&#123;user_data_mapping_id&#125;`. |
| <CopyableCode code="archiveTime" /> | `string` | Output only. Indicates the time when this mapping was archived. |
| <CopyableCode code="archived" /> | `boolean` | Output only. Indicates whether this mapping is archived. |
| <CopyableCode code="dataId" /> | `string` | Required. A unique identifier for the mapped resource. |
| <CopyableCode code="resourceAttributes" /> | `array` | Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute. |
| <CopyableCode code="userId" /> | `string` | Required. User's UUID provided by the client. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Gets the specified User data mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the User data mappings in the specified consent store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Creates a new User data mapping in the parent consent store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Deletes the specified User data mapping. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the User data mappings in the specified consent store. |
| <CopyableCode code="archive" /> | `EXEC` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Archives the specified User data mapping. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Updates the specified User data mapping. |
