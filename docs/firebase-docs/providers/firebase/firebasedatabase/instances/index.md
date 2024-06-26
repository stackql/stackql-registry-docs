---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - firebasedatabase
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebasedatabase.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The fully qualified resource name of the database instance, in the form: `projects/&#123;project-number&#125;/locations/&#123;location-id&#125;/instances/&#123;database-id&#125;`. |
| <CopyableCode code="databaseUrl" /> | `string` | Output only. Output Only. The globally unique hostname of the database. |
| <CopyableCode code="project" /> | `string` | Output only. The resource name of the project this instance belongs to. For example: `projects/&#123;project-number&#125;`. |
| <CopyableCode code="state" /> | `string` | Output only. The database's lifecycle state. Read-only. |
| <CopyableCode code="type" /> | `string` | Immutable. The database instance type. On creation only USER_DATABASE is allowed, which is also the default when omitted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_instances_get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets the DatabaseInstance identified by the specified resource name. |
| <CopyableCode code="projects_locations_instances_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists each DatabaseInstance associated with the specified parent project. The list items are returned in no particular order, but will be a consistent view of the database instances when additional requests are made with a `pageToken`. The resulting list contains instances in any STATE. The list results may be stale by a few seconds. Use GetDatabaseInstance for consistent reads. |
| <CopyableCode code="projects_locations_instances_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Requests that a new DatabaseInstance be created. The state of a successfully created DatabaseInstance is ACTIVE. Only available for projects on the Blaze plan. Projects can be upgraded using the Cloud Billing API https://cloud.google.com/billing/reference/rest/v1/projects/updateBillingInfo. Note that it might take a few minutes for billing enablement state to propagate to Firebase systems. |
| <CopyableCode code="projects_locations_instances_delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Marks a DatabaseInstance to be deleted. The DatabaseInstance will be set to the DELETED state for 20 days, and will be purged within 30 days. The default database cannot be deleted. IDs for deleted database instances may never be recovered or re-used. The Database may only be deleted if it is already in a DISABLED state. |
| <CopyableCode code="projects_locations_instances_disable" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Disables a DatabaseInstance. The database can be re-enabled later using ReenableDatabaseInstance. When a database is disabled, all reads and writes are denied, including view access in the Firebase console. |
| <CopyableCode code="projects_locations_instances_reenable" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Enables a DatabaseInstance. The database must have been disabled previously using DisableDatabaseInstance. The state of a successfully reenabled DatabaseInstance is ACTIVE. |
| <CopyableCode code="projects_locations_instances_undelete" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Restores a DatabaseInstance that was previously marked to be deleted. After the delete method is used, DatabaseInstances are set to the DELETED state for 20 days, and will be purged within 30 days. Databases in the DELETED state can be undeleted without losing any data. This method may only be used on a DatabaseInstance in the DELETED state. Purged DatabaseInstances may not be recovered. |
