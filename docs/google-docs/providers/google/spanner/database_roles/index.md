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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>database_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.database_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The name of the database role. Values are of the form `projects//instances//databases//databaseRoles/` where `` is as specified in the `CREATE ROLE` DDL statement. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_databases_database_roles_list" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Lists Cloud Spanner database roles. |

## `SELECT` examples

Lists Cloud Spanner database roles.

```sql
SELECT
name
FROM google.spanner.database_roles
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
