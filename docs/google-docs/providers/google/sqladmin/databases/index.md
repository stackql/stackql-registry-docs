---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - sqladmin
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the database in the Cloud SQL instance. This does not include the project ID or instance name. |
| `collation` | `string` | The Cloud SQL collation value. |
| `kind` | `string` | This is always `sql#database`. |
| `project` | `string` | The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. |
| `instance` | `string` | The name of the Cloud SQL instance. This does not include the project ID. |
| `sqlserverDatabaseDetails` | `object` | Represents a Sql Server database on the Cloud SQL instance. |
| `etag` | `string` | This field is deprecated and will be removed from a future version of the API. |
| `selfLink` | `string` | The URI of this resource. |
| `charset` | `string` | The Cloud SQL charset value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `database, instance, project` | Retrieves a resource containing information about a database inside a Cloud SQL instance. |
| `list` | `SELECT` | `instance, project` | Lists databases in the specified Cloud SQL instance. |
| `insert` | `INSERT` | `instance, project` | Inserts a resource containing information about a database inside a Cloud SQL instance. **Note:** You can't modify the default character set and collation. |
| `delete` | `DELETE` | `database, instance, project` | Deletes a database from a Cloud SQL instance. |
| `patch` | `EXEC` | `database, instance, project` | Partially updates a resource containing information about a database inside a Cloud SQL instance. This method supports patch semantics. |
| `update` | `EXEC` | `database, instance, project` | Updates a resource containing information about a database inside a Cloud SQL instance. |
