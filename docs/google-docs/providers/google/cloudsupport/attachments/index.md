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
| <CopyableCode code="creator" /> | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
| <CopyableCode code="filename" /> | `string` | The filename of the attachment (e.g. `"graph.jpg"`). |
| <CopyableCode code="mimeType" /> | `string` | Output only. The MIME type of the attachment (e.g. text/plain). |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. The size of the attachment in bytes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="parent, parentType" /> |
