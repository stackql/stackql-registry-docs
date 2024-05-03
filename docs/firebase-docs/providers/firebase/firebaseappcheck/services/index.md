---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - firebaseappcheck
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebaseappcheck.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The relative resource name of the service configuration object, in the format: ``` projects/&#123;project_number&#125;/services/&#123;service_id&#125; ``` Note that the `service_id` element must be a supported service ID. Currently, the following service IDs are supported: * `firebasestorage.googleapis.com` (Cloud Storage for Firebase) * `firebasedatabase.googleapis.com` (Firebase Realtime Database) * `firestore.googleapis.com` (Cloud Firestore) |
| <CopyableCode code="enforcementMode" /> | `string` | Required. The App Check enforcement mode for this service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_services_get" /> | `SELECT` | <CopyableCode code="projectsId, servicesId" /> | Gets the Service configuration for the specified service name. |
| <CopyableCode code="projects_services_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all Service configurations for the specified project. Only Services which were explicitly configured using UpdateService or BatchUpdateServices will be returned. |
| <CopyableCode code="projects_services_batchUpdate" /> | `EXEC` | <CopyableCode code="projectsId" /> | Atomically updates the specified Service configurations. |
| <CopyableCode code="projects_services_patch" /> | `EXEC` | <CopyableCode code="projectsId, servicesId" /> | Updates the specified Service configuration. |
