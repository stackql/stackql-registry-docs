---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - alloydb
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the resource in the form of projects/&#123;project&#125;/locations/&#123;location&#125;/cluster/&#123;cluster&#125;/users/&#123;user&#125;. |
| <CopyableCode code="databaseRoles" /> | `array` | Optional. List of database roles this user has. The database role strings are subject to the PostgreSQL naming conventions. |
| <CopyableCode code="password" /> | `string` | Input only. Password for the user. |
| <CopyableCode code="userType" /> | `string` | Optional. Type of this user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId, usersId" /> | Gets details of a single User. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Lists Users in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Creates a new User in a given project, location, and cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, projectsId, usersId" /> | Deletes a single User. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, projectsId, usersId" /> | Updates the parameters of a single User. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Lists Users in a given project and location. |
