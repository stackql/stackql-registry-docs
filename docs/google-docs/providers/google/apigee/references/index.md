---
title: references
hide_title: false
hide_table_of_contents: false
keywords:
  - references
  - apigee
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
<tr><td><b>Name</b></td><td><code>references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.references" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource id of this reference. Values must match the regular expression [\w\s\-.]+. |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description of this reference. |
| <CopyableCode code="refers" /> | `string` | Required. The id of the resource to which this reference refers. Must be the id of a resource that exists in the parent environment and is of the given resource_type. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource referred to by this reference. Valid values are 'KeyStore' or 'TrustStore'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_references_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, referencesId" /> | Gets a Reference resource. |
| <CopyableCode code="organizations_environments_references_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a Reference in the specified environment. |
| <CopyableCode code="organizations_environments_references_delete" /> | `DELETE` | <CopyableCode code="environmentsId, organizationsId, referencesId" /> | Deletes a Reference from an environment. Returns the deleted Reference resource. |
| <CopyableCode code="organizations_environments_references_update" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, referencesId" /> | Updates an existing Reference. Note that this operation has PUT semantics; it will replace the entirety of the existing Reference with the resource in the request body. |
