---
title: postgresql_instances_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - postgresql_instances_credentials
  - databases
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postgresql_instances_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.postgresql_instances_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="password" /> | `string` | The randomly-generated root password for the Managed Database instance. |
| <CopyableCode code="username" /> | `string` | The root username for the Managed Database instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDatabasesPostgreSQLInstanceCredentials" /> | `SELECT` | <CopyableCode code="instanceId" /> | Display the root username and password for an accessible Managed PostgreSQL Database.<br /><br />The Database must have an `active` status to perform this command.<br /> |
| <CopyableCode code="_getDatabasesPostgreSQLInstanceCredentials" /> | `EXEC` | <CopyableCode code="instanceId" /> | Display the root username and password for an accessible Managed PostgreSQL Database.<br /><br />The Database must have an `active` status to perform this command.<br /> |
| <CopyableCode code="postDatabasesPostgreSQLInstanceCredentialsReset" /> | `EXEC` | <CopyableCode code="instanceId" /> | Reset the root password for a Managed PostgreSQL Database.<br /><br />Requires `read_write` access to the Database.<br /><br />A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/&#123;instanceId&#125;/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.<br /><br />Only unrestricted Users can access this command, and have access regardless of the acting token's OAuth scopes.<br /><br />**Note**: Note that it may take several seconds for credentials to reset.<br /> |
