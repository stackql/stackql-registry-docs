---
title: projects__admin_sdk_config
hide_title: false
hide_table_of_contents: false
keywords:
  - projects__admin_sdk_config
  - firebase
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
<tr><td><b>Name</b></td><td><code>projects__admin_sdk_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebase.projects__admin_sdk_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseURL" /> | `string` | The default Firebase Realtime Database URL. |
| <CopyableCode code="locationId" /> | `string` | The ID of the Project's default GCP resource location. The location is one of the available [GCP resource locations](https://firebase.google.com/docs/projects/locations). This field is omitted if the default GCP resource location has not been finalized yet. To set a Project's default GCP resource location, call [`FinalizeDefaultLocation`](../projects.defaultLocation/finalize) after you add Firebase resources to the Project. |
| <CopyableCode code="projectId" /> | `string` | Immutable. A user-assigned unique identifier for the `FirebaseProject`. This identifier may appear in URLs or names for some Firebase resources associated with the Project, but it should generally be treated as a convenience alias to reference the Project. |
| <CopyableCode code="storageBucket" /> | `string` | The default Cloud Storage for Firebase storage bucket name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_getAdminSdkConfig" /> | `SELECT` | <CopyableCode code="projectsId" /> |
