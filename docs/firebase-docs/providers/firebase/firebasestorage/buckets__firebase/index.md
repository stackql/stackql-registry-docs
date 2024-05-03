---
title: buckets__firebase
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets__firebase
  - firebasestorage
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets__firebase</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebasestorage.buckets__firebase" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_buckets_addFirebase" /> | `EXEC` | <CopyableCode code="bucketsId, projectsId" /> | Links a Google Cloud Storage bucket to a Firebase project. |
| <CopyableCode code="projects_buckets_removeFirebase" /> | `EXEC` | <CopyableCode code="bucketsId, projectsId" /> | Unlinks a linked Google Cloud Storage bucket from a Firebase project. |
