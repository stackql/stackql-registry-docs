---
title: managed_folders
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_folders
  - storage
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
<tr><td><b>Name</b></td><td><code>managed_folders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.managed_folders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the managed folder, including the bucket name and managed folder name. |
| <CopyableCode code="name" /> | `string` | The name of the managed folder. Required if not specified by URL parameter. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket containing this managed folder. |
| <CopyableCode code="createTime" /> | `string` | The creation time of the managed folder in RFC 3339 format. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For managed folders, this is always storage#managedFolder. |
| <CopyableCode code="metageneration" /> | `string` | The version of the metadata for this managed folder. Used for preconditions and for detecting changes in metadata. |
| <CopyableCode code="selfLink" /> | `string` | The link to this managed folder. |
| <CopyableCode code="updateTime" /> | `string` | The last update time of the managed folder metadata in RFC 3339 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, managedFolder" /> | Returns metadata of the specified managed folder. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Lists managed folders in the given bucket. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Creates a new managed folder. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket, managedFolder" /> | Permanently deletes a managed folder. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="bucket" /> | Lists managed folders in the given bucket. |
