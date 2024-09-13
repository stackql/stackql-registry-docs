---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - attachments
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>attachment</code> resource or lists <code>attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudsupport.attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the attachment. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the attachment was created. |
| <CopyableCode code="creator" /> | `object` | An Actor represents an entity that performed an action. For example, an actor could be a user who posted a comment on a support case, a user who uploaded an attachment, or a service account that created a support case. |
| <CopyableCode code="filename" /> | `string` | The filename of the attachment (e.g. `"graph.jpg"`). |
| <CopyableCode code="mimeType" /> | `string` | Output only. The MIME type of the attachment (e.g. text/plain). |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. The size of the attachment in bytes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | List all the attachments associated with a support case. EXAMPLES: cURL: ```shell case="projects/some-project/cases/23598314" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case/attachments" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = ( supportApiService.cases() .attachments() .list(parent="projects/some-project/cases/43595344") ) print(request.execute()) ``` |

## `SELECT` examples

List all the attachments associated with a support case. EXAMPLES: cURL: ```shell case="projects/some-project/cases/23598314" curl \ --header "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://cloudsupport.googleapis.com/v2/$case/attachments" ``` Python: ```python import googleapiclient.discovery api_version = "v2" supportApiService = googleapiclient.discovery.build( serviceName="cloudsupport", version=api_version, discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}", ) request = ( supportApiService.cases() .attachments() .list(parent="projects/some-project/cases/43595344") ) print(request.execute()) ```

```sql
SELECT
name,
createTime,
creator,
filename,
mimeType,
sizeBytes
FROM google.cloudsupport.attachments
WHERE parent = '{{ parent }}'
AND parentType = '{{ parentType }}'; 
```
