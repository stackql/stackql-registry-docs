---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
  - cloudsupport
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudsupport.comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for the comment. |
| <CopyableCode code="body" /> | `string` | The full comment body. Maximum of 12800 characters. This can contain rich text syntax. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when this comment was created. |
| <CopyableCode code="creator" /> | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
| <CopyableCode code="plainTextBody" /> | `string` | Output only. DEPRECATED. An automatically generated plain text version of body with all rich text syntax stripped. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Retrieve all comments associated with the Case object. Here is an example of calling this endpoint using cURL: ```shell case="projects/cloud-support-qa-premium/cases/43595344" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case/comments" ``` |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Add a new comment to the specified Case. The comment object must have the following fields set: body. Here is an example of calling this endpoint using cURL: ```shell case="projects/some-project/cases/43591344" curl \ --request POST \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header 'Content-Type: application/json' \ --data '&#123; "body": "This is a test comment." &#125;' \ "https://cloudsupport.googleapis.com/v2/$case/comments" ``` |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Retrieve all comments associated with the Case object. Here is an example of calling this endpoint using cURL: ```shell case="projects/cloud-support-qa-premium/cases/43595344" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case/comments" ``` |
