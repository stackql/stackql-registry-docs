---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - cloudresourcemanager
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
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.organizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the organization. This is the organization's relative path in the API. Its format is "organizations/[organization_id]". For example, "organizations/1234". |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when the Organization was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Timestamp when the Organization was requested for deletion. |
| <CopyableCode code="directoryCustomerId" /> | `string` | Immutable. The G Suite / Workspace customer id used in the Directory API. |
| <CopyableCode code="displayName" /> | `string` | Output only. A human-readable string that refers to the organization in the Google Cloud Console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, "google.com") of the Google Workspace customer that owns the organization. |
| <CopyableCode code="etag" /> | `string` | Output only. A checksum computed by the server based on the current value of the Organization resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="state" /> | `string` | Output only. The organization's current lifecycle state. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when the Organization was last modified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Fetches an organization resource identified by the specified resource name. |
| <CopyableCode code="search" /> | `EXEC` |  | Searches organization resources that are visible to the user and satisfy the specified filter. This method returns organizations in an unspecified order. New organizations do not necessarily appear at the end of the results, and may take a small amount of time to appear. Search will only return organizations on which the user has the permission `resourcemanager.organizations.get` |
