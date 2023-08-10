---
title: database_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - database_roles
  - spanner
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
<tr><td><b>Name</b></td><td><code>database_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.database_roles</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_instances_databases_database_roles_list` | `SELECT` | `databasesId, instancesId, projectsId` |
| `_projects_instances_databases_database_roles_list` | `EXEC` | `databasesId, instancesId, projectsId` |
