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
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name of the comment. |
| <CopyableCode code="body" /> | `string` | The full comment body. Maximum of 12800 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the comment was created. |
| <CopyableCode code="creator" /> | `object` | An Actor represents an entity that performed an action. For example, an actor could be a user who posted a comment on a support case, a user who uploaded an attachment, or a service account that created a support case. |
| <CopyableCode code="plainTextBody" /> | `string` | Output only. DEPRECATED. DO NOT USE. A duplicate of the `body` field. This field is only present for legacy reasons. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | List all the comments associated with a case. EXAMPLES: cURL: ```shell case="projects/some-project/cases/43595344" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case/comments" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version=&#123;api_version&#125;", ) request = ( supportApiService.cases() .comments() .list(parent="projects/some-project/cases/43595344") ) print(request.execute()) ``` |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Add a new comment to a case. The comment must have the following fields set: `body`. EXAMPLES: cURL: ```shell case="projects/some-project/cases/43591344" curl \ --request POST \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ --header 'Content-Type: application/json' \ --data '&#123; "body": "This is a test comment." &#125;' \ "https://cloudsupport.googleapis.com/v2/$case/comments" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version=&#123;api_version&#125;", ) request = ( supportApiService.cases() .comments() .create( parent="projects/some-project/cases/43595344", body=&#123;"body": "This is a test comment."&#125;, ) ) print(request.execute()) ``` |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | List all the comments associated with a case. EXAMPLES: cURL: ```shell case="projects/some-project/cases/43595344" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case/comments" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version=&#123;api_version&#125;", ) request = ( supportApiService.cases() .comments() .list(parent="projects/some-project/cases/43595344") ) print(request.execute()) ``` |
