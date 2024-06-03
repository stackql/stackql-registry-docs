---
title: authorized_views
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_views
  - bigtableadmin
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
<tr><td><b>Name</b></td><td><code>authorized_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.authorized_views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of this AuthorizedView. Values are of the form `projects/&#123;project&#125;/instances/&#123;instance&#125;/tables/&#123;table&#125;/authorizedViews/&#123;authorized_view&#125;` |
| <CopyableCode code="deletionProtection" /> | `boolean` | Set to true to make the AuthorizedView protected against deletion. The parent Table and containing Instance cannot be deleted if an AuthorizedView has this bit set. |
| <CopyableCode code="etag" /> | `string` | The etag for this AuthorizedView. If this is provided on update, it must match the server's etag. The server returns ABORTED error on a mismatched etag. |
| <CopyableCode code="subsetView" /> | `object` | Defines a simple AuthorizedView that is a subset of the underlying Table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizedViewsId, instancesId, projectsId, tablesId" /> | Gets information from a specified AuthorizedView. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Lists all AuthorizedViews from a specific table. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Creates a new AuthorizedView in a table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizedViewsId, instancesId, projectsId, tablesId" /> | Permanently deletes a specified AuthorizedView. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="authorizedViewsId, instancesId, projectsId, tablesId" /> | Updates an AuthorizedView in a table. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Lists all AuthorizedViews from a specific table. |
