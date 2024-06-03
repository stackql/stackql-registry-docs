---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - servicedirectory
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicedirectory.namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters. |
| <CopyableCode code="uid" /> | `string` | Output only. The globally unique identifier of the namespace in the UUID4 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, namespacesId, projectsId" /> | Gets a namespace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all namespaces. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a namespace, and returns the new namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, namespacesId, projectsId" /> | Deletes a namespace. This also deletes all services and endpoints in the namespace. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, namespacesId, projectsId" /> | Updates a namespace. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all namespaces. |
