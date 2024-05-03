---
title: projects__settings
hide_title: false
hide_table_of_contents: false
keywords:
  - projects__settings
  - toolresults
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
<tr><td><b>Name</b></td><td><code>projects__settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.toolresults.projects__settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the project's settings. Always of the form: projects/&#123;project-id&#125;/settings In update request: never set In response: always set |
| <CopyableCode code="defaultBucket" /> | `string` | The name of the Google Cloud Storage bucket to which results are written. By default, this is unset. In update request: optional In response: optional |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_getSettings" /> | `SELECT` | <CopyableCode code="projectId" /> |
