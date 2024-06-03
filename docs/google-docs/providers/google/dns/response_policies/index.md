---
title: response_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - response_policies
  - dns
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
<tr><td><b>Name</b></td><td><code>response_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.response_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the resource; defined by the server (output only). |
| <CopyableCode code="description" /> | `string` | User-provided description for this Response Policy. |
| <CopyableCode code="gkeClusters" /> | `array` | The list of Google Kubernetes Engine clusters to which this response policy is applied. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="labels" /> | `object` | User labels. |
| <CopyableCode code="networks" /> | `array` | List of network names specifying networks to which this policy is applied. |
| <CopyableCode code="responsePolicyName" /> | `string` | User assigned name for this Response Policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, responsePolicy" /> | Fetches the representation of an existing Response Policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Enumerates all Response Policies associated with a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="project" /> | Creates a new Response Policy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, responsePolicy" /> | Deletes a previously created Response Policy. Fails if the response policy is non-empty or still being referenced by a network. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project, responsePolicy" /> | Applies a partial update to an existing Response Policy. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="project, responsePolicy" /> | Updates an existing Response Policy. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="project" /> | Enumerates all Response Policies associated with a project. |
